from pygame.math import Vector2

from .Unit import Unit


class GameState:
    def __init__(self):
        self.world_size = Vector2(1600, 900)
        self.ground = Vector2(0, 675)
        self.unit = Unit()
        self.gravity = Vector2(0, 0.5)
