from typing import List

from pygame.math import Vector2

from .Unit import Unit


class GameState:
    border_right: int
    border_left: int
    gravity: Vector2
    ground: Vector2
    world_size: Vector2
    score: int
    enemies: List[Unit]
    player: Unit

    def __init__(self):
        self.score = 0
        self.world_size = Vector2(1600, 900)
        self.ground = Vector2(0, 675)
        self.gravity = Vector2(0, 0.5)
        self.border_left = 0
        self.border_right = 900

        self.player = Unit(full_size=Vector2(40, 80))
        self.enemies = []
