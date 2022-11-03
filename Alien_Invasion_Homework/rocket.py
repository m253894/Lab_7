import pygame

class Rocket:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('HOMEWORK_PICS/Rocket.png')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.moving_up = False
        self.moving_down = False
        self.rocket_speed = 1.5
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_up:
            self.y -= self.rocket_speed
        if self.moving_down:
            self.y += self.rocket_speed
        self.rect.y = self.y
