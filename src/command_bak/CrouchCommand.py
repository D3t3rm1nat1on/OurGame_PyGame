from .Command import Command
from src.state_bak import Unit


class CrouchCommand(Command):
    unit: Unit

    def __init__(self, state, unit):
        super().__init__()
        self.state = state
        self.unit = unit

    def run(self):
        if self.on_ground(self.state, self.unit):
            if self.unit.speed.x <= 0:
                self.unit.rect_collision.size = self.unit.crouch_size
            else:
                self.unit.rect_collision.size = self.unit.slide_size
                self.unit.position.y += self.unit.crouch_size.y - self.unit.slide_size.y

        if self.on_ground(self.state, self.unit):
            if self.unit.speed.x > 0:
                self.unit.speed.x -= .04
            else:
                self.unit.speed.x -= .015

