import pygame
import random
from star import Star
from setting import Settings

class StarSky():    
    def __init__(self, game):
        self.settings = Settings()
        self.stars = pygame.sprite.Group()
        self.create_sky()
        self.screen = game.screen
        

    def create_sky(self):
        while len(self.stars.sprites()) < self.settings.amout_of_stars:
            new_star = Star()
            pos_x = random.random() * (self.settings.screen_width - new_star.rect.width * 2)
            pos_y = random.random() * (self.settings.screen_height - new_star.rect.height * 2)
            # new_star.x = pos_x
            # new_star.y = pos_y
            for star in self.stars.copy():
                distance = ((star.rect.centerx - pos_x)**2 + (star.rect.centery - pos_y)**2)**0.5
                if distance < 30 and distance < 30:
                    continue
            new_star.rect.x = pos_x
            new_star.rect.y = pos_y
            self.stars.add(new_star)


    def draw_sky(self):
        self.stars.draw(self.screen)

    



        

