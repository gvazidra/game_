import pygame
import os 
import random

SPEED_HAN = 2
SPEED_CARROT = 10

WIDTH = 500
HEIGHT = 480
FPS = 25

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.mixer.init()

screen = pygame.display.set_mode((1920, 1080))

#file upload
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img_set = [pygame.image.load(os.path.join(img_folder, f"pig_{i}.png")).convert() for i in range(1, 5)]
background_img = pygame.image.load(os.path.join(img_folder, 'background.png')).convert()
platform_img = pygame.image.load(os.path.join(img_folder, 'platform1.png')).convert()
#sound of walk
sound_floders = os.path.join(game_folder, 'sounds')
sound_walk_pig = pygame.mixer.Sound(sound_floders + '\\pig_walk_sound.ogg')
sound_walk_pig.set_volume(1)
channel0 = pygame.mixer.find_channel()
channel0.set_volume(0.9)

#sould of hru-hru
sound_pig = [pygame.mixer.Sound(sound_floders + f"\\pig_sound_{i}.ogg") for i in range(1, 4)]
channel1 = pygame.mixer.find_channel()
channel1.set_volume(0.3)

pygame.mixer.init()

