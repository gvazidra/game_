# -*- coding: utf-8 -*-
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
    virtual_surface.fill((250, 250, 250))
    all_sprites.add(player)
    all_sprites.update()
    virtual_surface.blit(background_img, (0, 0))
    all_sprites.draw(virtual_surface)
    draw_hearts(player.life_amount)

def main():
    global last_shot_time
    last_shot_time = pygame.time.get_ticks()
    global is_menu
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
                if event.key == pygame.K_ESCAPE:
                #channel.stop()
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
                    if is_menu == 'Loss' or is_menu == 'Win':
                        player.water_ability = 1
                        player.shoot_ability = 0
                        player.life_amount = 1
                        player.number_of_level = 0
                        player.rect.center = (start_x, start_y)
                        number_of_level = 0
                        Is_choose = False
                        virtual_surface.fill((40, 40, 150))
                        is_menu = 'Main_menu'
                    if is_menu == 'Volume_setting':
                        virtual_surface.fill((40, 40, 150))
                        is_menu = 'Option_menu'
                    if is_menu == 'Graph_menu':
                        virtual_surface.fill((40, 40, 150))
                        is_menu = 'Option_menu'



            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if is_menu == 'Main_menu':
                    if quit_button.is_clicked(mouse_pos):
                        running = False
                    elif option_button.is_clicked(mouse_pos):
                        is_menu = 'Option_menu'
                        channel.play(sound_button)
                    elif play_button.is_clicked(mouse_pos) and Is_choose == False:
                        channel.play(sound_button)
                        is_menu = 'Difficulty_menu'
                    elif play_button.is_clicked(mouse_pos) and Is_choose == True:
                        channel.play(sound_button)
                        is_menu = 'Game'
                elif is_menu == 'Option_menu':
                    if volume_button.is_clicked(mouse_pos):
                        channel.play(sound_button)
                        is_menu = 'Volume_setting'
                    if quit_button.is_clicked(mouse_pos):
                        is_menu = 'Main_menu'
                        channel.play(sound_button)
                    if graph_button.is_clicked(mouse_pos):
                        is_menu = 'Graph_menu'
                elif is_menu == 'Pause_2':
                    if quit_pause_button.is_clicked(mouse_pos):
                        is_menu = 'Main_menu'
                        channel.play(sound_button)
                elif is_menu == 'Difficulty_menu':
                    if easy_button.is_clicked(mouse_pos):
                        is_menu = 'Game'
                        player.life_amount = 5
                        number_of_level = 0
                        create_levels()
                        create_level(0)
                        Is_choose = True
                        channel.play(sound_button)
                    if normal_button.is_clicked(mouse_pos):
                            is_menu = 'Game'
                            player.life_amount = 3
                            number_of_level = 0
                            create_levels()
                            create_level(0)
                            Is_choose = True
                            channel.play(sound_button)
                    if hard_button.is_clicked(mouse_pos):
                            is_menu = 'Game'
                            player.life_amount = 1
                            number_of_level = 0
                            create_levels()
                            create_level(0) #НАДО ПОМЕНЯТЬ НА 0
                            Is_choose = True
                            channel.play(sound_button)
                elif is_menu == 'Volume_setting':
                    if quit_button.is_clicked(mouse_pos):
                        is_menu = 'Option_menu'
                        virtual_surface.fill((40, 40, 150))
                        channel.play(sound_button)
                    if click_1[0].is_clicked(mouse_pos):
                        channel.play(sound_button)
                        mixer_button_1.is_clicked(1)
                    if click_1[1].is_clicked(mouse_pos):
                        channel.play(sound_button)
                        mixer_button_1.is_clicked(-1)
                    if click_2[0].is_clicked(mouse_pos):
                        mixer_button_2.is_clicked_with_sound(1)
                    if click_2[1].is_clicked(mouse_pos):
                        mixer_button_2.is_clicked_with_sound(-1)
                elif is_menu == 'Graph_menu':
                    if quit_button.is_clicked(mouse_pos):
                        is_menu = 'Option_menu'
                        virtual_surface.fill((40, 40, 150))
                        channel.play(sound_button)
                    if click_1[0].is_clicked(mouse_pos) or click_1[1].is_clicked(mouse_pos):
                        if player.images == player_img_set_1:
                            player.skins_update(player_img_set_2)
                        else:
                            player.skins_update(player_img_set_1)



            elif event.type == pygame.VIDEORESIZE:
                global CURRENT_SIZE
                CURRENT_SIZE = event.size
                    
        mouse_pos = pygame.mouse.get_pos()

        pygame.display.flip()
        if is_menu == 'Game':
            game()
            CURRENT_SIZE = screen.get_size()
            scaled_surface = transform.scale(virtual_surface, CURRENT_SIZE)
            screen.blit(scaled_surface, (0, 0))
            pygame.display.flip()
        if is_menu == 'Pause':
            is_menu = 'Main_menu'
            darkness_surface = pygame.Surface((width_surface, height_surface), pygame.SRCALPHA)
            darkness_surface.fill((0, 0, 0, 128))
            virtual_surface.blit(darkness_surface, (0, 0))
        if is_menu == 'Main_menu':
            CURRENT_SIZE = screen.get_size()
            scaled_surface = transform.scale(virtual_surface, CURRENT_SIZE)
            screen.blit(scaled_surface, (0, 0))
            for button in main_menu_buttons:
                button.handle_hover(mouse_pos)
                button.draw(screen)
            pygame.display.flip()
        if is_menu == 'Option_menu':
            screen.fill((40, 40, 150))
            for button in options_menu_buttons:
                button.handle_hover(mouse_pos)
                button.draw(screen)
        if is_menu == 'Pause_2':
            quit_pause_button.handle_hover(mouse_pos)
            quit_pause_button.draw(screen)
        if is_menu == 'Difficulty_menu':
            for button in difficulty_menu_buttons:
                button.handle_hover(mouse_pos)
                button.draw(screen)
        if is_menu == 'Volume_setting':
            screen.fill((40, 40, 150))
            mixer_button_1.draw(screen)
            mixer_button_2.draw(screen)
            quit_button.handle_hover(mouse_pos)
            quit_button.draw(screen)
            for button in click_1:
                button.handle_hover(mouse_pos)
                button.draw(screen)
            for button in click_2:
                button.handle_hover(mouse_pos)
                button.draw(screen)
        if is_menu == 'Graph_menu':
            screen.fill((40, 40, 150))
            for button in click_1:
                button.handle_hover(mouse_pos)
                button.draw(screen)
            quit_button.handle_hover(mouse_pos)
            quit_button.draw(screen)
            if player.images == player_img_set_1:
                screen.blit(player_img_set_1[0], (screen.get_width() / 2 - (player_img_set_1[0].get_width() / 2), screen.get_height() / 2 -
                                                           (player_img_set_1[0].get_height() // 2)))
            else:
                screen.blit(player_img_set_2[0], (screen.get_width() / 2 - (player_img_set_1[0].get_width() / 2), screen.get_height() / 2 -
                                                           (player_img_set_1[0].get_height() // 2)))

            


        if player.life_amount <= 0:
            channel.stop()
            virtual_surface.fill((12, 12, 12))
            is_menu = "Loss"
            small_font = pygame.font.Font(None, 36)
            large_font = pygame.font.Font(None, 72)
            game_over_text = large_font.render("Вы проиграли!", True, WHITE)
            game_over_rect = game_over_text.get_rect(center=(virtual_surface.get_width() // 2, virtual_surface.get_height() // 2))
            virtual_surface.blit(game_over_text, game_over_rect)
            continue_text = small_font.render("Нажмите Escape, чтобы выйти", True, WHITE)
            continue_rect = continue_text.get_rect(center=(virtual_surface.get_width() // 2, virtual_surface.get_height() // 2 + 100))
            virtual_surface.blit(continue_text, continue_rect)
            CURRENT_SIZE = screen.get_size()
            scaled_surface = transform.scale(virtual_surface, CURRENT_SIZE)
            screen.blit(scaled_surface, (0, 0))
            pygame.display.flip()

        if player.number_of_level == 3:
            channel.stop()
            virtual_surface.fill((40, 40, 150))
            is_menu = "Win"
            small_font = pygame.font.Font(None, 36)
            large_font = pygame.font.Font(None, 72)
            game_over_text = large_font.render("Вы выиграли!", True, WHITE)
            game_over_rect = game_over_text.get_rect(center=(virtual_surface.get_width() // 2, virtual_surface.get_height() // 2))
            virtual_surface.blit(game_over_text, game_over_rect)
            continue_text = small_font.render("Нажмите Escape, чтобы выйти", True, WHITE)
            continue_rect = continue_text.get_rect(center=(virtual_surface.get_width() // 2, virtual_surface.get_height() // 2 + 100))
            virtual_surface.blit(continue_text, continue_rect)
            channel.play(sound_victory)
            CURRENT_SIZE = screen.get_size()
            scaled_surface = transform.scale(virtual_surface, CURRENT_SIZE)
            screen.blit(scaled_surface, (0, 0))
            pygame.display.flip()
        pygame.display.flip()

    pygame.quit()
    
    


    

if __name__ == "__main__":
    main()