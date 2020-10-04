from pygame.math import Vector2

from .Command import Command


class CrouchCommand(Command):
    def __init__(self, state, unit):
        self.state = state
        self.unit = unit

    def run(self):
        if not self.unit.is_crouching:
            self.unit.rect_collision.size = self.unit.crouch_size
            self.unit.position.y += self.unit.size.y - self.unit.crouch_size.y
            self.unit.is_crouching = True
