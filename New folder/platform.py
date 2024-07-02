# -*- coding: utf-8 -*-
from Item import *
from Enemy import Han
platform_number_of_level = 0
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

	list_platform_level[0].append(Platform(90 + distance, HEIGHT - 43, platform_img))
	distance += 180
	list_platform_level[0].append(Platform(90 + distance, HEIGHT - 153, platform_img))
	distance += 180

	list_platform_level[0].append(Platform(90 + distance, HEIGHT - 43, platform_img))
	list_platform_level[0].append(Platform(90 + distance, HEIGHT - 383, platform_img))
	distance += 166
	for i in range(3):
		list_water_level[0].append(Platform(90 + distance, HEIGHT - 43, water_img))
		distance += 166
	list_platform_level[0].append(Platform(90 + distance, HEIGHT - 43, platform_img))
	distance += 180
	distance -= 10
	list_ships_level[0].append(Platform(90 + distance, HEIGHT - 43, ships_img))
	distance += 165
	distance += 8

	list_platform_level[0].append(Platform(90 + distance, HEIGHT - 43, platform_img))
	distance += 180

	list_platform_level[0].append(Platform(90 + distance, HEIGHT - 43, platform_img))
	distance += 180

	blue_carrot_level[0].append(Item(90, HEIGHT - 73, blue_carrot_img))

	simple_carrot_level[0].append(Item(450, HEIGHT - 413, simple_carrot_img))

	strawberry_level[0].append(Item(1500, HEIGHT - 100, strawberry_img))

	list_chicken_level[0].append(Han((1400, HEIGHT - 113), True, 1400, 1500, 0))

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

	list_back_level[1].append(Platform(60, HEIGHT - 125, big_cust_img))
	list_back_level[1].append(Platform(100, HEIGHT - 125, big_cust_img))
	list_back_level[1].append(Platform(208, HEIGHT - 103, cust_img))
	list_back_level[1].append(Platform(269, HEIGHT - 102, cust_img))
	list_back_level[1].append(Platform(375, HEIGHT - 102, cust_img))
	list_back_level[1].append(Platform(435, HEIGHT - 82, cust_img))
	list_back_level[1].append(Platform(239, HEIGHT - 225, big_tree1_img))
	list_back_level[1].append(Platform(405, HEIGHT - 205, big_tree2_img))
	list_platform_level[1].append(Platform(239, HEIGHT - 380, invisible_platform_img))
	list_platform_level[1].append(Platform(405, HEIGHT - 360, invisible_platform_img))

	list_platform_level[1].append(Platform(83 + distance, HEIGHT - 50, forest_platform_img))
	list_platform_level[1].append(Platform(83 + distance, HEIGHT - 100, little_tree_img))

	for i in range(2):
		list_platform_level[1].append(Platform(249 + distance, HEIGHT - 50, forest_platform_img))
		distance += 166
	distance += 166

	list_water_level[1].append(Platform(581,HEIGHT - 45, water_img))
	list_water_level[1].append(Platform(913,HEIGHT - 45, water_img))
	list_water_level[1].append(Platform(1245,HEIGHT - 45, water_img))

	list_platform_level[1].append(Platform(249 + distance, HEIGHT - 50, forest_platform_img))
	distance += 166
	distance += 166
	list_platform_level[1].append(Platform(249 + distance, HEIGHT - 50, forest_platform_img))
	distance += 166
	distance += 166
	list_platform_level[1].append(Platform(249 + distance, HEIGHT - 50, forest_platform_img))
	distance += 166
	list_platform_level[1].append(Platform(249 + distance, HEIGHT - 50, forest_platform_img))

	list_back_level[1].append(Platform(747, HEIGHT - 245, big_tree3_img))
	list_back_level[1].append(Platform(1079, HEIGHT - 245, big_tree3_img))
	list_back_level[1].append(Platform(720, HEIGHT - 95, cust_img))
	list_back_level[1].append(Platform(776, HEIGHT - 102, cust_img))
	list_back_level[1].append(Platform(1052, HEIGHT - 102, cust_img))
	list_back_level[1].append(Platform(1103, HEIGHT - 95, cust_img))
	list_platform_level[1].append(Platform(747, HEIGHT - 360, invisible_platform_img))
	list_platform_level[1].append(Platform(1079, HEIGHT - 360, invisible_platform_img))
	list_back_level[1].append(Platform(1550, HEIGHT - 245, big_tree2_img))
	list_back_level[1].append(Platform(1435, HEIGHT - 125, big_cust_img))
	list_back_level[1].append(Platform(1550, HEIGHT - 105, big_cust_img))

	strawberry_level[1].append(Item(1079, HEIGHT - 73, strawberry_img))
	list_chicken_level[1].append((Han((664, HEIGHT - 113), True, 664, 830, 1)))
	list_chicken_level[1].append((Han((830, HEIGHT - 100), True, 664, 830, 1)))
	list_chicken_level[1].append((Han((1162, HEIGHT - 113), True, 996, 1162,1)))
	list_chicken_level[1].append((Han((996, HEIGHT - 93), True, 996, 1162,1)))
	list_chicken_level[1].append((Han((1056, HEIGHT - 93), True, 996, 1100, 1)))
	simple_carrot_level[1].append(Item(1411, HEIGHT - 83, simple_carrot_img))


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
		list_platform_level[2].append(Platform(distance, HEIGHT - 50, dessert_platform_img))
		distance += 160
	distance += 3
	for i in range(3):
		list_water_level[2].append(Platform(distance, HEIGHT - 45, water_img))
		distance += 166
	distance -= 6
	for i in range(4):
		list_platform_level[2].append(Platform(distance, HEIGHT - 50, dessert_platform_img))
		distance += 160
	list_ships_level[2].append(Platform(60, HEIGHT - 85, cactus_img))
	list_ships_level[2].append(Platform(160, HEIGHT - 60, cactus_img))
	list_ships_level[2].append(Platform(240, HEIGHT - 95, cactus_img))
	list_ships_level[2].append(Platform(1040, HEIGHT - 95, cactus_img))
	list_ships_level[2].append(Platform(1300, HEIGHT - 65, cactus_img))


	list_back_level[2].append(Platform(80, HEIGHT - 235, palma_img))
	list_back_level[2].append(Platform(320, HEIGHT - 135, palma_img))
	list_platform_level[2].append(Platform(80, HEIGHT - 335, invisible_platform_img))
	list_platform_level[2].append(Platform(310, HEIGHT - 245, invisible_platform_img))
	list_platform_level[2].append(Platform(1040, HEIGHT - 335, invisible_platform_img))
	list_platform_level[2].append(Platform(1400, HEIGHT - 235, invisible_platform_img))
	list_back_level[2].append(Platform(1040, HEIGHT - 235, palma_img))
	list_back_level[2].append(Platform(1400, HEIGHT - 135, palma_img))
	blue_carrot_level[2].append(Item(80, HEIGHT - 355, blue_carrot_img))
	strawberry_level[2].append(Item(1400, HEIGHT - 73, strawberry_img))

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


