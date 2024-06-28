from pig import *
from platform import *
from carrot import Carrot
from Item import *
from button import *
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
for i in range(list_platform_level[number_of_level].__len__()):
    all_sprites.add(list_platform_level[number_of_level][i])
for i in range(list_chicken_level[number_of_level].__len__()):
    all_sprites.add(list_chicken_level[number_of_level][i])
all_sprites.add(blue_carrot_level[number_of_level])
all_sprites.add(player)
#chickens.add(han1)
#chickens.add(han2)


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
    life_text = font.render(f"Lives: {player.life_amount}", True, (0, 0, 0))
    life_rect = life_text.get_rect()
    life_rect.midtop = (start_x - 700, start_y - 410)
    screen.blit(life_text, life_rect)
    if player.life_amount <= 0:
        pygame.quit()
    

if __name__ == "__main__":
    main()