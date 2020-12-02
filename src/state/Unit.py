import enum

from pygame.math import Vector2


class Unit:
    def __init__(self, position, speed, affected_by_gravity=True):
        """

        :type position: Vector2
        :type speed:    Vector2
        """
        self.position = position
        self.speed = speed
        self.affected_by_gravity = affected_by_gravity
        self.frame_index = 0
        self.state = State.running


class State(enum.Enum):
    running = 0
    jumping_up = 1
    jumping_down = 2
