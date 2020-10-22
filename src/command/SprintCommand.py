from .Command import Command
from src.state import Player


class SprintCommand(Command):
    player: Player

    def __init__(self, state, player):
        self.state = state
        self.player = player

    def run(self):
        self.player.is_sprinting = True
