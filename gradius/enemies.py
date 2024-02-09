import pygame
import random
from projectiles import *

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, image, bullet, group):
        super().__init__()
        self.x = x
        self.y = y
        self.bullet = bullet
        self.bulletspeed = 5
        self.image = image
        self.group = group
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.vx = -random.randint(140, 300)/100
        self.vy = 0
        self.firing = False
        self.firingtime = 0
        self.firingdelay = 0#random.randint(700, 2000)
        self.health = 1
        

    def fire(self, group):       
        group.add(EnemyProjectile(self.x, self.y, self.vx - self.bulletspeed, 0, self.bullet))
    
        
    def update(self):
        self.x += self.vx
        self.y += self.vy 
        self.rect.x = self.x
        self.rect.y = self.y

        

        if pygame.time.get_ticks() - self.firingtime > self.firingdelay:
            self.firing = False
        if not self.firing:
            self.fire(self.group)

            self.channel = pygame.mixer.Channel(2)
            self.shoot = pygame.mixer.Sound('sounds/enemyshoot.wav')
            self.shoot.set_volume(.3)
            self.channel.play(self.shoot)

            self.firing = True
            self.firingtime = pygame.time.get_ticks()

        if self.health <= 0:
            self.kill()
        if self.rect.x <= 0 - self.rect.width:
            self.kill()
        
        
        


class Fighter(Enemy):
    def __init__(self, x, y, image, bullet, group):
        super().__init__(x, y, pygame.transform.scale_by(pygame.transform.rotate(image,-90),4), bullet, group)
        self.health = 1
        self.firingdelay = random.randint(1500, 2000)
        self.bulletspeed = 4
        

class Bomber(Enemy): 
    def __init__(self, x, y, image, bullet, group):
        super().__init__(x,y, pygame.transform.scale_by(pygame.transform.rotate(image, 90), 5), bullet, group)
        self.health = 3
        self.firingdelay = 1200
        self.bulletspeed = 8
    

class Boss(Enemy):
    def __init__(self, x, y, image, bullet, group):
        super().__init__(x, y, pygame.transform.scale_by(pygame.transform.rotate(image, -90), 4), bullet, group)
        self.health = 40
        self.firingdelay = 200
        self.bulletspeed = 10
        self.vy = 5
        

    def update(self):
        
        acceleration = random.randint(-150, 150)/100
        
        if acceleration < -0.1 or acceleration > 0.1:
            acceleration = acceleration *2

        self.vy += acceleration
        
        if self.x <= 450:
            self.vx = 0 

        #resets the velocity and acceleration if acceleration gets too high
        if self.vy >= 10:
            self.vy = 5
        if self.vy <= -10:
            self.vy = -5


        if self.y <= 0:
            self.y = 0 
            self.vy = self.vy * -1

        if self.y >= 480 - self.rect.height:
            self.y = 480 - self.rect.height
            self.vy = self.vy * -1
            
        


        return super().update()