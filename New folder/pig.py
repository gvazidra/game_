from platform import *
class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.life_amount = 4
        self.water_ability = 1
        pygame.sprite.Sprite.__init__(self)
        self.key_pressed = False
        self.image = player_img_set[1]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (960, 540)
        self.speed = 4
        self.jumpCount = 10
        self.isJump = 0
        self.i = 0
        self.jumpSound = 0
        self.dir = -1
    
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
    
    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.move(-1)
            self.dir = -1
        elif keys[pygame.K_RIGHT]:
            self.move(1)
            self.dir = 1
        else:
            self.speed = 4
            if not self.isJump is True and channel0.get_sound() != sound_button:
                channel0.stop()
                
        if keys[pygame.K_SPACE]:
            if self.jumpSound == 0 and channel0.get_sound() != sound_button:
                channel1.play(sound_pig[random.randint(0, 2)])
            self.jumpSound = 1
            self.isJump = True
        if self.isJump is True:

            if self.jumpCount >= -10:

                if self.jumpCount < 0:
                    self.rect.y += (self.jumpCount ** 2) // 2
                else:
                    self.rect.y -= (self.jumpCount ** 2) // 2

                self.jumpCount -= 1

            else:
                channel1.stop()
                self.jumpSound = 0
                self.isJump = False
                self.jumpCount = 10

        collisions_falls = pygame.sprite.spritecollide(self, list_platform_level[number_of_level], False)
        if (not collisions_falls) and self.isJump == 0:
            self.rect.y += 12
        collisions_carrot = pygame.sprite.spritecollide(self, blue_carrot_level, False)
        if collisions_carrot:
            self.water_ability = 0
            blue_carrot_level[number_of_level].image.set_alpha(0)
        collisions_water = pygame.sprite.spritecollide(self, list_water_level[number_of_level], False)
        if collisions_water and self.water_ability:
            pygame.time.delay(300)
            self.rect.center = (start_x, start_y)
            channel1.play(sound_pig[random.randint(0, 2)])
            self.life_amount -= 1
        collisions_ships = pygame.sprite.spritecollide(self, list_ships_level[number_of_level], False)
        if collisions_ships:
            pygame.time.delay(250)
            self.rect.center = (start_x, start_y)
            channel1.play(sound_pig[random.randint(0, 2)])
            self.life_amount -= 1
        collisions_chicken = pygame.sprite.spritecollide(self, list_chicken_level[number_of_level], False)
        if collisions_chicken:
            pygame.time.delay(250)
            self.rect.center = (start_x, start_y)
            channel1.play(sound_pig[random.randint(0, 2)])
            self.life_amount -= 1

    def shoot_carrot(self):
        carrot = Carrot(self.rect.centerx, self.rect.top + 50, self.dir)
        return carrot

