import pygame
import os 
import random

WIDTH = 1920
HEIGHT = 1080
SPEED_HAN = 2
SPEED_CARROT = 10

FPS = 25
start_x = 960
start_y = 540
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((40, 40, 150))
#file upload
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img_set = [pygame.image.load(os.path.join(img_folder, f"pig_{i}.png")).convert() for i in range(1, 5)]
background_img = pygame.image.load(os.path.join(img_folder, 'background.png')).convert()
platform_img = pygame.image.load(os.path.join(img_folder, 'platform1.png')).convert()

ships_img = pygame.image.load(os.path.join(img_folder, 'ships.png')).convert()
blue_carrot_img = pygame.image.load(os.path.join(img_folder, 'blue_carrot.png')).convert()
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
button_image = pygame.image.load(r"C:\Users\dzhar\Downloads\Frame 3.png")
button_hover_image = pygame.image.load(r"C:\Users\dzhar\Downloads\Frame 4.png")

quit_button_img = pygame.image.load(r"C:\Users\dzhar\Downloads\Frame 2.png")
quit_hover_button_img = pygame.image.load(r"C:\Users\dzhar\Downloads\Frame 5.png")

op_button_img = pygame.image.load(r"C:\Users\dzhar\Downloads\Frame 1.png")
op_hover_button_img = pygame.image.load(r"C:\Users\dzhar\Downloads\Frame 7.png")

new_button_img = pygame.image.load(r"C:\Users\dzhar\Downloads\volume.png")
new_hover_button_img = pygame.image.load(r"C:\Users\dzhar\Downloads\Frame 8.png")
