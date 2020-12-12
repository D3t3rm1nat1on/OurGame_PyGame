import pygame

from mode.GameMode import GameMode
from mode.MenuFuctionalMode import MenuFunctional


class PauseMode(GameMode, MenuFunctional):
    def __init__(self):
        super().__init__()
        self.ind = -1
        self.old_x, self.old_y = 0, 0
        self.text = [
            [self.color[self.theme][0], (150, 90, 500, 40), "Continue", (300, 90), False, self.notify_show_game_requested],
            [self.color[self.theme][0], (150, 150, 500, 40), "To main menu", (300, 150), False, self.notify_show_menu_requested]
        ]

    def process_input(self):
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.notify_show_game_requested()
                self.old_x, self.old_y = x, y
                self.move_pointer(event, self.text, 2)
                if event.key == pygame.K_RETURN:
                    if self.ind == 0:
                        self.notify_show_game_requested()
                    else:
                        self.notify_show_menu_requested()
            elif self.old_y != y or self.old_x != x:
                self.ind = -1
                self.chosen_button(x, y, self.text)

            if event.type == pygame.MOUSEBUTTONDOWN:
                for el in self.text:
                    if el[1][0] <= x <= (el[1][0] + el[1][2]) and el[1][1] <= y <= (el[1][3] + el[1][1]):
                        el[5]()


    def update(self):
        pass

    def render(self, window):
        pygame.draw.rect(window, (0, 0, 0), (120, 80, 510, 90))
        self.print_button(window, self.text)
        for el in self.text:
            if el[4]:
                self.draw_frame(window, el[1][0], el[1][1], el[1][2], el[1][3])
