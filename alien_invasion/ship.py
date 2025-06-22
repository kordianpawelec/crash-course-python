import pygame
from pathlib import Path
from setting import Settings


class Ship():
    def __init__(self, game_instance):
        self.settings = Settings()
        self.screen = game_instance.screen
        self.screen_rectangle = game_instance.screen.get_rect()
        
        self.image = pygame.image.load(Path('alien_invasion\images\DurrrSpaceShip.bmp')).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rectangle.midbottom
        self.x = float(self.rect.x)

        self.left = False
        self.right = False
        
    

    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def update_action(self):
        if self.left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        elif self.right and self.rect.right < self.screen_rectangle.right:
            self.x += self.settings.ship_speed
        self.rect.x = self.x

    
    def center_ship(self):
        self.rect.midbottom = self.screen_rectangle.midbottom
        self.x = float(self.rect.x)
        