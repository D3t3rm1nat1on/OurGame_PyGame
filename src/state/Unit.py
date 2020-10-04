from pygame.math import Vector2

import pygame


class Unit:
    def __init__(self, position=Vector2(10, 20), speed=Vector2(0, 0), size=Vector2(40, 80), delta_speed=Vector2(0, 0)):
        self.position = position
        self.speed = speed
        self.delta_speed = delta_speed
        self.size = size
        self.rect_collision = pygame.Rect(position, size)
        self.crouch_size = Vector2(size.x, size.y / 2)
        self.is_crouching = False
        self.is_sprinting = False
        self.is_slowing = False
