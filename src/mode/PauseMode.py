from mode.GameMode import GameMode


class PauseMode(GameMode):
    def __init__(self):
        self.text = [
            [self.color[self.theme][0], (150, 90, 500, 40), "Continue", (300, 90), False],
            [self.color[self.theme][0], (150, 150, 500, 40), "Settings", (300, 150), False],
            [self.color[self.theme][0], (150, 210, 500, 40), "Results", (300, 210), False],
            [self.color[self.theme][0], (150, 270, 500, 40), "Achievements", (300, 270), False]
        ]


    def process_input(self):
        raise NotImplementedError()

    def update(self):
        raise NotImplementedError()

    def render(self, window):
        raise NotImplementedError()
