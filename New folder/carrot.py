from connectionAssets import *
import os
class Carrot(pygame.sprite.Sprite):
    def __init__(self, x, y,  direction):
        super().__init__()
        self.defaultImage = pygame.image.load(os.path.join(img_folder, 'flying_carrot.png')).convert()

        self.imageR = pygame.transform.flip(self.defaultImage, False, True)
        self.imageL = pygame.transform.flip(self.defaultImage, True, True)
        self.image = self.imageR
        self.imageL.set_colorkey((0, 0, 0))
        self.imageR.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = SPEED_CARROT
        self.direction = direction
        self.distance = 0

    def update(self):
        if self.direction == 1:
            self.image = self.imageR
        else:
            self.image = self.imageL
        self.rect.x += self.speed * self.direction
        self.distance += abs(self.speed)
        if self.rect.left > 1920 or self.rect.right < 0 or self.distance > 300:
            self.kill()


    def draw(self, screen):
        screen.blit(self.image, self.rect)