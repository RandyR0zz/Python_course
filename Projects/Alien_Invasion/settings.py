import pygame

class Settings():
    """Класс для хранения всех настроек"""

    def __init__(self):
        """Инициализирует статистические настройки игры"""
        #Настройки экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_img = pygame.image.load('D:\IT_Learning_Folder\Practice\Projects\Alien_Invasion\images\sky.jpg')
        
        #Настройки корабля
        self.ship_limit = 3

        #Настройки снарядов
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 0)
        self.bullet_allowed = 3
        
        #Настройки пришельцев
        self.fleet_drop_speed = 7

        #Темп ускорения
        self.speedup_scale = 1.1

        #Темп роста стоимости пришельца
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed = 0.3
        self.bullet_speed = 0.6
        self.alien_speed = 0.2

        self.fleet_direction = 1

        #Подсчет очков
        self.alien_points = 50
    
    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
