import random
from datetime import datetime
import pygame
from pygame.math import Vector2

from state import Unit, State
from .MoveCommand import MoveCommand


def sign(num):
    return -1 if num < 0 else 1


class MoveItemCommand(MoveCommand):
    player_unit: Unit

    def __init__(self, state, item, player_unit):
        super().__init__(state, item)
        self.player_unit = player_unit

    def respawn_item(self):
        factor = (1.2, 1.5)
        if self.unit.state == State.coin:
            factor = (1.2, 1.5)
        elif self.unit.state == State.hp_orb:
            factor = (8, 15)
        elif self.unit.state == State.x2:
            factor = (3, 9)
        elif self.unit.state == State.magnet:
            factor = (6, 12)
        rand_x = random.randint(int(self.state.world_size.x * factor[0]), int(self.state.world_size.x * factor[1]))
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
            self.respawn_item()
            if self.unit.state == State.coin:
                self.state.money += 1
                if self.state.x2_counter > 0:
                    self.state.money += 1
            elif self.unit.state == State.hp_orb:
                self.state.lives += 1
            elif self.unit.state == State.x2:
                self.state.x2_counter = 360
            elif self.unit.state == State.magnet:
                self.state.magnet_counter = 360
            print("пойман предмет")
        if self.unit.state == State.coin and self.state.magnet_counter > 0:
            speed = abs(self.unit.speed.x) + abs(self.unit.speed.y)
            pos_diff = self.unit.position - self.player_unit.position
            x_diff = abs(pos_diff.x)
            y_diff = abs(pos_diff.y)
            diff = x_diff + y_diff
            self.unit.speed.x = -sign(pos_diff.x) * speed * (x_diff / diff)
            self.unit.speed.y = -sign(pos_diff.y) * speed * (y_diff / diff)
