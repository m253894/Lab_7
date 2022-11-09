import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_game):
        super(Bullet, self).__init__()
        self.screen = ai_game.screen
        self.bullet_speed_factor = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60

        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midright = ai_game.rocket.rect.midright
        self.x = float(self.rect.x)
    def update(self):
        self.x += self.bullet_speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)
