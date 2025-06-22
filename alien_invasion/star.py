import pygame
from setting import Settings
from pathlib import Path
from pygame.sprite import Sprite
import random

class Star(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(Path(r'alien_invasion\images\star.bmp'))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.width = self.rect.width
        self.height = self.rect.height

    
    
