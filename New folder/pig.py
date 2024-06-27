import pygame

from carrot import Carrot
from connectionAssets import *
import random
#from Enemy import Han

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.key_pressed = False
        self.image = player_img_set[1]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (960, 540)
        self.speed = 4
        self.jumpCount = 10
        self.isJump = False
        self.i = 0
        self.jumpSound = 0
        self.runningRight = 0

    
    def move(self, k):
        #print((k+1) // 2)
        self.image = pygame.transform.flip(player_img_set[self.i], (k+1) // 2, False)
        self.image.set_colorkey(BLACK)
        self.i += 1
        if self.i == 3:
            self.i = 0
        if not channel0.get_busy():
            channel0.play(sound_walk_pig)
        self.rect.x += self.speed * k
        if self.speed < 15:
            self.speed += 1
    
    def jump(self):
        if self.jumpSound == 0:
                channel0.stop()
                channel1.play(sound_pig[random.randint(0, 2)])
                self.jumpSound = 1
        self.isJump = True

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move(-1)
            self.runningRight = 0
        elif keys[pygame.K_RIGHT]:
            self.move(1)
            self.runningRight = 1
        else:
            if not self.isJump:
                channel0.stop()
                
        if keys[pygame.K_SPACE]:
            self.jump()

        if self.isJump:
            if self.jumpCount >= -10:

                if self.jumpCount < 0:
                    self.rect.y += (self.jumpCount ** 2) // 2
                else:
                    self.rect.y -= (self.jumpCount ** 2) // 2

                self.jumpCount -= 1

            else:
                channel1.stop()
                self.jumpSound = 0
                self.isJump = False
                self.jumpCount = 10

    def shoot_carrot(self):

        direction = 1 if self.runningRight else -1
        carrot = Carrot(self.rect.centerx, self.rect.top + 50, direction)
        return carrot