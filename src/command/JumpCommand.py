from .Command import Command


class JumpCommand(Command):
    def __init__(self, state, unit):
        self.state = state
        self.unit = unit
