import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect(self.x, self.y, 10, 60)
    
    def draw(self, screen):
        pygame.draw.rect(screen, 'white', self.rect)