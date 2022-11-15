import sys

import pygame
from rain import Rain

class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (230, 230, 230)
        self.drops = pygame.sprite.Group()
        self.create_rain()
    def create_rain(self):
        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        available_room_x = 1200
        number_drops_x = available_room_x // (2 * rain_width)
        for rain_number in range(number_drops_x):
            rain = Rain(self)
            rain.x = rain_width + 2 * rain_width * rain_number
            rain.rect.x = rain.x
            self.drops.add(rain)
    def check_fleet_edges(self):
        for rain in self.drops.sprites():
            if rain.check_edges():
                self.create_rain()
                break
    def _update_drops(self):
        self.drops.update()
        self.check_fleet_edges()
    def run_game(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._update_drops()
            self.screen.fill(self.bg_color)
            self.drops.draw(self.screen)
            pygame.display.flip()
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()