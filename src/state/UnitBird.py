import math

from .Unit import Unit, State
from pygame.math import Vector2


class UnitBird(Unit):
    def __init__(self, position=Vector2(15, 4), speed=Vector2(-0.06, 0), affected_by_gravity=False,
                 size=Vector2(0.5, 0.5)):
        super().__init__(position, speed, affected_by_gravity,
                         size, State.b_fly)
        self.const_speed = Vector2(self.speed.x, self.speed.y)
        self.angle = 0

    def unique_movement(self):
        self.angle += 5
        cos = math.cos(math.radians(self.angle)) / 100
        sin = math.sin(math.radians(self.angle)) / 100
        rad_speed = 2 * Vector2(cos, sin)
        self.speed = self.const_speed + rad_speed
