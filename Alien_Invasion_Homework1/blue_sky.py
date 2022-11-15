import sys

import pygame

from rocket import Rocket
from bullette import Bullet
from star import Star

class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (250,250,250)
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.create_space()
        collisions = pygame.sprite.groupcollide(self.bullets, self.stars, True, True)

    def create_space(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        available_room_x = 1200
        available_room_y = 800
        number_stars_x = available_room_x // (2 * star_width)
        number_rows = available_room_y // (2 * star_height)
        print(number_rows)
        for row_number in range(number_rows):
                star = Star(self)
                star.y = star_height + 2 * star_height * number_rows
                self.x = 1100
                star.rect.x = 1100
                star.rect.y = star_height + 2 * star.rect.height * row_number
                self.stars.add(star)
    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            self._update_screen()
            self.bullets.update()
            if pygame.sprite.groupcollide(self.bullets, self.stars, True, True):
                sys.exit()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.rocket.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.rocket.moving_down = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.rocket.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.rocket.moving_down = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.rocket.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.stars.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()