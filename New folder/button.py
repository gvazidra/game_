# -*- coding: utf-8 -*-

from connectionAssets import *


class Button:
    def __init__(self, center_x, center_y, image, hover_image):
        self.center_x = center_x
        self.center_y = center_y
        self.image = image
        self.image.set_colorkey(BLACK)
        self.hover_image = hover_image
        self.hover_image.set_colorkey(BLACK)
        self.is_hovered = False
        self.width, self.height = image.get_size()
        self.x = center_x - self.width // 2
        self.y = center_y - self.height // 2

    def draw(self, virtual_surface):
        current_image = self.hover_image if self.is_hovered else self.image
        virtual_surface.blit(current_image, (self.x, self.y))

    def is_clicked(self, mouse_pos):
        button_rect = self.image.get_rect(center=(self.center_x, self.center_y))
        return button_rect.collidepoint(mouse_pos)

    def handle_hover(self, mouse_pos):
        self.is_hovered = self.is_clicked(mouse_pos)


class MixerButton():
    def __init__(self, center_x, center_y, image):
        self.center_x = center_x
        self.center_y = center_y
        self.k = 4
        self.images = image
        self.image = self.images[self.k]
        self.image.set_colorkey(BLACK)
        self.width, self.height = self.image.get_size()
        self.x = center_x - self.width // 2
        self.y = center_y - self.height // 2

    def draw(self, virtual_surface):
        virtual_surface.blit(self.image, (self.x, self.y))

    def is_clicked(self, i):
        if i == 1:
            if self.k > 0:
                self.k -= 1
                pygame.mixer.music.set_volume(self.k  / 9)
        if i == -1:
            if self.k < 9:
                self.k += 1
                pygame.mixer.music.set_volume(self.k / 9)
        self.update_image()

    def is_clicked_with_sound(self, i):
        if i == 1:
            if self.k > 0:
                self.k -= 1
                channel.set_volume(self.k / 9)
                channel.play(sound_button)
        if i == -1:
            if self.k < 9:
                self.k += 1
                channel.set_volume(self.k / 9)
                channel.play(sound_button)
        self.update_image()

    def update_image(self):
        self.image = self.images[self.k]


quit_button = Button(WIDTH // 2, HEIGHT // 2 + 100, quit_button_img, quit_hover_button_img)
quit_pause_button = Button(WIDTH // 2,  HEIGHT // 2, quit_button_img, quit_hover_button_img)
quit_button_cntrl = Button(WIDTH // 2, HEIGHT // 2 + 200, quit_button_img, quit_hover_button_img)
play_button = Button(WIDTH // 2, HEIGHT // 2 - 100, button_image, button_hover_image)

option_button = Button(WIDTH // 2, HEIGHT // 2, op_button_img, op_hover_button_img)
volume_button = Button(WIDTH // 2, HEIGHT // 2 - 100, volume_button_img, volume_hover_button_img)
graph_button = Button(WIDTH // 2 - 100, HEIGHT // 2, graph_button_img, graph_hover_button_img)
control_button = Button(WIDTH // 2 + 100, HEIGHT // 2, control_button_img, control_hover_button_img)
easy_button = Button(WIDTH // 2, HEIGHT // 2 + 100, easy_image, easy_hover_image)

normal_button = Button(WIDTH // 2, HEIGHT // 2, normal_image, normal_hover_image)
hard_button = Button(WIDTH // 2, HEIGHT // 2 - 100, hard_image, hard_hover_image)

difficulty_menu_buttons = [hard_button, normal_button, easy_button]

main_menu_buttons = [quit_button, play_button, option_button]

options_menu_buttons = [volume_button, graph_button, quit_button, control_button]

mixer_button_1 = MixerButton(WIDTH // 2, HEIGHT // 2, volume_mixer)

click_1 = [Button(WIDTH // 2 - 150, HEIGHT // 2, click_image, click_image), Button(WIDTH // 2 + 150, HEIGHT // 2,
            pygame.transform.flip(click_image, True, False),pygame.transform.flip(click_image, True, False)),]

mixer_button_2 = MixerButton(WIDTH // 2, HEIGHT // 2 - 100, volume_mixer)

click_2 = [Button(WIDTH // 2 - 150, HEIGHT // 2 - 100, click_image, click_image), Button(WIDTH // 2 + 150, HEIGHT // 2 - 100,
            pygame.transform.flip(click_image, True, False),pygame.transform.flip(click_image, True, False)),]
