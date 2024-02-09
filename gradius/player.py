import pygame
from projectiles import *

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.rect = image.get_rect()
        self.image = pygame.transform.scale2x(pygame.transform.rotate(image,90))
        self.rect.x = self.x
        self.rect.y = self.y
        self.firing = False
        self.firingdelay = 200
        self.health = 20

    def fire(self, image, group):
        if self.firing:
            pass
        else:
            self.firingtime = pygame.time.get_ticks()
            self.firing = True
            image = pygame.transform.scale2x(pygame.transform.rotate(image,-90))
            proj = PlayerProjectile(self.x+32, self.y+8, 10, 0, image)
            group.add(proj)

            #adds the player shoot sound here to prevent sounds overlapping
            self.channel = pygame.mixer.Channel(1)
            self.shoot = pygame.mixer.Sound('sounds/laserShoot.wav')
            self.shoot.set_volume(.4)
            self.channel.play(self.shoot)

            

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        if self.firing and pygame.time.get_ticks() - self.firingtime > self.firingdelay:
            self.firing = False
        
        #keeps player on screen
        if self.y <= 0:
            self.y = 0
            self.rect.y = 0
        if self.y >= 448:
            self.y = 448
            self.rect.y = 448

