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
status = 'Main_menu'
all_sprites = pygame.sprite.Group()
bad_for_chicken = pygame.sprite.Group()
list_platform_level = [[]]
list_ships_level = [[]]
list_water_level = [[]]
list_chicken_level = [[]]
list_back_level = [[]]
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
player_img_set_1 = [pygame.image.load(os.path.join(img_folder + "\\skins", f"pig_{i}.png")).convert() for i in range(1, 5)]
player_img_set_2 = [pygame.image.load(os.path.join(img_folder + "\\skins", f"pig_{i}.png")).convert() for i in range(5, 9)]
background_img = pygame.image.load(os.path.join(img_folder, 'background.png')).convert()
platform_img = pygame.image.load(os.path.join(img_folder, 'platform1.png')).convert()

for image in player_img_set_1:
    image.set_colorkey(BLACK)
    
for image in player_img_set_2:
    image.set_colorkey(BLACK)

ships_img = pygame.image.load(os.path.join(img_folder, 'ships.png')).convert()
blue_carrot_img = pygame.image.load(os.path.join(img_folder, 'blue_carrot.png')).convert()
strawberry_img = pygame.image.load(os.path.join(img_folder, 'strawberry.png')).convert()
simple_carrot_img = pygame.image.load(os.path.join(img_folder, 'simple_carrot.png')).convert()
water_img  = pygame.image.load(os.path.join(img_folder, 'water.png')).convert()
forest_platform_img  = pygame.image.load(os.path.join(img_folder, 'forest_platform.png')).convert()
invisible_platform_img  = pygame.image.load(os.path.join(img_folder, 'invisible_platform.png')).convert()
cust_img  = pygame.image.load(os.path.join(img_folder, 'cust.png')).convert()
big_tree1_img  = pygame.image.load(os.path.join(img_folder, 'big_tree1.png')).convert()
big_tree2_img  = pygame.image.load(os.path.join(img_folder, 'big_tree2.png')).convert()
big_tree3_img  = pygame.image.load(os.path.join(img_folder, 'big_tree3.png')).convert()
little_tree_img  = pygame.image.load(os.path.join(img_folder, 'little_tree.png')).convert()
big_cust_img  = pygame.image.load(os.path.join(img_folder, 'big_cust.png')).convert()




sound_floders = os.path.join(game_folder, 'sounds')
sound_walk_pig = pygame.mixer.Sound(sound_floders + '\\pig_walk_sound.ogg')
sound_walk_pig.set_volume(1)
sound_button = pygame.mixer.Sound(sound_floders + '\\button_sound.ogg')
channel = pygame.mixer.find_channel()

#sould of hru-hru
sound_pig = [pygame.mixer.Sound(sound_floders + f"\pig_sound_{i}.ogg") for i in range(1, 4)]
channel = pygame.mixer.find_channel()
channel.set_volume(4 / 9)

#pygame.mixer.init()

#image of button
button_image = pygame.image.load(os.path.join(img_folder, 'play_button.png')).convert()
button_hover_image = pygame.image.load(os.path.join(img_folder, 'play_button_triggered.png')).convert()

quit_button_img = pygame.image.load(os.path.join(img_folder, 'quit_button.png')).convert()
quit_hover_button_img = pygame.image.load(os.path.join(img_folder, 'quit_button_triggered.png')).convert()

op_button_img = pygame.image.load(os.path.join(img_folder, 'setting_button.png')).convert()
op_hover_button_img = pygame.image.load(os.path.join(img_folder, 'setting_button_triggered.png')).convert()

volume_button_img = pygame.image.load(os.path.join(img_folder, 'volume_button.png')).convert()
volume_hover_button_img = pygame.image.load(os.path.join(img_folder, 'volume_button_triggered.png')).convert()

graph_button_img = pygame.image.load(os.path.join(img_folder, 'graph_button.png')).convert()
graph_hover_button_img = pygame.image.load(os.path.join(img_folder, 'graph_button_triggered.png')).convert()

easy_image = pygame.image.load(os.path.join(img_folder, 'easy.png')).convert()
easy_hover_image = pygame.image.load(os.path.join(img_folder, 'easy_triggered.png')).convert()

normal_image = pygame.image.load(os.path.join(img_folder, 'normal.png')).convert()
normal_hover_image = pygame.image.load(os.path.join(img_folder, 'normal_triggered.png')).convert()

hard_image = pygame.image.load(os.path.join(img_folder, 'hard.png')).convert()
hard_hover_image = pygame.image.load(os.path.join(img_folder, 'hard_triggered.png')).convert()

heart_image = pygame.image.load(os.path.join(img_folder, 'heart.png')).convert()
heart_image.set_colorkey(BLACK)

def draw_hearts(life_amount):
    x = screen.get_width()/2 - life_amount * (10 + heart_image.get_width()) / 2
    y = 40
    for _ in range(life_amount):
        virtual_surface.blit(heart_image, (x, y))
        x +=  heart_image.get_width() + 10
        
        
volume_mixer = [pygame.image.load(os.path.join(img_folder + '\\volume_bar', f"volume_{i}.png")).convert() for i in range(0, 10)]

click_image = pygame.image.load(os.path.join(img_folder, 'click.png')).convert()

pygame.mixer.music.load(sound_floders + '\\game_music.ogg')
pygame.mixer.music.set_volume(4 / 9)
pygame.mixer.music.play(-1)     