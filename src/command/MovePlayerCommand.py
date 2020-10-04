import random

from pygame.math import Vector2

from .MoveCommand import MoveCommand


class MovePlayerCommand(MoveCommand):
    def __init__(self, state, player):
        super().__init__(state, player)

    def run(self):
        super().run()
        # зона игрока
        if self.unit.rect_collision.left <= self.state.border_left:
            self.unit.position.x = self.state.border_left
        if self.unit.rect_collision.right >= self.state.border_right:
            self.unit.position.x = self.state.border_right - self.unit.rect_collision.size[0]


