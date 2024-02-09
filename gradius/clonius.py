import pygame
from pygame.locals import *
from pygame import mixer
import math
import random

from player import *
from spritesheet import *
from enemies import *
from hud import *
from explosions import *
from projectiles import *
from powerups import *


pygame.init()
mixer.init()
winheight = 480
winwidth = 640 
gamewindow = pygame.display.set_mode((winwidth,winheight))
pygame.display.set_caption("Clonius")

titlefontold = 'freesansbold.ttf'
titlefont = 'fonts/Cybersomething.ttf'
hud = Hud(gamewindow, (winwidth, winheight), titlefont, titlefont)
titlebg = pygame.image.load('images/titlebg.png')

exit = False
running = True 

clock = pygame.time.Clock()
FPS = 60
dt = 0


ships_sheet = spritesheet('images/ships.png')
projs_sheet = spritesheet('images/projectiles.png')
asset_sheet = spritesheet('images/assetpack.png')

player = Player(50,240,ships_sheet.image_at((32,64,16,16), "black"))
playerprojgroup = pygame.sprite.Group()
playerhp = 30
playerdamage = 2
gamestate = 0


enemiesgroup = pygame.sprite.Group()
enemyprojgroup = pygame.sprite.Group()
bossprojgroup =  pygame.sprite.Group()
explosionsgroup = pygame.sprite.Group()
powerupgroup = pygame.sprite.Group()

#code for background music
bgmchannel = pygame.mixer.Channel(0)
backgm = pygame.mixer.Sound('sounds/maingamesound.mp3')
backgm.set_volume(.5)
bgmchannel.play(backgm, -1)
#channel 0 for background music
#channel 1 for player shooting
#channel 2 for enemy shooting
#channel 3 for healing
healchannel = pygame.mixer.Channel(3)


#load background images
bg_images = []
for i in range(1,7):
    bg_image = pygame.image.load("images/bglayers/background" + str(i) + ".png").convert_alpha()
    bg_image = pygame.transform.scale(bg_image, (bg_image.get_width(), winheight))
    bg_images.append(bg_image)
bg_width = bg_images[0].get_width()
scroll = 0
tiles = math.ceil(winwidth  / bg_width) + 1

#lists of sprites for each class
fighter_list = [
    #32x32 sprites after resizing
    (32,32,8,8), #purple 
    (40,32,8,8), #red
    (48,32,8,8), #blue
    (56,32,8,8), #green
    (64,32,8,8), #light blue
    (72,32,8,8),  #yellow
    #second row on sprites:
    (32,40,8,8), #blue
    (56,40,8,8), #yellow
    (72,40,8,8)  #white
]

bomber_list = [
    #40x40 sprites after resizing
    (8,0,8,8), #white
    (8,8,8,8), #orange
    (8,16,8,8), #green
    (8,24,8,8), #purple
    (8,32,8,8)  #red
]

boss_list = [
    #64x64 sprites after resizing
    (32,48,16,16), #purple
    (48,48,16,16), #orange
    (64,48,16,16), #green
    (64,64,16,16)  #red-orange
]

fighterBullet = pygame.transform.scale_by(pygame.transform.rotate(projs_sheet.image_at((16,40,8,8), "black"), 135),2.5)
bomberBullet = pygame.transform.scale_by(pygame.transform.rotate(projs_sheet.image_at((0,40,8,8), "black"), 135), 4)
bossBullet = pygame.transform.scale_by(pygame.transform.rotate(projs_sheet.image_at((8,56,8,8), "black"), 135), 4)

bomberchance = 10
boss_spawned = False
spawn_rate = 750


def spawnenemies():    #responsible for generating enemies
    global bomberchance
    global boss_spawned

    #spawns a boss every 50 score and stops spawning of everything else
    if (playerscore % 50) == 0 and playerscore != 0 and boss_spawned == False:
            boss_spawned = True
            enemiesgroup.add(Boss(680, random.randrange(32, 480 - 64), ships_sheet.image_at(boss_list[random.randint(0,3)], "black"), bossBullet, bossprojgroup))
    if not boss_spawned:
        if random.randrange(0, 100) <= bomberchance:
            enemiesgroup.add(Bomber(680, random.randrange(32, 480 - 40), ships_sheet.image_at(bomber_list[random.randint(0,4)], "black"), bomberBullet, enemyprojgroup))
        else:
            enemiesgroup.add(Fighter(680, random.randrange(32, 480 - 32), ships_sheet.image_at(fighter_list[random.randint(0,8)], "black"), fighterBullet, enemyprojgroup))
    
    #increases the chance for a bomber to spawn
    if (playerscore % 5) == 0 and playerscore != 0:
        bomberchance += 1
        #at every 5 playerscore increases the chance for bomber by 1


def genPowerup():
    heartchance = 10 #makes it a 10% chance to get a heart
    if random.randrange(0, 100) <= heartchance:
        powerupgroup.add(Health(enemy.x, enemy.y, asset_sheet.image_at((16,0,8,8), "black")))

dead_var = 0    #used to make sure teh death sound wasn't played multiple times
#used for making countdown in game
startingscreen = True
tic_var = pygame.time.get_ticks()
#used for setting enemy spawn rate
oldTime = 0
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    
    if gamestate == 0:  #starting screen
        bgmchannel.unpause()

        if keys[pygame.K_r]:
            gamestate = 1

       
        gamewindow.fill('black')
        gamewindow.blit(titlebg, (0,0))
        hud.main_menu("Clonius IV", "purple")
        hud.place_text("Press 'R' to Play!", "purple", 0, 60)
        

        pygame.display.flip()

    if gamestate == 1:  #resets playerscore, loading screen for game
        #startingscreen = True
        dead_var = 0
        playerscore = 0
        player.health = playerhp
        #empties all the classes to get a fresh board
        enemiesgroup.empty()
        enemyprojgroup.empty()
        bossprojgroup.empty()
        playerprojgroup.empty()
        powerupgroup.empty()
        
        gamestate = 1.1
        
    if gamestate == 1.1: #main game
        
        #makes moving background
        gamewindow.fill("black")
        for x in range(0, tiles):
            speed = 1
            for i in bg_images:
                gamewindow.blit(i, (x * bg_width - scroll * speed/1.5, 0))
                speed += 0.3
        scroll += 5
        if abs(scroll) > bg_width:
            scroll = 0

        if keys[pygame.K_w]:
            player.y -= 300*dt
        if keys[pygame.K_s]:
            player.y += 300*dt
        if keys[pygame.K_SPACE]:
            player.fire(projs_sheet.image_at((0,8,8,8), "black"),  playerprojgroup)
        
        
        
        #adds a starting sequence
        seconds = (pygame.time.get_ticks()-tic_var)/1000
        if seconds >= 5.5 and startingscreen == True:
            hud.main_menu("", "purple", 1000,1000)
            startingscreen = False
        elif seconds >= 4.5 and startingscreen == True:
             hud.main_menu("Go!", "purple", 0,0)
        elif seconds >= 3.5 and startingscreen == True:
            hud.main_menu("1...", "purple", 0,0)
        elif seconds >= 2.5 and startingscreen == True:
            hud.main_menu("2...", "purple", 0,0)
        elif startingscreen == True:
            hud.main_menu("3...", "purple", 0,0)
        

        #controls the spawning speed
        nowTime = pygame.time.get_ticks()
        if nowTime - oldTime >= spawn_rate and startingscreen != True:
            spawnenemies()
            oldTime = nowTime


        #adds interaction between powerups and player
        for power in pygame.sprite.spritecollide(player, powerupgroup, False):
            player.health += 5
            power.kill()

            heal = pygame.mixer.Sound('sounds/heal.wav')
            heal.play()
            heal.set_volume(.4)
            healchannel.play(heal)

        #detects if there an enemy has been hit
        for shot in playerprojgroup:
            for enemy in pygame.sprite.spritecollide(shot, enemiesgroup, False):
                explosionsgroup.add(Explosion(enemy.rect.x, enemy.rect.y, 1))
                enemy.health -= playerdamage
                shot.kill()


                heartchance = 90
                #adds 1 to score for killing a fighter
                if type(enemy) == Fighter and enemy.health <= 0:
                    playerscore += 1
                    genPowerup()
                if type(enemy) == Bomber and enemy.health <= 0:
                    playerscore += 1
                    genPowerup()
                if type(enemy) == Boss and enemy.health <= 0:
                    boss_spawned = False #resets boss_spawned so normal bots will spawn
                    powerupgroup.add(Health(enemy.x, enemy.y, asset_sheet.image_at((16,0,8,8), "black")))
                    playerscore += 1


                #makes explosion sound
                boom = pygame.mixer.Sound('sounds/explosion.wav')
                boom.set_volume(.6)
                boom.play()

        #take 7 damage if an enemy hits the player
        for enem in pygame.sprite.spritecollide(player, enemiesgroup, False):
            explosionsgroup.add(Explosion(player.x-4, player.y-8, 1.5))
            player.health -= 7
            enem.kill()

            boom = pygame.mixer.Sound('sounds/explosion.wav')
            boom.set_volume(.6)
            boom.play()

        #detects if player has been hit by enemy shot
        for shot in pygame.sprite.spritecollide(player, enemyprojgroup, True):
            explosionsgroup.add(Explosion(shot.x, shot.y+8, .5))
            player.health -= 1

            boom = pygame.mixer.Sound('sounds/playerexplosion.wav')
            boom.set_volume(1)
            boom.play()
        
        #detects if player gets hit by a boss
        for shot in pygame.sprite.spritecollide(player, bossprojgroup, True):
            explosionsgroup.add(Explosion(shot.x, shot.y+4, 1))
            player.health -= 3

            boom = pygame.mixer.Sound('sounds/playerexplosion.wav')
            boom.set_volume(1)
            boom.play()


        if player.health <= 0:
            gamestate = 3
         
        gamewindow.blit(player.image, player.rect)
        enemyprojgroup.draw(gamewindow)
        bossprojgroup.draw(gamewindow)
        playerprojgroup.draw(gamewindow)
        enemiesgroup.draw(gamewindow)
        explosionsgroup.draw(gamewindow)
        powerupgroup.draw(gamewindow)
        hud.score = playerscore
        hud.health = player.health
        hud.game_info()

        pygame.display.flip()
        player.update()
        playerprojgroup.update()
        enemiesgroup.update()
        enemyprojgroup.update()
        bossprojgroup.update()
        explosionsgroup.update()
        powerupgroup.update()
        dt = clock.tick(FPS)/1000

    if gamestate == 3: #game over screen
        bgmchannel.pause()
        if dead_var == 0:
            dead = pygame.mixer.Sound('sounds/death.mp3')
            dead.play()
            dead_var = 1
        if keys[pygame.K_p]:
            gamestate = 0

        gamewindow.fill('black')
        gamewindow.blit(titlebg, (0,0))
        hud.game_end("Game Over", (140,9,0))
        hud.place_text(("Score: " + str(playerscore)), "purple", 0, 50)
        hud.place_text("Press 'P' to Play Again!", "purple", 0, 120)

        pygame.display.flip()
