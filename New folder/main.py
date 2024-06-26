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
player_img_set = [pygame.image.load(os.path.join(img_folder, f"pig_{i}.png")).convert() for i in range(1, 4)]
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
        self.image = player_img_set[1]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (960, 540)
        self.r_speed = 4
        self.l_speed = 4
        self.flip = 0
        self.jumpCount = 10
        self.isJump = 10
        self.i = 0
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.image = pygame.transform.flip(player_img_set[self.i], True, False)
            self.image.set_colorkey(BLACK)
            self.i += 1
            if self.i == 3:
                self.i = 0
            if not channel.get_busy():
                channel.play(sound_pig)
            self.rect.x += self.r_speed
            self.l_speed = 4
            if self.r_speed < 10:
                self.r_speed += 1
                
        elif keys[pygame.K_LEFT]:
            self.image = player_img_set[self.i]
            self.i += 1
            if self.i == 3:
                self.i = 0
            self.image.set_colorkey(BLACK)
            if not channel.get_busy():
                channel.play(sound_pig)
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