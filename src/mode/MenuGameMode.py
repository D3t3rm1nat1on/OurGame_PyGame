import json
from collections import namedtuple

import pygame

from pygame.math import Vector2

from layer import Layer
from .GameMode import GameMode
from .MenuFuctionalMode import MenuFunctional, Sound


class MenuGameMode(GameMode, MenuFunctional):
    def __init__(self):
        super().__init__()
        self.old_x, self.old_y = 0, 0
        self.ind = -1
        self.settings = Sound()
        self.num_ren = 0
        self.data = []
        self.text_theme = [
            [self.color[self.theme][0], (150, 90, 500, 40), "Shine like a princess", (300, 90), False, -1, True, 0],
            # тема, координаты прямоуг., название, коор. текста, выделение кнопки, переход в другой рендер,
            # доступна ли, номер темы
            [self.color[self.theme][0], (150, 150, 500, 40), "Toxic frogs", (300, 150), False, -1, True, 1],
            [self.color[self.theme][0], (150, 210, 500, 40), "Back", (300, 210), False, 1, False]
        ]
        self.text = [
            [self.color[self.theme][0], (150, 90, 500, 40), "Let's go!", (300, 90), False, 140800],
            [self.color[self.theme][0], (150, 150, 500, 40), "Settings", (300, 150), False, 1],
            [self.color[self.theme][0], (150, 210, 500, 40), "Results", (300, 210), False, 2],
            [self.color[self.theme][0], (150, 270, 500, 40), "Shop", (300, 270), False, 4],
            [self.color[self.theme][0], (150, 330, 500, 40), "Exit", (300, 330), False, 177013]
        ]
        self.text_settings = [
            [self.color[self.theme][0], (150, 90, 500, 40), "Sound:" + str(self.settings.vol) + "%", (300, 90), False,
             -1],
            [self.color[self.theme][0], (150, 150, 500, 40), "Unlocked themes", (300, 150), False, 5],
            [self.color[self.theme][0], (150, 210, 500, 40), "To main menu", (300, 210), False, 0],
            [self.color[self.theme][0], (110, 90, 30, 40), "-", (120, 85), False, -1],
            [self.color[self.theme][0], (660, 90, 30, 40), "+", (670, 85), False, -1]
        ]
        self.results = [
            [self.color[self.theme][0], (150, 400, 500, 40), "To main menu", (300, 400), False, 0]
        ]

        self.shop = [
            [self.color[self.theme][0], (1250, 90, 230, 40), "", (1300, 90), False, -1, False],
            [self.color[self.theme][0], (1250, 150, 230, 40), "", (1300, 150), False, -1, False],
            [self.color[self.theme][0], (1250, 210, 230, 40), "", (1300, 210), False, -1, False],
            [self.color[self.theme][0], (500, 270, 500, 40), "Back", (700, 270), False, 0, False]

        ]
        self.lists = [self.text, self.text_settings, self.results, 3, self.shop, self.text_theme]
        self.renders = [self.render0, self.render1, self.render2, 3, self.render4, self.render5]

    def process_input(self):
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                self.old_x, self.old_y = x, y
                self.move_pointer(event, self.lists[self.num_ren], 1)
                if event.key == pygame.K_RETURN:
                    if self.ind == 0 and self.lists[self.num_ren][self.ind][5] == 140800:
                        self.notify_show_perk_requested()
                        # self.notify_load_level_requested()
                    if self.ind != -1 and self.lists[self.num_ren][self.ind][5] != -1:
                        self.lists[self.num_ren][self.ind][4] = False
                        self.num_ren = self.lists[self.num_ren][self.ind][5]
                        self.ind = -1
                    if self.num_ren == 1 and self.ind == 3:
                        self.settings.lower_sound()
                    if self.num_ren == 1 and self.ind == 4:
                        self.settings.louder_sound()
                    if self.num_ren == 5 and self.ind != 2:
                        self.change_theme(self.text_theme[self.ind][3][0], self.text_theme[self.ind][3][1])
                    if self.num_ren == 4:
                        self.buy_perk()
                elif event.key == pygame.K_ESCAPE:
                    self.notify_quit_requested()
            elif self.old_y != y or self.old_x != x:
                self.ind = -1
                self.chosen_button(x, y, self.lists[self.num_ren])

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.num_ren == 0 and 150 <= x <= 650 and 90 <= y <= 130:
                    self.notify_show_perk_requested()
                    # self.notify_load_level_requested()
                if self.num_ren == 0:
                    self.into_new_render(x, y, self.text)
                else:
                    if self.num_ren == 1:
                        self.into_new_render(x, y, self.text_settings)
                    else:
                        if self.num_ren == 2:
                            self.into_new_render(x, y, self.results)
                        else:
                            if self.num_ren == 5:
                                self.into_new_render(x, y, self.text_theme)
                                self.change_theme(x, y)
                            elif self.num_ren == 4:
                                self.into_new_render(x, y, self.shop)
                                self.convert_position_in_ind(x, y)

                if self.num_ren == 1 and 110 <= x <= 150 and 90 <= y <= 130:
                    self.settings.lower_sound()
                if self.num_ren == 1 and 660 <= x <= 700 and 90 <= y <= 130:
                    self.settings.louder_sound()
            if event.type == pygame.QUIT or self.num_ren == 177013:
                self.notify_quit_requested()

    def update(self):
        pass

    def render(self, window):
        for j, function in enumerate(self.renders):
            if j == self.num_ren:
                function(window)

    def render0(self, window):
        window.blit(
            pygame.font.SysFont('Comic Sans MS', 30).render('Start menu', True, (0, 0, 0)),
            (300, 20))
        self.print_button(window, self.text)
        for el in self.text:
            if el[4]:
                self.draw_frame(window, el[1][0], el[1][1], el[1][2], el[1][3])
        # Layer(Vector2(16, 16), "assets/units_spritesheet.png").render_tile(window, Vector2(47, 31),
        #                                                                    Vector2(2, 5),
        #                                                                    Vector2(0.5, 0.5))

    def render1(self, window):
        window.blit(
            pygame.font.SysFont('Comic Sans MS', 30).render('Settings', True, (0, 0, 0)),
            (300, 20))
        self.text_settings[0][2] = "Sound:" + str(self.settings.vol) + "%"
        self.print_button(window, self.text_settings)
        for el in self.text_settings:
            if el[4]:
                self.draw_frame(window, el[1][0], el[1][1], el[1][2], el[1][3])

    def render2(self, window):
        window.blit(
            pygame.font.SysFont('Comic Sans MS', 30).render('Results', True, (0, 0, 0)),
            (200, 20))
        with open('results.txt', 'r') as f:
            nums = f.read().splitlines()
        window.blit(
            pygame.font.SysFont('Comic Sans MS', 30).render('Your best score: ', True, (0, 0, 0)),
            (50, 60))
        for i, el in enumerate(nums):
            temp = str(el).split()
            window.blit(
                pygame.font.SysFont('Comic Sans MS', 30).render(temp[2], True, (0, 0, 0)),
                (300, 60 + 30 * i))
            window.blit(
                pygame.font.SysFont('Comic Sans MS', 30).render(temp[1], True, (0, 0, 0)),
                (500, 60 + 30 * i))
        self.print_button(window, self.results)
        for el in self.results:
            if el[4]:
                self.draw_frame(window, el[1][0], el[1][1], el[1][2], el[1][3])

    def render4(self, window):
        window.blit(
            pygame.font.SysFont('Comic Sans MS', 30).render("Ho-ho. I see u wanna spend money", True, (0, 0, 0)),
            (500, 20))
        with open('money.txt', 'r') as f:
            money = int(f.read())
        window.blit(
            pygame.font.SysFont('Comic Sans MS', 30).render("In your wallet: " + str(money), True, (0, 0, 0)),
                                                        (1200, 40))
        with open("perks.json", "r") as read_file:
            h = read_file.read()
        self.data = json.loads(h)
        for el in self.data:
            window.blit(pygame.font.SysFont('Comic Sans MS', 30).render(el['perk'], True, (0, 0, 0)),
                        el['perk_position'])
            window.blit(pygame.font.SysFont('Comic Sans MS', 30).render(el['description'], True, (0, 0, 0)),
                        el['desc_position'])
        self.check_perk_status()
        self.print_button(window, self.shop)
        for el in self.shop:
            if el[4]:
                self.draw_frame(window, el[1][0], el[1][1], el[1][2], el[1][3])
        self.render_icons(window)

    def check_perk_status(self):
        for j, availability in enumerate(self.data):
            if availability['availability']:
                self.shop[j][2] = "Available"
                self.shop[j][6] = True
            else:
                self.shop[j][2] = "Buy for " + str(availability['price'])

    def convert_position_in_ind(self, x, y):
        for i, el in enumerate(self.shop):
            if el[1][0] <= x <= (el[1][0] + el[1][2]) and el[1][1] <= y <= (el[1][3] + el[1][1]):
                self.ind = i
                self.buy_perk()
                break

    def buy_perk(self):
        if self.shop[self.ind][5] == -1 and not self.shop[self.ind][6]:
            with open('money.txt', 'r') as f:
                money = int(f.read())
            if money >= self.data[self.ind]['price']:
                money -= self.data[self.ind]['price']
                self.data[self.ind]['availability'] = True
                self.shop[self.ind][6] = True
                r = json.dumps(self.data)
                with open('perks.json', 'w') as f:
                    f.write(r)
                with open('money.txt', 'w') as f:
                    f.write(str(money))

    def render5(self, window):
        window.blit(pygame.font.SysFont('Comic Sans MS', 30).render('Themes', True, (0, 0, 0)),
                    (300, 20))
        self.print_button(window, self.text_theme)
        for el in self.text_theme:
            if el[4]:
                self.draw_frame(window, el[1][0], el[1][1], el[1][2], el[1][3])

    def change_theme(self, x, y):
        for el in self.text_theme:
            if el[1][0] <= x <= (el[1][0] + el[1][2]) and el[1][1] <= y <= (el[1][3] + el[1][1]):
                if el[6]:
                    MenuFunctional.theme = el[7]

    def button_soung(self, ev):
        if self.text_settings[0][4]:
            if ev.key == pygame.K_RIGHT:
                self.text_settings[4][4] = True
                self.text_settings[0][4] = False
                self.ind = 4
                return
            if ev.key == pygame.K_LEFT:
                self.text_settings[3][4] = True
                self.text_settings[0][4] = False
                self.ind = 3
                return
        if self.text_settings[4][4]:
            if ev.key == pygame.K_LEFT:
                self.text_settings[0][4] = True
                self.text_settings[4][4] = False
                self.ind = 0
                return
        if self.text_settings[3][4]:
            if ev.key == pygame.K_RIGHT:
                self.text_settings[0][4] = True
                self.text_settings[3][4] = False
                self.ind = 0
                return
