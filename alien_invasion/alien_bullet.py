from bullet import Bullet
import pygame

class AlienBullet(Bullet):
    def __init__(self, game, alien):
        super().__init__(game)
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.colour = self.settings.bullet_colour_alien
        self.rect.midtop = alien.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.alien_bullet_speed
        self.rect.y = self.y


    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)
