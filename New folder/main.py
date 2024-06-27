import pygame
from platform import *
from Enemy import Han
from pig import *
from carrot import Carrot

pygame.init()
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
carrots = pygame.sprite.Group()
#chickens = pygame.sprite.Group()

player = Player()
for i in range(9):
    all_sprites.add(list_platform_level1[i])
all_sprites.add(player)

han1 = Han((800, 530), True, 600, 900)
han2 = Han((1300, 530), False, 1200, 1400)
#chickens.add(han1)
#chickens.add(han2)
all_sprites.add(han1)
all_sprites.add(han2)

def main():
    running = True
    global last_shot_time
    last_shot_time = pygame.time.get_ticks()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                if event.type == pygame.KEYDOWN:
                    current_time = pygame.time.get_ticks()
                    if current_time - last_shot_time > 500:
                        if event.key == pygame.K_r:
                            carrot = player.shoot_carrot()
                            if carrot:
                                carrots.add(carrot)
                                all_sprites.add(carrot)
                                last_shot_time = current_time
                    if event.key == pygame.K_ESCAPE:
                        running = False

        screen.fill(WHITE)
        screen.blit(background_img, (0, 0))
        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.flip()

    pygame.quit()
    
if __name__ == "__main__":
    main()