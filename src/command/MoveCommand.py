from pygame.math import Vector2

from .Command import Command


class MoveCommand(Command):
    def __init__(self, state, unit):
        self.state = state
        self.unit = unit

    def run(self):
        self.unit.speed += self.state.gravity
        self.unit.position += self.unit.speed
        if self.unit.position.y + self.unit.size.y >= self.state.ground.y and self.unit.speed.y >= 0:
            self.unit.position.y = self.state.ground.y - self.unit.size.y
            self.unit.speed = Vector2(self.unit.speed.x, 0)
