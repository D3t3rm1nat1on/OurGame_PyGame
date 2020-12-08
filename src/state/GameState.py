from pygame.math import Vector2

from .Unit import Unit
from .Player import Player


class GameState:
    def __init__(self):
        self.world_size = Vector2(15, 10)
        self.ground = [[None] * self.world_width] * self.world_height
        self.gravity = Vector2(0, 0.005)
        self.units = [Player(Vector2(3, 7), Vector2(0, 0))]
        self.ground_level = 7
        self.border_left = 0.0
        self.border_right = 7.0

    @property
    def world_width(self):
        return int(self.world_size.x)

    @property
    def world_height(self):
        return int(self.world_size.y)
