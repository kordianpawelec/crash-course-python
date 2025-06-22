import pygame
import sys
from setting import Settings
from ship import Ship
from pathlib import Path
from enum_keys import Keys
from bullet import Bullet
from the_alien_the_heretic_the_mutant import Alien
from star_sky import StarSky
from falling_star import FallingStar
import random


class AlienInvasion():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.running = True
        self.clock = pygame.time.Clock()
        self.bg_clour = self.settings.screen_bg
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.falling_stars = pygame.sprite.Group()
        self.create_alien_fleet()
        self.sky = StarSky(self)


    def run_game(self):
        while self.running:
            self.create_falling_stars()
            self.action_listoner()
            self.screen_update()
    
            self.updade_bullets()
            self.update_falling_stars()
            self.update_aliens_movement()

            self.ship.update_action()
            self.clock.tick(self.settings.tick_rate)

            
    def action_listoner(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_event(event)
                

    def check_keydown_event(self, event):
        if event.key == Keys.A.value:
            self.ship.left = True
        elif event.key == Keys.D.value:
            self.ship.right = True
        elif event.key == Keys.Q.value:
            sys.exit()
        elif event.key == Keys.F_12.value:
            self.set_full_screen()
        elif event.key == Keys.SPACE.value:
            self.fire_bullet()


    def check_keyup_event(self, event):
        if event.key == Keys.A.value:
            self.ship.left = False
        elif event.key == Keys.D.value:
            self.ship.right = False


    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def updade_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)


    def screen_update(self):
        self.screen.fill(self.bg_clour)
        self.sky.draw_sky()


        for falling_star in self.falling_stars.sprites():
            falling_star.draw_falling_star()


        for bullet in self.bullets.sprites():
            bullet.draw_bullet()


        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()
        

    def create_alien_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        current_y = alien_height
        current_x = alien_width


        while current_y < (self.settings.screen_height - 3 * alien_height):
            while  current_x <  (self.settings.screen_width - 2 * alien_width):
                self.create_alien(current_x,current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height


    def create_alien(self, x_position, y_position):
            new_alien = Alien(self)
            new_alien.x = x_position
            new_alien.y = y_position
            new_alien.rect.x = x_position
            new_alien.rect.y = y_position
            self.aliens.add(new_alien)

        
    def update_aliens_movement(self):
        self.check_army_edge()
        self.aliens.update()
            

    def check_army_edge(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break


    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.army_drop_speed
        self.settings.army_dir *= -1


    def create_falling_stars(self):
        while len(self.falling_stars.sprites()) < self.settings.number_of_stars_on_screen and random.randrange(1,5) == 4:
            new_falling_star = FallingStar(self)
            self.falling_stars.add(new_falling_star)
            

    def update_falling_stars(self):
        self.falling_stars.update()
        for star in self.falling_stars.copy():
            if star.rect.top > self.settings.screen_height:
                self.falling_stars.remove(star)


if __name__ == '__main__':
    alien = AlienInvasion()
    alien.run_game()