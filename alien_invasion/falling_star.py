import pygame
import random
from pygame.sprite import Sprite


class FallingStar(Sprite):


    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.colour = self.settings.falling_star_colour
        self.random_x = random.randint(self.settings.falling_star_width, self.settings.screen_width - self.settings.falling_star_width)
        self.rect = pygame.Rect(self.random_x, 0, self.settings.falling_star_width, self.settings.falling_star_height)
        self.y = float(self.rect.y)


    def update(self):
        self.y += self.settings.falling_star_speed
        self.rect.y = self.y

    
    def draw_falling_star(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)