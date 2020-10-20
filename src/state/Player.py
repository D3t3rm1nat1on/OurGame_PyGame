import math

from .Unit import Unit
from pygame.math import Vector2


class Player(Unit):
    max_speed_x: float

    def __init__(self, position=Vector2(10, 20), speed=Vector2(0, 0), full_size=Vector2(40, 80),
                 affected_by_gravity=False, max_speed_x=10.0):
        super().__init__(position, speed, full_size,
                         affected_by_gravity)
        self.max_speed_x = max_speed_x

    def unique_movement(self):
        if self.speed.x > self.max_speed_x:
            self.speed.x = self.max_speed_x
