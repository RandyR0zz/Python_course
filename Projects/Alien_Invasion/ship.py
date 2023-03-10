import pygame

from pygame.sprite import Sprite

class Ship(Sprite):
    """Класс для управления кораблем"""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его позицию"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('D:\IT_Learning_Folder\Practice\Projects\Alien_Invasion\images\ship.bmp')
        self.rect = self.image.get_rect()
        self.center_ship()

        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """Размещение корабля в центре нижней стороны"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)