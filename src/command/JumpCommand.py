from pygame.math import Vector2

from .Command import Command


class JumpCommand(Command):
    def __init__(self, state, unit):
        self.state = state
        self.unit = unit

    def run(self):
        if self.unit.position.y + self.unit.size.y >= self.state.ground.y:
            self.unit.speed -= Vector2(0, 14)
