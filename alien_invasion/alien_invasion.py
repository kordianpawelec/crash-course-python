import pygame
import sys
from time import sleep
from setting import Settings
from ship import Ship
from pathlib import Path
from enum_keys import Keys
from bullet import Bullet
from the_alien_the_heretic_the_mutant import Alien
from star_sky import StarSky
from falling_star import FallingStar
from alien_bullet import AlienBullet
import random
from games_states import GameState
from score_board import Scoreboard
from button import Button


class AlienInvasion():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.stats = GameState(self)
        self.running = True
        self.clock = pygame.time.Clock()
        self.bg_clour = self.settings.screen_bg
        self.ship = Ship(self)
        self.alien_bullets = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.falling_stars = pygame.sprite.Group()
        self.create_alien_fleet()
        self.sky = StarSky(self)
        self.game_active = False
        self.play_button = Button(self, "Play Game")
        self.score_board = Scoreboard(self)



    def run_game(self):
        while self.running:
            self.action_listoner()

            if self.game_active:
                self.alien_shot()
                self.update_alien_bullets()
                self.create_falling_stars()
                self.ship.update_action()
                self.updade_bullets()
                self.update_falling_stars()
                self.update_aliens_movement()
            
            self.screen_update()
            self.clock.tick(self.settings.tick_rate)

            
    def action_listoner(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.stats.save_saved_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_clicked(mouse_pos)
            self.mouse_hover(pygame.mouse.get_pos())

                

    def check_keydown_event(self, event):
        if event.key == Keys.A.value:
            self.ship.left = True
        elif event.key == Keys.D.value:
            self.ship.right = True
        elif event.key == Keys.Q.value:
            self.stats.save_saved_score()
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
        self.check_alien_bullet_collison()
        

    def check_alien_bullet_collison(self):
        collsion = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collsion:
            for aliens in collsion.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.score_board.prep_score() 
            self.score_board.check_high_score()
        if not self.aliens:
            self.bullets.empty()
            self.create_alien_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.score_board.prep_level()

    def screen_update(self):
        self.screen.fill(self.bg_clour)

        self.sky.draw_sky()
        
        for falling_star in self.falling_stars.sprites():
            falling_star.draw_falling_star()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        for bull in self.alien_bullets.sprites():
            bull.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)
        if not self.game_active:
            self.play_button.draw_button()

        self.score_board.show_score()

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
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()

        self.check_alien_bottom()
            

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

    def ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.bullets.empty()
            self.aliens.empty()
            self.falling_stars.empty()
            self.sky.create_sky()
            self.create_alien_fleet()
            self.ship.center_ship()
            self.score_board.prep_ship()
            sleep(1)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def check_alien_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom > self.settings.screen_height:
                self.ship_hit()

    def check_play_clicked(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.stats.reset_game()
            self.game_active = True
            self.bullets.empty()
            self.aliens.empty()
            self.create_alien_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)
            self.settings.init_dynamic_settings()
            self.score_board.prep_score()
            self.score_board.prep_level()
            self.score_board.prep_ship()
            
    
    def mouse_hover(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.play_button.button_colour = self.settings.button_hover_colour
        else:
            self.play_button.button_colour = self.settings.button_colour


    def alie_shoot(self):
        if self.aliens:
            shooting_alien = random.choice(self.aliens.sprites())
            bullet = AlienBullet(self, shooting_alien)
            self.alien_bullets.add(bullet)

    
    def update_alien_bullets(self):
        self.alien_bullets.update()
        for bullet in self.alien_bullets.copy():
            if bullet.rect.top > self.settings.screen_height:
                self.alien_bullets.remove(bullet)
            elif bullet.rect.colliderect(self.ship.rect):
                self.ship_hit()
                self.alien_bullets.remove(bullet)

    def alien_shot(self):
        if random.randint(1,600) and len(self.alien_bullets) < 5:
            self.alie_shoot()


if __name__ == '__main__':
    alien = AlienInvasion()
    alien.run_game()