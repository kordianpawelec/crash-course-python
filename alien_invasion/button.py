import pygame.font


class Button:
    def __init__(self, game, msg):
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        self.width = self.settings.button_width
        self.height = self.settings.buton_height
        self.button_colour = self.settings.button_colour
        self.text_colour = self.settings.button_text_colour
        self.font = pygame.font.SysFont(None, self.settings.button_font_size)
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.prep_button(msg)


    def prep_button(self, msg):
        self.msg_img = self.font.render(msg, True, self.text_colour, self.button_colour)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    
    def draw_button(self):
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)

