from pygame.math import Vector2

from .Command import Command


class JumpCommand(Command):
    def __init__(self, state, unit):
        super().__init__()
        self.state = state
        self.unit = unit

    def run(self):
        if self.on_ground(self.state, self.unit):
            self.unit.speed -= Vector2(0, 14)
