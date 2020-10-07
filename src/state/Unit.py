from pygame.math import Vector2

import pygame


class Unit:
    def __init__(self, position=Vector2(10, 20), speed=Vector2(0, 0), full_size=Vector2(40, 80),
                 affected_by_gravity=True):
        self.position = position
        self.speed = speed
        self.delta_speed = Vector2(0, 0)
        self.full_size = full_size
        self.rect_collision = pygame.Rect(position, full_size)
        self.crouch_size = Vector2(full_size.x, full_size.y / 2)
        self.is_crouching = False
        self.is_sprinting = False
        self.is_slowing = False
        self.affected_by_gravity = affected_by_gravity
