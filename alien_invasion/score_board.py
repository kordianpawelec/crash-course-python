import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats
        self.game = game
        self.text_colour = self.settings.button_text_colour_score
        self.font = pygame.font.SysFont(None, self.settings.button_font_size)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()


    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_string = f"{rounded_score:,}"
        self.score_image = self.font.render(score_string, True, self.text_colour, self.settings.screen_bg)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - self.settings.score_image_offset
        self.score_rect.top = self.settings.score_image_offset


    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_image_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)


    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_string = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_string, True, self.text_colour, self.settings.screen_bg)

        self.high_score_image_rect = self.high_score_image.get_rect()
        self.high_score_image_rect.centerx = self.screen_rect.centerx
        self.high_score_image_rect.top = self.screen_rect.top

    
    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()


    def prep_level(self):
        level_string = str(self.stats.level)
        self.level_image = self.font.render(level_string, True, self.text_colour, self.settings.screen_bg)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + self.settings.score_image_offset

    def prep_ship(self):
        self.ships = Group()
        for ships in range(self.stats.ships_left):
            ship = Ship(self.game)
            ship.rect.x = 10 + ships *  ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)