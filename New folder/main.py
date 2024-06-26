from platform import *
from Item import *
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
ships_group = pygame.sprite.Group()
water_group = pygame.sprite.Group()
blue_carrot = pygame.sprite.Group()
blue_carrot.add(Blue_carrot(start_x - 200, start_y + 40))
player = Player()
for i in range(9):
    all_sprites.add(list_platform_level1[i])
for i in range(2):
    ships_group.add(list_ships_level1[i])
water_group.add(list_water_level1[0])
all_sprites.add(blue_carrot)
all_sprites.add(player)
font = pygame.font.Font(None, 36)
def main():
    running = True
    Life_amount = 3 #переменная тут, так как почему-то в других местах она не была видна(((#
    Water_ability = 1
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                k = pygame.key.get_pressed()
                if k[pygame.K_ESCAPE]:
                    running = False
        all_sprites.update()
        screen.blit(background_img, (0, 0))
        all_sprites.draw(screen)
        life_text = font.render(f"Жизни: {Life_amount}", True, (0, 0, 0))
        life_rect = life_text.get_rect()
        life_rect.midtop = (start_x - 700, start_y - 410)
        screen.blit(life_text, life_rect)
        collisions_carrot = pygame.sprite.spritecollide(player, blue_carrot, False)
        if collisions_carrot:
            Water_ability = 0
            all_sprites.remove(blue_carrot )
        collisions_water = pygame.sprite.spritecollide(player, water_group, False)
        if collisions_water and Water_ability:
            player.rect.center = (start_x, start_y)
            channel1.play(sound_pig[random.randint(0, 2)])
            Life_amount -= 1
        collisions = pygame.sprite.spritecollide(player, list_ships_level1, False)
        if collisions:
            player.rect.center = (start_x, start_y)
            channel1.play(sound_pig[random.randint(0, 2)])
            Life_amount -= 1
        if Life_amount <= 0:
            pygame.quit()
        else:
            pygame.display.flip()
    pygame.quit()
    
if __name__ == "__main__":
    main()