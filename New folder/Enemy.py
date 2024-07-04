# -*- coding: utf-8 -*-

import pygame
import os
from connectionAssets import *


class Han(pygame.sprite.Sprite):
    def __init__(self, position, moveRight, borderL, borderR, number_level):
        pygame.sprite.Sprite.__init__(self)
        self.movingRight = moveRight
        self.enemyImage = pygame.image.load(os.path.join(img_folder, 'chicken.png')).convert()
        if self.movingRight:
            self.image = self.enemyImage
        elif not self.movingRight:
            self.image = pygame.transform.flip(self.enemyImage, True, False)
        self.rect = self.enemyImage.get_rect()
        self.rect.x, self.rect.y = position
        self.borderL = borderL
        self.borderR = borderR
        self.number_level = number_level

    def update(self):
        if self.movingRight:
            self.rect.x += SPEED_HAN
            self.image = self.enemyImage
        else:
            self.rect.x -= SPEED_HAN
            self.image = pygame.transform.flip(self.enemyImage, True, False)
        if self.rect.left < self.borderL:
            self.movingRight = True
        elif self.rect.right > self.borderR:
            self.movingRight = False

        collisions = pygame.sprite.spritecollide(self, bad_for_chicken, False)
        if collisions:
            channel.play(sound_han)
            self.kill()
            list_chicken_level[self.number_level].remove(self)

    def draw(self, displaySurface):
        displaySurface.blit(self.image, self.rect)
