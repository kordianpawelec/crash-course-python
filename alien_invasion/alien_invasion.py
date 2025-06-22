import pygame
import sys
from setting import Settings
from ship import Ship
from pathlib import Path
from enum_keys import Keys
from bullet import Bullet
from the_alien_the_heretic_the_mutant import Alien
from star_sky import StarSky

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
        self.create_alien_fleet()
        self.sky = StarSky(self)


    def run_game(self):
        while self.running:
            self.action_listoner()
            self.screen_update()
            self.updade_bullets()
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
        #updatebullet position
        self.bullets.update()
        #or copy because when we remove entries for the orgina python deosnt expect the loop to be cahge but if we creat a copy instead of sprit() its all g
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)


    def screen_update(self):
        self.screen.fill(self.bg_clour)
        self.sky.draw_sky()
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
            


if __name__ == '__main__':

    alien = AlienInvasion()
    alien.run_game()




    # def set_full_screen(self):
    #     self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    #     self.settings.screen_width = self.screen.get_rect().width
    #     self.settings.screen_height = self.screen.get_rect().height
#chunky why????
            # keys = pygame.key.get_pressed()
            # if keys[Keys.A.value]:
            #     self.ship.rect.x -= self.settings.speed
            # if keys[Keys.D.value]:
            #     self.ship.rect.x += self.settings.speed


            # elif event.type == pygame.KEYDOWN: