# -*- coding: utf-8 -*-

from platform import *
from carrot import *
from connectionAssets import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.life_amount = 3
        self.number_of_level = 0#НАДО ПОМЕНЯТЬ НА 0
        self.water_ability = 1
        self.shoot_ability = 0
        pygame.sprite.Sprite.__init__(self)
        self.key_pressed = False
        self.images = player_img_set_1
        self.image = self.images[1]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (start_x, start_y)
        self.speed = 4
        self.jumpCount = 10
        self.isJump = 0
        self.i = 0
        self.jumpSound = 0
        self.dir = -1
        self.speed_x = 0
        self.speed_y = 0
        self.on_side = 0
        self.ready_to_jump = True
    
    def skins_update(self, skins):
        self.images = skins
        self.image = self.images[self.i]
        self.image.set_colorkey(BLACK)
        self.update()
    
    def move(self, k):
        self.image = pygame.transform.flip(self.images[self.i], (k+1) // 2, False)
        self.image.set_colorkey(BLACK)
        self.i += 1
        if self.i == 3:
            self.i = 0
        if not channel.get_busy() and channel.get_sound() != sound_button:
            channel.play(sound_walk_pig)
        self.rect.x += self.speed * k
        if self.speed < 15:
            self.speed += 1
    
    def jump(self):
        if self.jumpSound == 0:
                channel.stop()
                channel.play(sound_pig[random.randint(0, 2)])
                self.jumpSound = 1
        self.isJump = True

    def is_on_ground(self):
        # check vertical collusions with platforms
        if not self.isJump:
            self.on_side = 0
        collisions_platform = pygame.sprite.spritecollide(self, list_platform_level[self.number_of_level], False)
        for platform in collisions_platform:
            if abs(self.speed_y) > 0 and self.rect.bottom > platform.rect.top and self.rect.top < platform.rect.top and not self.on_side:
                self.rect.bottom = platform.rect.top
                self.speed_y = 0
                self.isJump = False
                self.ready_to_jump = False
            elif abs(self.speed_y) > 0 and self.rect.top < platform.rect.bottom and self.rect.bottom > platform.rect.bottom and not self.on_side:
                self.rect.top = platform.rect.bottom
                self.speed_y = 0
                self.isJump = False

    def update(self):

        self.is_on_ground()
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.move(-1)
            self.dir = -1
            self.speed_x = -PLAYER_SPEED
        elif keys[pygame.K_RIGHT]:
            self.move(1)
            self.dir = 1
            self.speed_x = PLAYER_SPEED
        else:
            self.speed = 4
            if not self.isJump is True and channel.get_sound() != sound_button:
                channel.stop()

        if keys[pygame.K_SPACE]:
            if not self.ready_to_jump:
                self.speed_y = -PLAYER_SPEED
                if self.jumpSound == 0 and channel.get_sound() != sound_button:
                    channel.play(sound_pig[random.randint(0, 2)])
                self.jumpSound = 1
                self.isJump = True
                self.ready_to_jump = True

        if self.isJump and self.ready_to_jump:
            if self.jumpCount > 0:
                self.rect.y -= (self.jumpCount ** 2) // 2
                self.jumpCount -= 1
            elif not pygame.sprite.spritecollide(self, list_platform_level[self.number_of_level], False):
                self.rect.y += (self.jumpCount ** 2) // 2
                self.is_on_ground()
                self.jumpCount -= 1

        else:
            self.is_on_ground()
            channel.stop()
            self.jumpSound = 0
            self.jumpCount = 10

        collisions_bluecarrot = pygame.sprite.spritecollide(self, blue_carrot_level[self.number_of_level], False)
        if collisions_bluecarrot:
            channel.play(sound_eat)
            self.water_ability = 0
            for item in collisions_bluecarrot:
                item.kill()
                blue_carrot_level[self.number_of_level].remove(item)
            for water in list_water_level[self.number_of_level]:
                list_platform_level[self.number_of_level].append(water)
            #pygame.time.delay(500)




        collisions_carrot = pygame.sprite.spritecollide(self, simple_carrot_level[self.number_of_level], False)
        if collisions_carrot:
            channel.play(sound_eat)
            self.shoot_ability = 1
            for item in collisions_carrot:
                item.kill()
                simple_carrot_level[self.number_of_level].remove(item)
            #pygame.time.delay(500)




        collisions_water = pygame.sprite.spritecollide(self, list_water_level[self.number_of_level], False)
        if collisions_water and self.water_ability:
            channel.play(sound_water)
            #pygame.time.delay(1500)
            self.rect.center = (start_x, start_y)
            channel.play(sound_pig[random.randint(0, 2)])
            self.life_amount -= 1

        collisions_ships = pygame.sprite.spritecollide(self, list_ships_level[self.number_of_level], False)
        if collisions_ships:
            channel.play(sound_hurt)
            #pygame.time.delay(1500)
            self.rect.center = (start_x, start_y)
            channel.play(sound_pig[random.randint(0, 2)])
            self.life_amount -= 1

        collisions_chicken = pygame.sprite.spritecollide(self, list_chicken_level[self.number_of_level], False)
        if collisions_chicken:
            channel.play(sound_hurt)
            pygame.time.delay(1500)
            self.rect.center = (start_x, start_y)
            channel.play(sound_pig[random.randint(0, 2)])
            self.life_amount -= 1

        # Check horizontal collisions
        collisions_platform = pygame.sprite.spritecollide(self, list_platform_level[self.number_of_level], False)
        if not collisions_platform:
            self.on_side = 0
        for platform in collisions_platform:
            if self.speed_x > 0 and self.rect.right > platform.rect.left and self.rect.left < platform.rect.right and self.speed_y == 0:
                self.rect.right = platform.rect.left
                self.speed_x = 0
                self.on_side = 1
            elif self.speed_x < 0 and self.rect.left < platform.rect.right and self.rect.right > platform.rect.left and self.speed_y == 0:
                self.rect.left = platform.rect.right
                self.speed_x = 0
                self.on_side = 1

        # Gravity effect
        if not self.isJump:
            self.speed_y = 24
            self.rect.y += self.speed_y
            #self.is_on_ground()
        if self.rect.top >= 1080:
            pygame.time.delay(300)
            self.rect.center = (start_x, start_y)
            channel.play(sound_pig[random.randint(0, 2)])
            self.life_amount -= 1

        collisions_strawberry = pygame.sprite.spritecollide(self, strawberry_level[self.number_of_level], False)
        if collisions_strawberry:
            channel.play(sound_victory)
            pygame.time.delay(1500)
            for item in collisions_carrot:
                item.kill()
                strawberry_level[self.number_of_level].remove(item)
            self.shoot_ability = 0
            self.water_ability = 1
            self.rect.center = (start_x, start_y)
            self.number_of_level += 1
            create_level(self.number_of_level)


    def shoot_carrot(self):
        if self.shoot_ability:
         carrot = Carrot(self.rect.centerx, self.rect.top + 50, self.dir)
         return carrot
