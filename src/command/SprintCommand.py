from .Command import Command
from src.state import Player


class SprintCommand(Command):
    player: Player

    def __init__(self, state, player):
        super().__init__()
        self.state = state
        self.player = player

    def run(self):
        self.player.is_sprinting = True
        if self.player.is_sprinting and not self.player.is_crouching and self.player.stamina >= 0.5 and self.on_ground(self.state, self.player):
            self.player.sprint()


