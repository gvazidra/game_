from pygame import *
import os
import pygame
pygame.init()
import random

info = display.Info()
WIDTH = info.current_w
HEIGHT = info.current_h
SPEED_HAN = 2
PLAYER_SPEED = 4
SPEED_CARROT = 20
FPS = 25
start_x = 440
start_y = HEIGHT - 95
number_of_level = 0

#построение уровня
all_sprites = pygame.sprite.Group()
bad_for_chicken = pygame.sprite.Group()
list_platform_level = [[]]
list_ships_level = [[]]
list_water_level = [[]]
list_chicken_level = [[]]
blue_carrot_level = [[]]
simple_carrot_level = [[]]
strawberry_level = [[]]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

#прорисовка окна
virtual_surface = Surface((WIDTH, HEIGHT))

FULL_SCREEN_SIZE = (info.current_w, info.current_h)
CURRENT_SIZE = screen.get_size()
is_fullscreen = False
last_size = CURRENT_SIZE
#

virtual_surface.fill((40, 40, 150))
#file upload
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img_set = [pygame.image.load(os.path.join(img_folder, f"pig_{i}.png")).convert() for i in range(1, 5)]
background_img = pygame.image.load(os.path.join(img_folder, 'background.png')).convert()
platform_img = pygame.image.load(os.path.join(img_folder, 'platform1.png')).convert()

ships_img = pygame.image.load(os.path.join(img_folder, 'ships.png')).convert()
blue_carrot_img = pygame.image.load(os.path.join(img_folder, 'blue_carrot.png')).convert()
strawberry_img = pygame.image.load(os.path.join(img_folder, 'strawberry.png')).convert()
simple_carrot_img = pygame.image.load(os.path.join(img_folder, 'simple_carrot.png')).convert()
water_img  = pygame.image.load(os.path.join(img_folder, 'water.png')).convert()
#���� ��������

sound_floders = os.path.join(game_folder, 'sounds')
sound_walk_pig = pygame.mixer.Sound(sound_floders + '\\pig_walk_sound.ogg')
sound_walk_pig.set_volume(1)
sound_button = pygame.mixer.Sound(sound_floders + '\\button_sound.ogg')
channel0 = pygame.mixer.find_channel()
channel0.set_volume(0.9)

#sould of hru-hru
sound_pig = [pygame.mixer.Sound(sound_floders + f"\pig_sound_{i}.ogg") for i in range(1, 4)]
channel1 = pygame.mixer.find_channel()
channel1.set_volume(0.3)

pygame.mixer.init()

#image of button
button_image = pygame.image.load(os.path.join(img_folder, 'play_button.png')).convert()
button_hover_image = pygame.image.load(os.path.join(img_folder, 'play_button_triggered.png')).convert()

quit_button_img = pygame.image.load(os.path.join(img_folder, 'quit_button.png')).convert()
quit_hover_button_img = pygame.image.load(os.path.join(img_folder, 'quit_button_triggered.png')).convert()

op_button_img = pygame.image.load(os.path.join(img_folder, 'setting_button.png')).convert()
op_hover_button_img = pygame.image.load(os.path.join(img_folder, 'setting_button_triggered.png')).convert()

volume_button_img = pygame.image.load(os.path.join(img_folder, 'volume_button.png')).convert()
volume_hover_button_img = pygame.image.load(os.path.join(img_folder, 'volume_button_triggered.png')).convert()

easy_image = pygame.image.load(os.path.join(img_folder, 'easy.png')).convert()
easy_hover_image = pygame.image.load(os.path.join(img_folder, 'easy_triggered.png')).convert()

normal_image = pygame.image.load(os.path.join(img_folder, 'normal.png')).convert()
normal_hover_image = pygame.image.load(os.path.join(img_folder, 'normal_triggered.png')).convert()

hard_image = pygame.image.load(os.path.join(img_folder, 'hard.png')).convert()
hard_hover_image = pygame.image.load(os.path.join(img_folder, 'hard_triggered.png')).convert()

