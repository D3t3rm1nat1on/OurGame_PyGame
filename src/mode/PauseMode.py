import pygame

from mode.GameMode import GameMode
from mode.MenuFuctionalMode import MenuFunctional


class PauseMode(GameMode, MenuFunctional):
    def __init__(self):
        super().__init__()
        self.text = [
            [self.color[self.theme][0], (150, 90, 500, 40), "Continue", (300, 90), False],
            [self.color[self.theme][0], (150, 150, 500, 40), "To main menu", (300, 150), False]
        ]

    def process_input(self):
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.notify_show_game_requested()
                self.old_x, self.old_y = x, y
                self.m(event)
                #if event.key == pygame.K_RETURN:
                # if self.num_ren == 0 and 150 <= x <= 650 and 90 <= y <= 130:
                #     self.notify_load_level_requested()
    def m (self, ev):
        cur_list = self.text
        if self.ind > 0:
            if ev.key == pygame.K_UP:
                self.ind -= 1
                cur_list[self.ind + 1][4] = False
                cur_list[self.ind][4] = True
        if self.ind < len(cur_list) - 1:
            if self.num_ren == 1 and self.ind == 2:
                return
            if ev.key == pygame.K_DOWN:
                self.ind += 1
                if self.ind != 0:
                    cur_list[self.ind - 1][4] = False
                cur_list[self.ind][4] = True
                    # self.show_game_requested()
        #  if event.type == pygame.MOUSEBUTTONDOWN:

    def update(self):
        pass

    def render(self, window):
        pygame.draw.rect(window, (0, 0, 0), (120, 80, 510, 90))
        self.print_button(window, self.text)
        for el in self.text:
            if el[4]:
                self.draw_frame(window, el[1][0], el[1][1], el[1][2], el[1][3])
