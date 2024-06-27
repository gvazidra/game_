from connectionAssets import *
class Button:
    def __init__(self, center_x, center_y, image, hover_image):
        self.center_x = center_x
        self.center_y = center_y
        self.image = image
        self.hover_image = hover_image
        self.is_hovered = False
        self.width, self.height = image.get_size()
        self.x = center_x - self.width // 2
        self.y = center_y - self.height // 2

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, (self.x, self.y))

    def is_clicked(self, mouse_pos):
        button_rect = self.image.get_rect(center=(self.center_x, self.center_y))
        return button_rect.collidepoint(mouse_pos)

    def handle_hover(self, mouse_pos):
        self.is_hovered = self.is_clicked(mouse_pos)
        
quit_button = Button(WIDTH // 2, HEIGHT // 2 + 100, quit_button_img, quit_hover_button_img)
quit_pause_button = Button(WIDTH // 2, HEIGHT // 2, quit_button_img, quit_hover_button_img)
play_button = Button(WIDTH // 2, HEIGHT // 2 - 100, button_image, button_hover_image)
option_button = Button(WIDTH // 2, HEIGHT // 2, op_button_img, op_hover_button_img)
new_button1 = Button(WIDTH // 2, HEIGHT // 2 - 100, new_button_img, new_hover_button_img)
new_button2 = Button(WIDTH // 2, HEIGHT // 2, new_button_img, new_hover_button_img)

main_menu_buttons = [quit_button, play_button, option_button]
options_menu_buttons = [new_button1, new_button2, quit_button]