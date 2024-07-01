from platform import *
from carrot import *
global number_of_level
class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.life_amount = 3
        self.water_ability = 1
        self.shoot_ability = 0
        pygame.sprite.Sprite.__init__(self)
        self.key_pressed = False
        self.image = player_img_set[1]
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
    
    def move(self, k):
        print((k+1) // 2)
        self.image = pygame.transform.flip(player_img_set[self.i], (k+1) // 2, False)
        self.image.set_colorkey(BLACK)
        self.i += 1
        if self.i == 3:
            self.i = 0
        if not channel0.get_busy() and channel0.get_sound() != sound_button:
            channel0.play(sound_walk_pig)
        self.rect.x += self.speed * k
        if self.speed < 15:
            self.speed += 1
    
    def jump(self):
        if self.jumpSound == 0:
                channel0.stop()
                channel1.play(sound_pig[random.randint(0, 2)])
                self.jumpSound = 1
        self.isJump = True

    def is_on_ground(self):
        # check vertical collusions with platforms
        collisions_platform = pygame.sprite.spritecollide(self, list_platform_level[number_of_level], False)
        for platform in collisions_platform:
            if abs(self.speed_y) > 0 and self.rect.bottom >= platform.rect.top and self.rect.top <= platform.rect.bottom:
                self.rect.bottom = platform.rect.top
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
            if not self.isJump is True and channel0.get_sound() != sound_button:
                channel0.stop()

        if keys[pygame.K_SPACE]:
            self.speed_y = -PLAYER_SPEED
            if self.jumpSound == 0 and channel0.get_sound() != sound_button:
                channel1.play(sound_pig[random.randint(0, 2)])
            self.jumpSound = 1
            self.isJump = True
        if self.isJump is True:
            if self.jumpCount > 0:
                self.rect.y -= (self.jumpCount ** 2) // 2
                self.jumpCount -= 1
            elif not pygame.sprite.spritecollide(self, list_platform_level[number_of_level], False):
                self.rect.y += (self.jumpCount ** 2) // 2
                self.is_on_ground()
                self.jumpCount -= 1

        else:
            self.is_on_ground()
            channel1.stop()
            self.jumpSound = 0
            self.jumpCount = 10

        collisions_bluecarrot = pygame.sprite.spritecollide(self, blue_carrot_level[number_of_level], False)
        if collisions_bluecarrot:
            self.water_ability = 0
            for item in collisions_bluecarrot:
                item.kill()
                blue_carrot_level[number_of_level].remove(item)

        collisions_carrot = pygame.sprite.spritecollide(self, simple_carrot_level[number_of_level], False)
        if collisions_carrot:
            self.shoot_ability = 1
            for item in collisions_carrot:
                item.kill()
                simple_carrot_level[number_of_level].remove(item)

        collisions_strawberry = pygame.sprite.spritecollide(self, strawberry_level[number_of_level], False)
        if collisions_strawberry:
            pygame.time.delay(1500)
            for item in collisions_carrot:
                item.kill()
                strawberry_level[number_of_level].remove(item)
            self.shoot_ability = 0
            self.water_ability = 1
            self.rect.center = (start_x, start_y)
            #number_of_level += 1 ТУТ ПРОБЛЕМА
            create_level()

        collisions_water = pygame.sprite.spritecollide(self, list_water_level[number_of_level], False)
        if collisions_water and self.water_ability:
            pygame.time.delay(1500)
            self.rect.center = (start_x, start_y)
            channel1.play(sound_pig[random.randint(0, 2)])
            self.life_amount -= 1

        collisions_ships = pygame.sprite.spritecollide(self, list_ships_level[number_of_level], False)
        if collisions_ships:
            pygame.time.delay(1500)
            self.rect.center = (start_x, start_y)
            channel1.play(sound_pig[random.randint(0, 2)])
            self.life_amount -= 1

        collisions_chicken = pygame.sprite.spritecollide(self, list_chicken_level[number_of_level], False)
        if collisions_chicken:
            pygame.time.delay(1500)
            self.rect.center = (start_x, start_y)
            channel1.play(sound_pig[random.randint(0, 2)])
            self.life_amount -= 1

        # Check horizontal collisions
        collisions_platform = pygame.sprite.spritecollide(self, list_platform_level[number_of_level], False)
        for platform in collisions_platform:
            if self.speed_x > 0 and self.rect.right > platform.rect.left and self.rect.left < platform.rect.right and self.speed_y == 0:
                self.rect.right = platform.rect.left
                self.speed_x = 0
            elif self.speed_x < 0 and self.rect.left < platform.rect.right and self.rect.right > platform.rect.left and self.speed_y == 0:
                self.rect.left = platform.rect.right
                self.speed_x = 0

        # Gravity effect
        if not self.isJump:
            self.speed_y = 24
            self.rect.y += self.speed_y
        if self.rect.top >= 1080:
            pygame.time.delay(300)
            self.rect.center = (start_x, start_y)
            channel1.play(sound_pig[random.randint(0, 2)])
            self.life_amount -= 1


    def shoot_carrot(self):
        if self.shoot_ability:
         carrot = Carrot(self.rect.centerx, self.rect.top + 50, self.dir)
         return carrot


