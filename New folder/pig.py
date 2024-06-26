from connectionAssets import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.key_pressed = False
        self.image = player_img_set[1]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (start_x, start_y)
        self.speed = 4
        self.jumpCount = 10
        self.isJump = 10
        self.i = 0
        self.jumpSound = 0

    def move(self, k):
        print((k + 1) // 2)
        self.image = pygame.transform.flip(player_img_set[self.i], (k + 1) // 2, False)
        self.image.set_colorkey(BLACK)
        self.i += 1
        if self.i == 3:
            self.i = 0
        if not channel0.get_busy():
            channel0.play(sound_walk_pig)
        self.rect.x += self.speed * k
        if self.speed < 15:
            self.speed += 1

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.move(1)

        elif keys[pygame.K_LEFT]:
            self.move(-1)

        else:
            self.speed = 4
            channel0.stop()

        if keys[pygame.K_SPACE]:
            if self.jumpSound == 0:
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
                self.jumpSound = 0
                self.isJump = False
                self.jumpCount = 10