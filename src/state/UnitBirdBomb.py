import math

from .Unit import Unit
from .UnitBird import UnitBird
from pygame.math import Vector2


class UnitBirdBomb(UnitBird):
    def __init__(self, position=Vector2(10, 20), speed=Vector2(0, 0), full_size=Vector2(40, 80),
                 affected_by_gravity=False):
        super().__init__(position, speed, full_size,
                         affected_by_gravity)
        self.is_killable = False

    def hit(self):
        print("KA-BOOM")
        self.speed *= 0
        self.unique_movement = lambda : 0
        self.rect_collision.size = self.full_size * 2

    # def unique_movement(self):
    #     super().unique_movement()
    #     self.
    #
    # def go_big(self):
