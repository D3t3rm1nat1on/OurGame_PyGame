import enum

import pygame
from pygame.math import Vector2


class State(enum.Enum):
    running = 0
    jumping_up = 1
    jumping_down = 2
    g_running = 3
    b_fly = 4


class Unit:
    def __init__(self, position, speed, affected_by_gravity=True, size=Vector2(1, 1), state=State.running):
        """

        :type position: Vector2
        :type speed:    Vector2
        """
        self.position = position
        self.speed = speed
        self.affected_by_gravity = affected_by_gravity
        self.size = size
        self.frame_index = 0
        self.state = state
        self.is_slowing = False
        self.is_sprinting = False
        self.is_collision_able = True
        self.is_alive = True

    def unique_movement(self):
        pass
