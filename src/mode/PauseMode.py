import pygame

from mode.GameMode import GameMode


class PauseMode(GameMode):
    def __init__(self):
        self.color = [
            [(255, 20, 147), (176, 255, 46)],
            [(176, 255, 46), (255, 20, 147)]]
        self.theme = 0
        self.text = [
            [self.color[self.theme][0], (150, 90, 500, 40), "Continue", (300, 90), False],
            [self.color[self.theme][0], (150, 150, 500, 40), "Settings", (300, 150), False],
            [self.color[self.theme][0], (150, 210, 500, 40), "Results", (300, 210), False],
            [self.color[self.theme][0], (150, 270, 500, 40), "Achievements", (300, 270), False]
        ]


    def process_input(self):
        pass

    def update(self):
        pass

    def render(self, window):
        pygame.draw.rect(window,(0,0,0), (60, 600, 50, 100))
