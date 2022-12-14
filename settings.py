import pygame

class Settings():

    def __init__(self):
        # Параметры экрана
        self.screen_width = 1150
        self.screen_height = 700
        self.bg_color = (230, 230, 230)


        # Параметры пули

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 50, 50
        self.bullets_allowed = 3

        # Настройки корабля

        self.ship_limit = 3

        # Настройки пришельцев
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.

        # Подсчет очков
        self.alien_points = 50

        # Темп ускорения игры
        self.speedup_scale = 1.2
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        #"""Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 1.2
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
        # Подсчет очков
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

    def increase_speed(self):
        #"""Увеличивает настройки скорости."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
