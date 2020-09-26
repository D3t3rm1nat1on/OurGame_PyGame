from pygame.math import Vector2

from .Unit import Unit


class GameState:
    def __init__(self):
        self.epoch = 0
        self.world_size = Vector2(1600, 900)
        self.ground = Vector2(0, 675)
        self.unit = Unit(Vector2(1, 2), Vector2(1, 0)) ## coordinate and speed
