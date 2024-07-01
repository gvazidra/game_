from pig import *
from platform import *
from button import *
from carrot import *

pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
player = Player()

carrots = pygame.sprite.Group()
font = pygame.font.Font(None, 36)


def game():
    all_sprites.add(player)
    all_sprites.update()
    virtual_surface.blit(background_img, (0, 0))
    all_sprites.draw(virtual_surface)
    life_text = font.render(f"Lives: {player.life_amount}", True, (0, 0, 0))
    life_rect = life_text.get_rect()
    life_rect.midtop = (100, 36)
    virtual_surface.blit(life_text, life_rect)

def main():
    pygame.FULLSCREEN
    global last_shot_time
    last_shot_time = pygame.time.get_ticks()
    is_menu = 'Main_menu'
    running = True
    water_used = False
    Game_active = True
    Is_choose = False

    while running: 
        if not player.water_ability and not water_used:
            for j in range (list_water_level[number_of_level].__len__()):
                list_platform_level[number_of_level].append(list_water_level[number_of_level][j])
            water_used = True
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
                            bad_for_chicken.add(carrot)






                            all_sprites.add(carrot)
                            last_shot_time = current_time
                if event.key == pygame.K_ESCAPE:  #ИЗМЕНИЛ
                #channel0.stop()
                    if is_menu == 'Main_menu':
                        running = False
                    if is_menu == 'Option_menu':
                        is_menu = 'Main_menu'
                    if is_menu == 'Game':
                        is_menu = 'Pause'
                    if is_menu == 'Pause_2':
                        is_menu = 'Game'
                    if is_menu == 'Difficulty_menu':
                        is_menu = 'Main_menu'
                    if is_menu == 'Loss':
                        running = False



            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_menu == 'Main_menu':
                    if quit_button.is_clicked(mouse_pos):
                        running = False
                    elif option_button.is_clicked(mouse_pos):
                        is_menu = 'Option_menu'
                        channel0.play(sound_button)
                    elif play_button.is_clicked(mouse_pos) and Is_choose == False:
                        channel0.play(sound_button)
                        is_menu = 'Difficulty_menu'
                    elif play_button.is_clicked(mouse_pos) and Is_choose == True:
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
                elif is_menu == 'Difficulty_menu':
                    if easy_button.is_clicked(mouse_pos):
                        is_menu = 'Game'
                        player.life_amount = 5
                        number_of_level = 0
                        create_levels()
                        create_level()
                        Is_choose = True
                        channel0.play(sound_button)
                    if normal_button.is_clicked(mouse_pos):
                            is_menu = 'Game'
                            player.life_amount = 3
                            number_of_level = 0
                            create_levels()
                            create_level()
                            Is_choose = True
                            channel0.play(sound_button)
                    if hard_button.is_clicked(mouse_pos):
                            is_menu = 'Game'
                            player.life_amount = 1
                            number_of_level = 0
                            create_levels()
                            create_level()
                            Is_choose = True
                            channel0.play(sound_button)



            elif event.type == pygame.VIDEORESIZE:
                CURRENT_SIZE = event.size
                    
        mouse_pos = pygame.mouse.get_pos()

        pygame.display.flip()
        if is_menu == 'Game':
            game()
        if is_menu == 'Pause':
            is_menu = 'Main_menu'
            darkness_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            darkness_surface.fill((0, 0, 0, 128))
            virtual_surface.blit(darkness_surface, (0, 0))
        if is_menu == 'Main_menu':
             for button in main_menu_buttons:
                button.handle_hover(mouse_pos)
                button.draw(virtual_surface)
        if is_menu == 'Option_menu':
            for button in options_menu_buttons:
                button.handle_hover(mouse_pos)
                button.draw(virtual_surface)
        if is_menu == 'Pause_2':
                quit_pause_button.handle_hover(mouse_pos)
                quit_pause_button.draw(virtual_surface)
        if is_menu == 'Difficulty_menu':
            for button in difficulty_menu_buttons:
                button.handle_hover(mouse_pos)
                button.draw(virtual_surface)


        if player.life_amount <= 0:
            virtual_surface.fill((12, 12, 12))
            channel1.set_volume(0.0)
            is_menu = "Loss"
            large_font = pygame.font.Font(None, 72)
            small_font = pygame.font.Font(None, 36)
            game_over_text = large_font.render("Вы проиграли!", True, WHITE)
            game_over_rect = game_over_text.get_rect(center=(virtual_surface.get_width() // 2, virtual_surface.get_height() // 2))
            virtual_surface.blit(game_over_text, game_over_rect)
            continue_text = small_font.render("Нажмите Escape, чтобы выйти", True, WHITE)
            continue_rect = continue_text.get_rect(center=(virtual_surface.get_width() // 2, virtual_surface.get_height() // 2 + 100))
            virtual_surface.blit(continue_text, continue_rect)

        #CURRENT_SIZE = screen.get_size()
        CURRENT_SIZE = (WIDTH, HEIGHT)
        scaled_surface = transform.scale(virtual_surface,CURRENT_SIZE)
        screen.blit(scaled_surface, (0,0))
        pygame.display.flip()

    pygame.quit()
    
    


    

if __name__ == "__main__":
    main()