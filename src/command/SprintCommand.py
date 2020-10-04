from pygame.math import Vector2

from .Command import Command


class SprintCommand(Command):
    def __init__(self, state, unit):
        self.state = state
        self.unit = unit

    def run(self):
        if not self.unit.is_sprinting:
            self.unit.speed.x += 1
            self.unit.is_sprinting = True
