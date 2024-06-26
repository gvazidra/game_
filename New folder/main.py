import pygame
import random
import os 

WIDTH = 500
HEIGHT = 480
FPS = 30

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((1920, 1080))
pygame.mixer.init()

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join(img_folder, 'pig.png')).convert()
background_img = pygame.image.load(os.path.join(img_folder, 'background.png')).convert()

sound_floders = os.path.join(game_folder, 'sounds')
sound_pig = pygame.mixer.Sound(sound_floders + '\\pig_sound.ogg')
sound_pig.set_volume(1)
channel = pygame.mixer.find_channel()

channel.play(sound_pig)
channel.set_volume(0.9)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.key_pressed = False
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (960, 540)
        self.r_speed = 4
        self.l_speed = 4
        self.flip = 0
        self.jumpCount = 10
        self.isJump = 10
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if not channel.get_busy():
                channel.play(sound_pig)
            if self.flip == 0:
                self.flip = 1
                self.image = pygame.transform.flip(self.image, True, False)
            self.rect.x += self.r_speed
            self.l_speed = 4
            if self.r_speed < 10:
                self.r_speed += 1
                
        elif keys[pygame.K_LEFT]:
            if not channel.get_busy():
                channel.play(sound_pig)
            if self.flip == 1:
                self.flip = 0
                self.image = pygame.transform.flip(self.image, True, False)
            self.r_speed = 4
            self.rect.x -= self.l_speed
            if self.l_speed < 10:
                self.l_speed += 1
        
        else:
            channel.stop()
                
        if keys[pygame.K_SPACE]:
            self.isJump = True

        if self.isJump is True:

            if self.jumpCount >= -10:

                if self.jumpCount < 0:
                    self.rect.y += (self.jumpCount ** 2) // 2
                else:
                    self.rect.y -= (self.jumpCount ** 2) // 2

                self.jumpCount -= 1

            else:
                self.isJump = False
                self.jumpCount = 10
            
pygame.init()
pygame.mixer.init() 
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            k = pygame.key.get_pressed()
            if k[pygame.K_ESCAPE]:
                running = False
    all_sprites.update()
    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()