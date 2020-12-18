import json

from mode.GameMode import GameMode
from mode.MenuFuctionalMode import MenuFunctional


class ChosePerkMode(GameMode, MenuFunctional):
    def __init__(self):
        super().__init__()
        self.data = []
        self.buttons = [

        ]

    def process_input(self):
        pass

    def update(self):
        pass

    def render(self, window):
        with open("perks.json", "r") as read_file:
            h = read_file.read()
        self.data = json.loads(h)