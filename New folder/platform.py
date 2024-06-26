from connectionAssets import *
import pygame
class Platform(pygame.sprite.Sprite):
	def __init__(self, X, Y):
		super().__init__()
		self.image = platform_img
		self.rect = self.image.get_rect()
		self.rect.center = (X, Y)
class Ships(pygame.sprite.Sprite):
	def __init__(self, X, Y):
		super().__init__()
		self.image = ships_img
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.center = (X, Y)
class Water(pygame.sprite.Sprite):
	def __init__(self, X, Y):
		super().__init__()
		self.image = water_img
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.center = (X, Y)

list_platform_level1 = []
list_ships_level1 = []
list_water_level1 = []
distance = 0

for i in range(6):
		list_platform_level1.append(Platform(240 + distance, 585))
		distance += 180
for i in range(1):
				list_platform_level1.append(Water(240 + distance, 585))
				list_water_level1.append(Water(240 + distance, 585))
				distance += 180
distance -= 10
for i in range(2):
			list_platform_level1.append(Ships(240 + distance, 585))
			list_ships_level1.append(Ships(240 + distance,  585))
			distance += 165
