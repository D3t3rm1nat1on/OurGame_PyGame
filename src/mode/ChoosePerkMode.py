import json

import pygame

from mode.GameMode import GameMode
from mode.MenuFuctionalMode import MenuFunctional


class ChoosePerkMode(GameMode, MenuFunctional):
    def __init__(self):
        super().__init__()
        self.data = []
        self.buttons = []
        self.add_available_perks()

    def process_input(self):
        pass

    def update(self):
        pass

    def render(self, window):
        window.blit(
            pygame.font.SysFont('Comic Sans MS', 30).render("Choose perk to begin", True, (0, 0, 0)),
            (300, 20))
        if len(self.buttons) > 1:
            pygame.draw.rect(window, (0, 0, 0), (120, 80, 510, 90 + 45 * (len(self.buttons) - 2)))
        else:
            window.blit(
                pygame.font.SysFont('Comic Sans MS', 30).render("You haven't bought any perk yet", True, (0,0,0)),
                (170, 90))
        self.print_button(window, self.buttons)

    def add_available_perks(self):
        with open("perks.json", "r") as read_file:
            h = read_file.read()
        self.data = json.loads(h)
        for j, perk in enumerate(self.data):
            i = len(self.buttons)
            if perk['availability']:
                self.buttons.append(
                    [self.color[self.theme][0], (150, 90 + 60 * i, 500, 40), perk['perk'], (260, 90 + 60 * i), False,
                     j])
        if len(self.buttons) == 0:
            self.buttons.append(
                [self.color[self.theme][0], (150, 90 + 60, 500, 40), "Continue", (260, 90 + 60), False, 178908])
        else:
            self.buttons.append(
                [self.color[self.theme][0], (150, 90 + 60 * i, 500, 40), "Continue", (260, 90 + 60 * i), False, 178908])
