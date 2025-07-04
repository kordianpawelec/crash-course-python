import pygame
from pygame.sprite import Sprite
from pathlib import Path
from alien_bullet import AlienBullet


class Alien(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.game = game
        self.settings = game.settings
        self.image = pygame.image.load(Path(r'alien_invasion\images\alien.bmp')).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.alien_bullet_speed = self.settings.alien_bullet_speed


    def update(self):
        self.x += self.settings.alien_speed * self.settings.army_dir
        self.rect.x = self.x


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    

    def shoot(self):
        bullet = AlienBullet(self, self.game)
        bullet.update()
        