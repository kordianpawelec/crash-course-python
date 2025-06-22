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
        attempts = 0
        while len(self.stars.sprites()) < self.settings.amout_of_stars and attempts < self.settings.while_loops_atempts:
            new_star = Star()


            pos_x = random.random() * (self.settings.screen_width - new_star.rect.width * 2)
            pos_y = random.random() * (self.settings.screen_height - new_star.rect.height * 2)


            if not self.is_valid_draw(pos_x, pos_y):
                new_star.rect.x = pos_x
                new_star.rect.y = pos_y
                self.stars.add(new_star)
                continue
            attempts += 1

    def is_valid_draw(self, pos_x, pos_y):
        for star in self.stars:
            if abs(star.rect.x - pos_x) < (star.width * 2) and abs(star.rect.y - pos_y) < (star.height * 2):
               return True 


    def draw_sky(self):
        self.stars.draw(self.screen)

    



        

