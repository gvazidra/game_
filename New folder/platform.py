from pig import *
import pygame
class Platform(pygame.sprite.Sprite):
	def __init__(self, X, Y):
		super().__init__()
		self.image = platform_img
		self.rect = self.image.get_rect()
		self.rect.center = (X, Y)
list_platform_level1 = []
distance = 0
for i in range(9):
		list_platform_level1.append(Platform(240 + distance, 585))
		distance += 180