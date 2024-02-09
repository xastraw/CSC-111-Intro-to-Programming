import pygame
import random

class Powerup(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.vx = -4
        self.vy = 0
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.x = self.x
        self.rect.y = self.y
        
        if self.x <= 0 - self.rect.width:
            self.kill
    
class Health(Powerup):
    def __init__(self, x, y, image):
        super().__init__(x, y, pygame.transform.scale_by(image, 3))