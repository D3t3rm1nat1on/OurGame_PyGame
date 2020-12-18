import random
from datetime import datetime
import pygame
from pygame.math import Vector2

from state import Unit
from .MoveCommand import MoveCommand


class MoveItemCommand(MoveCommand):
    player_unit: Unit

    def __init__(self, state, item, player_unit):
        super().__init__(state, item)
        self.player_unit = player_unit


    def respawn_item(self):
        rand_x = random.randint(int(self.state.world_size.x * 1.2), int(self.state.world_size.x * 1.5))
        rand_y = random.randint(self.state.ground_level - 2, self.state.ground_level)
        self.unit.position = Vector2(rand_x, rand_y)


    def run(self):
        super().run()
        item = self.unit
        # пропустили предмет
        if item.position.x + item.size.x <= -item.size.x:
            self.respawn_item()

        if not item.is_alive:
            self.state.units.remove(item)

        item_col = pygame.Rect(item.position.elementwise() * Vector2(16, 16),
                                item.size.elementwise() * Vector2(16, 16))
        player_col = pygame.Rect(self.player_unit.position.elementwise() * Vector2(16, 16), (16, 16))
        # игрок поймал предмет
        if item_col.colliderect(player_col) and (item.position.x - self.player_unit.position.x) < 0.75:
            self.player_unit.position.x -= 0.75 - (item.position.x - self.player_unit.position.x)
            self.respawn_item()
            print("пойман предмет")

