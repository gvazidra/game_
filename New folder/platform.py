# -*- coding: utf-8 -*-
from Item import *
from Enemy import Han

class Platform(pygame.sprite.Sprite):
	def __init__(self, X, Y, img):
		super().__init__()
		self.image = img
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.center = (X, Y)

def create_levels():
	all_sprites.empty()
	list_platform_level.clear()
	list_ships_level.clear()
	list_water_level.clear()
	list_chicken_level.clear()
	blue_carrot_level.clear()
	simple_carrot_level.clear()
	strawberry_level.clear()
	list_back_level.clear()
	list_platform_level.append([])
	list_water_level.append([])
	list_ships_level.append([])
	list_back_level.append([])
	list_chicken_level.append([])
	blue_carrot_level.append([])
	simple_carrot_level.append([])
	strawberry_level.append([])
	distance = 0

	list_platform_level[0].append(Platform(90 + distance, height_surface - 43, platform_img))
	distance += 180
	list_platform_level[0].append(Platform(90 + distance, height_surface - 153, platform_img))
	distance += 180

	list_platform_level[0].append(Platform(90 + distance, height_surface - 43, platform_img))
	list_platform_level[0].append(Platform(90, height_surface - 363, platform_img))
	distance += 166
	for i in range(3):
		list_water_level[0].append(Platform(90 + distance, height_surface - 43, water_img))
		distance += 166
	list_platform_level[0].append(Platform(90 + distance, height_surface - 43, platform_img))
	distance += 180
	distance -= 10
	list_ships_level[0].append(Platform(90 + distance, height_surface - 43, ships_img))
	distance += 165
	distance += 8
	for i in range(5):
		list_platform_level[0].append(Platform(90 + distance, height_surface - 43, platform_img))
		distance += 180

	blue_carrot_level[0].append(Item(90, height_surface - 73, blue_carrot_img))

	simple_carrot_level[0].append(Item(90, height_surface - 413, simple_carrot_img))

	strawberry_level[0].append(Item(1700, height_surface - 100, strawberry_img))

	list_chicken_level[0].append(Han((1405, height_surface - 123), True, 1400, 1500, 0))
	list_chicken_level[0].append(Han((1505, height_surface - 123), True, 1500, 1700, 0))
	# второй уровень
	distance = 0
	list_platform_level.append([])
	list_water_level.append([])
	list_ships_level.append([])
	list_chicken_level.append([])
	list_back_level.append([])
	strawberry_level.append([])
	simple_carrot_level.append([])
	blue_carrot_level.append([])

	list_back_level[1].append(Platform(60, height_surface - 125, big_cust_img))
	list_back_level[1].append(Platform(100, height_surface - 125, big_cust_img))
	list_back_level[1].append(Platform(208, height_surface - 103, cust_img))
	list_back_level[1].append(Platform(269, height_surface - 102, cust_img))
	list_back_level[1].append(Platform(375, height_surface - 102, cust_img))
	list_back_level[1].append(Platform(435, height_surface - 82, cust_img))
	list_back_level[1].append(Platform(239, height_surface - 225, big_tree1_img))
	list_back_level[1].append(Platform(405, height_surface - 205, big_tree2_img))
	list_platform_level[1].append(Platform(239, height_surface - 380, invisible_platform_img))
	list_platform_level[1].append(Platform(405, height_surface - 360, invisible_platform_img))

	list_platform_level[1].append(Platform(83 + distance, height_surface - 50, forest_platform_img))
	list_platform_level[1].append(Platform(83 + distance, height_surface - 100, little_tree_img))

	for i in range(2):
		list_platform_level[1].append(Platform(249 + distance, height_surface - 50, forest_platform_img))
		distance += 166
	distance += 166
	list_water_level[1].append(Platform(581,height_surface - 45, water_img))
	list_water_level[1].append(Platform(913,height_surface - 45, water_img))
	list_water_level[1].append(Platform(1245,height_surface - 45, water_img))
	list_platform_level[1].append(Platform(249 + distance, height_surface - 50, forest_platform_img))
	distance += 332
	list_platform_level[1].append(Platform(249 + distance, height_surface - 50, forest_platform_img))
	distance += 332

	for i in range(2):
		list_platform_level[1].append(Platform(249 + distance, height_surface - 50, forest_platform_img))
		distance += 166
	for i in range(4):
		list_water_level[1].append(Platform(distance, height_surface - 45, water_img))
		distance += 166

	list_back_level[1].append(Platform(747, height_surface - 245, big_tree3_img))
	list_back_level[1].append(Platform(1079, height_surface - 245, big_tree3_img))
	list_back_level[1].append(Platform(720, height_surface - 95, cust_img))
	list_back_level[1].append(Platform(776, height_surface - 102, cust_img))
	list_back_level[1].append(Platform(1052, height_surface - 102, cust_img))
	list_back_level[1].append(Platform(1103, height_surface - 95, cust_img))
	list_platform_level[1].append(Platform(747, height_surface - 360, invisible_platform_img))
	list_platform_level[1].append(Platform(1079, height_surface - 360, invisible_platform_img))
	list_back_level[1].append(Platform(1550, height_surface - 245, big_tree2_img))
	list_back_level[1].append(Platform(1435, height_surface - 125, big_cust_img))
	list_back_level[1].append(Platform(1550, height_surface - 105, big_cust_img))

	strawberry_level[1].append(Item(1079, height_surface - 86, strawberry_img))
	list_chicken_level[1].append((Han((660, height_surface - 123), True, 664, 830, 1)))
	list_chicken_level[1].append((Han((825, height_surface - 117), True, 664, 830, 1)))
	list_chicken_level[1].append((Han((1152, height_surface - 123), True, 996, 1162,1)))
	list_chicken_level[1].append((Han((986, height_surface - 113), True, 996, 1162,1)))
	list_chicken_level[1].append((Han((1056, height_surface - 113), True, 996, 1100, 1)))
	simple_carrot_level[1].append(Item(1411, height_surface - 83, simple_carrot_img))


	#третий уровень
	distance = 80
	list_platform_level.append([])
	list_water_level.append([])
	list_ships_level.append([])
	list_chicken_level.append([])
	list_back_level.append([])
	strawberry_level.append([])
	simple_carrot_level.append([])
	blue_carrot_level.append([])
	for i in range(3):
		list_platform_level[2].append(Platform(distance, height_surface - 50, dessert_platform_img))
		distance += 160
	distance += 3
	for i in range(3):
		list_water_level[2].append(Platform(distance, height_surface - 45, water_img))
		distance += 166
	distance -= 6
	for i in range(5):
		list_platform_level[2].append(Platform(distance, height_surface - 50, dessert_platform_img))
		distance += 160
	for i in range(3):
		list_water_level[2].append(Platform(distance, height_surface - 45, water_img))
		distance += 166
	list_ships_level[2].append(Platform(60, height_surface - 85, cactus_img))
	list_ships_level[2].append(Platform(160, height_surface - 60, cactus_img))
	list_ships_level[2].append(Platform(240, height_surface - 95, cactus_img))
	list_ships_level[2].append(Platform(1040, height_surface - 95, cactus_img))
	list_ships_level[2].append(Platform(1300, height_surface - 65, cactus_img))
	list_ships_level[2].append(Platform(1650, height_surface - 65, cactus_img))


	list_back_level[2].append(Platform(80, height_surface - 235, palma_img))
	list_back_level[2].append(Platform(320, height_surface - 135, palma_img))
	list_platform_level[2].append(Platform(80, height_surface - 335, invisible_platform_img))
	list_platform_level[2].append(Platform(310, height_surface - 245, invisible_platform_img))
	list_platform_level[2].append(Platform(1040, height_surface - 315, invisible_platform_img))
	list_platform_level[2].append(Platform(1400, height_surface - 235, invisible_platform_img))
	list_back_level[2].append(Platform(1040, height_surface - 235, palma_img))
	list_back_level[2].append(Platform(1400, height_surface - 135, palma_img))
	list_back_level[2].append(Platform(1710, height_surface - 235, palma_img))
	blue_carrot_level[2].append(Item(80, height_surface - 355, blue_carrot_img))
	strawberry_level[2].append(Item(1400, height_surface - 83, strawberry_img))

	#заглушка
	distance = 80
	list_platform_level.append([])
	list_water_level.append([])
	list_ships_level.append([])
	list_chicken_level.append([])
	list_back_level.append([])
	strawberry_level.append([])
	simple_carrot_level.append([])
	blue_carrot_level.append([])



def create_level(number_of_level):
	all_sprites.empty()
	platform_number_of_level = number_of_level
	if  number_of_level <= 2:

		for i in range(list_water_level[number_of_level].__len__()):
			all_sprites.add(list_water_level[number_of_level][i])
		for i in range(list_back_level[number_of_level].__len__()):
			all_sprites.add(list_back_level[number_of_level][i])
		for i in range(list_platform_level[number_of_level].__len__()):
			all_sprites.add(list_platform_level[number_of_level][i])

		for i in range(list_ships_level[number_of_level].__len__()):
			all_sprites.add(list_ships_level[number_of_level][i])
		all_sprites.add(blue_carrot_level[number_of_level])
		all_sprites.add(simple_carrot_level[number_of_level])
		all_sprites.add(strawberry_level[number_of_level])
		for i in range(list_chicken_level[number_of_level].__len__()):
			all_sprites.add(list_chicken_level[number_of_level][i])


