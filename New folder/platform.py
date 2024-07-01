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
	list_platform_level.append([])
	list_water_level.append([])
	list_ships_level.append([])
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
	distance += 180
	distance += 180

	for i in range(2):
		# list_platform_level[0].append(Water(240 + distance, 585))
		list_water_level[0].append(Platform(90 + distance, HEIGHT - 43, water_img))
		distance += 178

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

	strawberry_level[0].append(Item(900, HEIGHT - 413, strawberry_img))

	list_chicken_level[0].append(Han((1400, HEIGHT - 113), True, 1400, 1500))

	# второй уровень
	distance = 0
	list_platform_level.append([])
	list_water_level.append([])
	list_ships_level.append([])
	list_chicken_level.append([])
	strawberry_level.append([])
	simple_carrot_level.append([])
	blue_carrot_level.append([])
	list_platform_level[1].append(Platform(90 + distance, HEIGHT - 43, platform_img))

	distance += 180

	list_platform_level[1].append(Platform(90 + distance, HEIGHT - 153, platform_img))
	distance += 180

	list_platform_level[1].append(Platform(90 + distance, HEIGHT - 43, platform_img))
	list_platform_level[1].append(Platform(90 + distance, HEIGHT - 383, platform_img))
	distance += 180
	distance += 180

	for i in range(2):
		# list_platform_level[0].append(Water(240 + distance, 585))
		list_water_level[1].append(Platform(90 + distance, HEIGHT - 43, water_img))
		distance += 178

	list_platform_level[1].append(Platform(90 + distance, HEIGHT - 43, platform_img))
	distance += 180
	distance -= 10

	list_ships_level[1].append(Platform(90 + distance, HEIGHT - 43, ships_img))
	distance += 165
	distance += 8

	list_platform_level[1].append(Platform(90 + distance, HEIGHT - 43, platform_img))
	distance += 180

def create_level():
	all_sprites.empty()
	for i in range(list_platform_level[number_of_level].__len__()):
		all_sprites.add(list_platform_level[number_of_level][i])
	for i in range(list_water_level[number_of_level].__len__()):
		all_sprites.add(list_water_level[number_of_level][i])
	for i in range(list_ships_level[number_of_level].__len__()):
		all_sprites.add(list_ships_level[number_of_level][i])
	for i in range(list_chicken_level[number_of_level].__len__()):
		all_sprites.add(list_chicken_level[number_of_level][i])
	all_sprites.add(blue_carrot_level[number_of_level])
	all_sprites.add(simple_carrot_level[number_of_level])
	all_sprites.add(strawberry_level[number_of_level])




