import math

from .Unit import Unit
from pygame.math import Vector2


class Player(Unit):
    stamina: float
    max_speed_x: float

    def __init__(self, position=Vector2(10, 20), speed=Vector2(0, 0), full_size=Vector2(40, 80),
                 affected_by_gravity=False):
        super().__init__(position, speed, full_size,
                         affected_by_gravity)
        self.max_speed_x = 5
        self.stamina = 100

    def sprint(self):
        self.speed.x += 0.08
        self.stamina -= 0.5

    def unique_movement(self):
        if self.is_sprinting and self.stamina >= 0.5:
            self.sprint()
        else:
            self.stamina += 0.3
            if self.stamina > 100.0:
                self.stamina = 100.0
            if self.speed.x > 0:
                if self.speed.x > 0.16:
                    self.speed.x -= 0.16
                else:
                    self.speed.x = 0
        if self.speed.x > self.max_speed_x:
            self.speed.x = self.max_speed_x
