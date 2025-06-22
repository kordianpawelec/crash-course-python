import pygame
from pygame.sprite import Sprite
from pathlib import Path


class Alien(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.image = pygame.image.load(Path(r'alien_invasion\images\alien.bmp'))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

