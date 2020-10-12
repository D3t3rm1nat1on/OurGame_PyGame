from typing import List, Any

from pygame.math import Vector2
from src.state import Unit

class GameState:

    player: Unit

    def __init__(self):
        self.score = 0
        self.world_size = Vector2(1600, 900)
        self.ground = Vector2(0, 675)
        self.gravity = Vector2(0, 0.5)
        self.border_left = 0
        self.border_right = 300

        self.player = Unit.Unit(full_size=Vector2(40, 80))
        self.enemies = []
