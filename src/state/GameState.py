from pygame.math import Vector2

from .Unit import Unit


class GameState:
    def __init__(self):
        self.world_size = Vector2(15, 10)
        self.ground = [[None] * self.world_width] * self.world_height
        self.units = [Unit(Vector2(3, 7), Vector2(0, 0), Vector2(0, 0))]

    @property
    def world_width(self):
        return int(self.world_size.x)

    @property
    def world_height(self):
        return int(self.world_size.y)
