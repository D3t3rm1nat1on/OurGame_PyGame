import math

from .Unit import Unit
from pygame.math import Vector2


class UnitBird(Unit):
    def __init__(self, position=Vector2(10, 20), speed=Vector2(0, 0), full_size=Vector2(40, 80),
                 affected_by_gravity=False):
        super().__init__(position, speed, full_size,
                         affected_by_gravity)
        self.const_speed = Vector2(self.speed.x, self.speed.y)
        self.angle = 0

    def unique_movement(self):
        self.angle += 5
        cos = math.cos(math.radians(self.angle))
        sin = math.sin(math.radians(self.angle))
        rad_speed = 2 * Vector2(cos, sin)
        self.speed = self.const_speed + rad_speed
