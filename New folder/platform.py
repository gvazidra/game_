from Item import *
from Enemy import Han
class Platform(pygame.sprite.Sprite):
	def __init__(self, X, Y):
		super().__init__()
		self.image = platform_img
		self.image.set_colorkey(BLACK)
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


#первый уровень
list_platform_level = [[]]
list_ships_level = [[]]
list_water_level = [[]]
list_chicken_level = [[]]
distance = 0

list_platform_level[0].append(Platform(90 + distance, HEIGHT - 43))
distance += 180

list_platform_level[0].append(Platform(90 + distance, HEIGHT - 153))
distance += 180

list_platform_level[0].append(Platform(90 + distance, HEIGHT - 43))
distance += 180
distance += 180

for i in range(2):
	#list_platform_level[0].append(Water(240 + distance, 585))
	list_water_level[0].append(Water(90 + distance, HEIGHT - 43))
	distance += 180

list_platform_level[0].append(Platform(90 + distance, HEIGHT - 43))
distance += 180
distance -= 10

#list_platform_level[0].append(Ships(240 + distance, 585))
list_ships_level[0].append(Ships(90 + distance,  HEIGHT - 43))
distance += 165
distance += 8

list_platform_level[0].append(Platform(90 + distance, HEIGHT - 43))
distance += 180

list_platform_level[0].append(Platform(90 + distance, HEIGHT - 43))
distance += 180

blue_carrot_level = []
blue_carrot_level.append(Blue_carrot(90, HEIGHT - 73))


list_chicken_level[0].append(Han((1400, HEIGHT - 93), True, 1400, 1500))



#первый уровень