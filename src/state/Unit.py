from pygame.math import Vector2

import pygame
from pygame.rect import RectType


class Unit:
    position: Vector2
    speed: Vector2
    delta_speed: Vector2
    full_size: Vector2
    rect_collision: RectType
    crouch_size: Vector2
    is_crouching: bool
    is_sprinting: bool
    is_slowing: bool
    affected_by_gravity: bool

    def __init__(self, position=Vector2(10, 20), speed=Vector2(0, 0), full_size=Vector2(40, 80),
                 affected_by_gravity=True):
        """

        :type speed: Vector2
        :type position Vector2
        :type full_size Vector2
        :type affected_by_gravity bool
        """
        self.is_alive = True

        self.is_killable = False
        self.is_collision_able = True
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

    def unique_movement(self):
        pass

    def hit(self):
        pass
