import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.rain_speed = 1
        self.fleet_direction = -1

        self.image = pygame.image.load('Images2/rain.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    def update(self):
        self.y += self.rain_speed
        self.rect.y = self.y
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom <= screen_rect.bottom:
            return True

