from platform import *
from Enemy import Han
from pig import *
from carrot import Carrot
from Item import *
from button import *
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
ships_group = pygame.sprite.Group()
water_group = pygame.sprite.Group()
blue_carrot = pygame.sprite.Group()
carrots = pygame.sprite.Group()
#chickens = pygame.sprite.Group()
blue_carrot.add(Blue_carrot(start_x - 200, start_y + 40))
player = Player()

for i in range(9):
    all_sprites.add(list_platform_level1[i])
for i in range(2):
    ships_group.add(list_ships_level1[i])
water_group.add(list_water_level1[0])
all_sprites.add(blue_carrot)
all_sprites.add(player)

han1 = Han((800, 530), True, 600, 900)
han2 = Han((1300, 530), False, 1200, 1400)
#chickens.add(han1)
#chickens.add(han2)
all_sprites.add(han1)
all_sprites.add(han2)

font = pygame.font.Font(None, 36)

def main():
    global last_shot_time
    last_shot_time = pygame.time.get_ticks()
    is_menu = 'Main_menu'
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                current_time = pygame.time.get_ticks()
                if current_time - last_shot_time > 500:
                    if event.key == pygame.K_r:
                        carrot = player.shoot_carrot()
                        if carrot:
                            carrots.add(carrot)
                            all_sprites.add(carrot)
                            last_shot_time = current_time
                if event.key == pygame.K_ESCAPE:
                #channel0.stop()
                    if is_menu == 'Main_menu':
                        running = False
                    if is_menu == 'Option_menu':
                        is_menu = 'Main_menu'
                    if is_menu == 'Game':
                        is_menu = 'Pause'
                    if is_menu == 'Pause_2':
                        is_menu = 'Game'
                    
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_menu == 'Main_menu':
                    if quit_button.is_clicked(mouse_pos):
                        running = False
                    elif option_button.is_clicked(mouse_pos):
                        is_menu = 'Option_menu'
                        channel0.play(sound_button)
                    elif play_button.is_clicked(mouse_pos):
                        channel0.play(sound_button)
                        is_menu = 'Game'
                elif is_menu == 'Option_menu':
                    if quit_button.is_clicked(mouse_pos):
                        is_menu = 'Main_menu'
                        channel0.play(sound_button)
                    elif volume_button1.is_clicked(mouse_pos):
                        pass
                elif is_menu == 'Pause_2':
                    if quit_pause_button.is_clicked(mouse_pos):
                        is_menu = 'Main_menu'
                        channel0.play(sound_button)
                    
        mouse_pos = pygame.mouse.get_pos()

        pygame.display.flip()
        if is_menu == 'Game':
            game()
        if is_menu == 'Pause':
            is_menu = 'Main_menu'
            darkness_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            darkness_surface.fill((0, 0, 0, 128))
            screen.blit(darkness_surface, (0, 0))
        if is_menu == 'Main_menu':
             for button in main_menu_buttons:
                button.handle_hover(mouse_pos)
                button.draw(screen)
        if is_menu == 'Option_menu':
            for button in options_menu_buttons:
                button.handle_hover(mouse_pos)
                button.draw(screen)
        if is_menu == 'Pause_2':
                quit_pause_button.handle_hover(mouse_pos)
                quit_pause_button.draw(screen)
        pygame.display.flip()
    pygame.quit()
    
    
def game():
    all_sprites.update()
    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)
    life_text = font.render(f"Lives: {player.Life_amount}", True, (0, 0, 0))
    life_rect = life_text.get_rect()
    life_rect.midtop = (start_x - 700, start_y - 410)
    screen.blit(life_text, life_rect)
    collisions_carrot = pygame.sprite.spritecollide(player, blue_carrot, False)
    if collisions_carrot:
        player.Water_ability = 0
        all_sprites.remove(blue_carrot )
    collisions_water = pygame.sprite.spritecollide(player, water_group, False)
    if collisions_water and player.Water_ability:
        player.rect.center = (start_x, start_y)
        channel1.play(sound_pig[random.randint(0, 2)])
        player.Life_amount -= 1
    collisions = pygame.sprite.spritecollide(player, list_ships_level1, False)
    if collisions:
        player.rect.center = (start_x, start_y)
        channel1.play(sound_pig[random.randint(0, 2)])
        player.Life_amount -= 1
    if player.Life_amount <= 0:
        pygame.quit()
    

if __name__ == "__main__":
    main()