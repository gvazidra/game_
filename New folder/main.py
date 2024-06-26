from platform import *
from pig import *
from Enemy import Han
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
for i in range(9):
    all_sprites.add(list_platform_level1[i])
all_sprites.add(player)
han1 = Han((800, 530), True, 600, 900)
han2 = Han((1300, 530), False, 1200, 1400)
all_sprites.add(han1)
all_sprites.add(han2)


def main():
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
        all_sprites.update()
        screen.blit(background_img, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
    
if __name__ == "__main__":
    main()