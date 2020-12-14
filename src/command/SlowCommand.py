from state import Unit

from .Command import Command


class SlowCommand(Command):
    unit: Unit

    def __init__(self, state, unit):
        super().__init__()
        self.state = state
        self.unit = unit

    def run(self):
        if self.on_ground(self.state, self.unit):
            self.unit.speed.x -= .003
