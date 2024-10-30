import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.x = x
        self.y = y # stays constant
        self.rect = pygame.rect.Rect(self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    def draw(self, screen):
        pygame.draw.rect(screen, 'white', self.rect)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= PLAYER_SPEED * dt # y values are moving up as you go down
        if keys[pygame.K_s]:
            self.y += PLAYER_SPEED * dt

        self.rect.y = self.y
