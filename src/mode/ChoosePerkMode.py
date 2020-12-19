import json

import pygame

from mode.GameMode import GameMode
from mode.MenuFuctionalMode import MenuFunctional
from state.GameState import GameState


class ChoosePerkMode(GameMode, MenuFunctional):
    def __init__(self):
        super().__init__()
        self.data = []
        self.buttons = []
        self.ind = -1
        self.old_x, self.old_y = 0, 0
        self.add_available_perks()

    def process_input(self):
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.notify_show_game_requested()
                self.old_x, self.old_y = x, y
                self.move_pointer(event, self.buttons, 2)
                if event.key == pygame.K_RETURN:
                    if self.buttons[self.ind][5] == 178908:
                        self.notify_show_game_requested()
                    else:
                        GameState.active_perk = self.ind
            elif self.old_y != y or self.old_x != x:
                self.ind = -1
                self.chosen_button(x, y, self.buttons)

            if event.type == pygame.MOUSEBUTTONDOWN:
                for el in self.buttons:
                    if el[1][0] <= x <= (el[1][0] + el[1][2]) and el[1][1] <= y <= (el[1][3] + el[1][1]):
                        if el[5] == 178908:
                            self.notify_show_game_requested()
                        else:
                            GameState.active_perk = el[5]
            print(GameState.active_perk)
            if event.type == pygame.QUIT:
                self.notify_quit_requested()

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
                pygame.font.SysFont('Comic Sans MS', 30).render("You haven't bought any perk yet", True, (0, 0, 0)),
                (170, 90))
        self.print_button(window, self.buttons)
        for el in self.buttons:
            if el[4]:
                self.draw_frame(window, el[1][0], el[1][1], el[1][2], el[1][3])

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
                [self.color[self.theme][0], (150, 90 + 60 * (i+1), 500, 40), "Continue", (260, 90 + 60 * (i+1)), False, 178908])
