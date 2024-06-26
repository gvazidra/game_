import pygame
from connectionAssets import *
class Carrot(pygame.sprite.Sprite):
    def __init__(self, x, y,  direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'flying_carrot.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = SPEED_CARROT
        self.movingRight = direction
        self.distance = 0

    def update(self):
        if self.movingRight == False:
             self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        self.distance += self.speed
        if self.rect.left < 0 or self.rect.right > 1920 or self.distance > 300:
            self.kill()

