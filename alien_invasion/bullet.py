from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):


    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.colour = self.settings.bullet_colour

        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)
    
    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)