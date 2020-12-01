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
        self.functions = []
        self.functions.append(self.first)
        self.explosion_size = 100
        self.explosion_count = 10

    def hit(self):
        print("KA-BOOM")
        for func in self.functions:
            func()

    def first(self):
        self.speed *= 0
        self.is_collision_able = False
        self.unique_movement = self.explosion
        self.functions.remove(self.first)

    def explosion(self):
        self.position.x -= 5
        self.position.y -= 5
        self.full_size += Vector2(10, 10)
        self.rect_collision.size = self.full_size + Vector2(10, 10)
        self.explosion_count -= 1
        if self.explosion_count == 0:
            self.unique_movement = lambda: 1
            self.is_alive = False

    # def unique_movement(self):
    #     super().unique_movement()
    #     self.
    #
    # def go_big(self):
