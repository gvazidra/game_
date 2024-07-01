import pygame
import os
from connectionAssets import *

class Han(pygame.sprite.Sprite):
    def __init__(self, position, moveRight, borderL, borderR, number_level):
        pygame.sprite.Sprite.__init__(self)
        self.movingRight = moveRight
        enemyImage = pygame.image.load(os.path.join(img_folder, 'chicken.png')).convert()
        if self.movingRight == True:
            self.enemyImage = enemyImage
        elif self.movingRight == False:
            self.enemyImage = pygame.transform.flip(enemyImage, True, False)
        self.image = self.enemyImage
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.borderL = borderL
        self.borderR = borderR
        self.number_level = number_level


    def update(self):
        if self.movingRight:
            self.rect.x += SPEED_HAN
        else:
            self.rect.x -= SPEED_HAN

        if self.rect.left < self.borderL:
            self.movingRight = True
            self.enemyImage = pygame.transform.flip(self.enemyImage, True, False)
            self.image = self.enemyImage
        elif self.rect.right > self.borderR:
            self.movingRight = False
            self.enemyImage = pygame.transform.flip(self.enemyImage, True, False)
            self.image = self.enemyImage

        collisions = pygame.sprite.spritecollide(self, bad_for_chicken, False)
        if collisions:
            channel.play(sound_han)
            self.kill()
            list_chicken_level[self.number_level].remove(self)
            pygame.time.delay(500)


    def draw(self, displaySurface):
        displaySurface.blit(self.image, self.rect)




