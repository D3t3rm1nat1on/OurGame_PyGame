from pygame.math import Vector2

from .Unit import Unit, State
from .UnitBird import UnitBird
from .Player import Player


class GameState:
    active_perk = -1

    def __init__(self):
        self.world_size = Vector2(15, 10)
        self.ground = [[None] * self.world_width] * self.world_height
        self.gravity = Vector2(0, 0.005)
        self.units = [Player(Vector2(3, 7), Vector2(0, 0)),
                      Unit(Vector2(12, 7), Vector2(-0.08, 0), state=State.g_running),
                      UnitBird()]
        orb = UnitBird(Vector2(11, 7), Vector2(-0.07, 0), affected_by_gravity=False, size=Vector2(0.5, 0.5))
        orb.state = State.hp_orb
        self.items = [Unit(Vector2(14, 7), Vector2(-0.07, 0), affected_by_gravity=False, size=Vector2(0.5, 0.5),
                           state=State.coin),
                      orb,
                      Unit(Vector2(13, 7), Vector2(-0.07, 0), affected_by_gravity=False, size=Vector2(0.5, 0.5),
                           state=State.x2),
                      Unit(Vector2(12, 7), Vector2(-0.07, 0), affected_by_gravity=False, size=Vector2(0.5, 0.5),
                           state=State.magnet),
                      ]
        self.ground_level = 7
        self.border_left = 0.0
        self.border_right = 7.0

        self.score = 0
        self.money = 0
        self.lives = 0
        self.x2_counter = 0
        self.magnet_counter = 120

    @property
    def world_width(self):
        return int(self.world_size.x)

    @property
    def world_height(self):
        return int(self.world_size.y)
