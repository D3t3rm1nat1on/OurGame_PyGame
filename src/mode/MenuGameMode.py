import pygame

from .GameMode import GameMode


class MenuGameMode(GameMode):
    def __init__(self):
        super().__init__()
        self.theme = 0
        self.old_x, self.old_y = 0, 0
        self.ind = -1
        self.color = [
            [(255, 20, 147), (176, 255, 46)],
            [(176, 255, 46), (255, 20, 147)]]
        self.settings = Sound()
        self.text_theme = [
            [self.color[self.theme][0], (150, 90, 500, 40), "Shine like a princess", (300, 90), False, -1, True, 0],
            # тема, координаты прямоуг., название, коор. текста, выделение кнопки, переход в другой рендер, доступна ли, номер темы
            [self.color[self.theme][0], (150, 150, 500, 40), "Toxic frogs", (300, 150), False, -1, True, 1],
            [self.color[self.theme][0], (150, 210, 500, 40), 'Back', (300, 210), False, 1, False]
        ]
        self.text = [
            [self.color[self.theme][0], (150, 90, 500, 40), "Let's go!", (300, 90), False, 140800],
            [self.color[self.theme][0], (150, 150, 500, 40), "Settings", (300, 150), False, 1],
            [self.color[self.theme][0], (150, 210, 500, 40), "Results", (300, 210), False, 2],
            [self.color[self.theme][0], (150, 270, 500, 40), "Achievements", (300, 270), False, 3]]

        self.text_settings = [
            [self.color[self.theme][0], (150, 90, 500, 40), "Sound:" + str(self.settings.vol) + "%", (300, 90), False,
             -1],
            [self.color[self.theme][0], (150, 150, 500, 40), "Unlocked themes", (300, 150), False, 5],
            [self.color[self.theme][0], (150, 270, 500, 40), 'To main menu', (300, 270), False, 0],
            [self.color[self.theme][0], (110, 90, 30, 40), '-', (120, 85), False, -1],
            [self.color[self.theme][0], (660, 90, 30, 40), '+', (670, 85), False, -1]]
        self.results = [
            [self.color[self.theme][0], (150, 400, 500, 40), 'To main menu', (300, 400), False, 0]
        ]
        self.num_ren = 0
        self.lists = [self.text, self.text_settings, self.results, 3, 4, self.text_theme]
        self.renders = [self.render0, self.render1, self.render2, 3, 4, self.render5]

    def process_input(self):
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                self.old_x, self.old_y = x, y
                self.move_pointer(event)
                if event.key == pygame.K_RETURN:
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
            elif self.old_y != y or self.old_x != x:
                self.ind = -1
                self.chosen_button(x, y, self.lists[self.num_ren])

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.num_ren == 0 and 150 <= x <= 650 and 90 <= y <= 130:
                    self.notify_quit_requested()
                # game = g.GameWindow()
                # game.run()
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

                if self.num_ren == 1 and 110 <= x <= 150 and 90 <= y <= 130:
                    self.settings.lower_sound()
                if self.num_ren == 1 and 660 <= x <= 700 and 90 <= y <= 130:
                    self.settings.louder_sound()
            if event.type == pygame.QUIT:
                self.notify_quit_requested()

    def update(self):
        pass

    def render(self, window):
        for j, function in enumerate(self.renders):
            if j == self.num_ren:
                function(window)

    def render0(self, window):
        window.blit(pygame.image.load("assets/menu_background.jpg"), (0, 0))
        window.blit(
            pygame.font.SysFont('Comic Sans MS', 30).render('Start menu', True, (0, 0, 0)),
            (300, 20))
        self.print_button(window, self.text)
        for el in self.text:
            if el[4]:
                self.draw_frame(window, el[1][0], el[1][1], el[1][2], el[1][3])

    def render1(self, window):
        window.blit(pygame.image.load("assets/menu_background.jpg"), (0, 0))
        window.blit(
            pygame.font.SysFont('Comic Sans MS', 30).render('Settings', True, (0, 0, 0)),
            (300, 20))
        self.text_settings[0][2] = "Sound:" + str(self.settings.vol) + "%"
        self.print_button(window, self.text_settings)
        for el in self.text_settings:
            if el[4]:
                self.draw_frame(window, el[1][0], el[1][1], el[1][2], el[1][3])

    def render2(self, window):
        window.blit(pygame.image.load("assets/menu_background.jpg"), (0, 0))
        window.blit(
            pygame.font.SysFont('Comic Sans MS', 30).render('Results', True, (0, 0, 0)),
            (200, 20))
        with open('src/results.txt', 'r') as f:
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

    def render5(self, window):
        window.blit(pygame.image.load("assets/menu_background.jpg"), (0, 0))
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
                    self.theme = el[7]
                    # self.render5()  TODO

    def move_pointer(self, ev):
        cur_list = self.lists[self.num_ren]
        if self.num_ren == 1 and (ev.key == pygame.K_RIGHT or ev.key == pygame.K_LEFT):
            self.button_soung(ev)
            return
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

    def chosen_button(self, x, y, temp):
        for el in temp:
            if el[1][0] <= x <= (el[1][0] + el[1][2]) and el[1][1] <= y <= (el[1][3] + el[1][1]):
                el[4] = True
            else:
                el[4] = False

    def into_new_render(self, x, y, text):
        for el in text:
            if el[1][0] <= x <= (el[1][0] + el[1][2]) and el[1][1] <= y <= (el[1][3] + el[1][1]) and el[5] != -1:
                self.num_ren = el[5]

    def draw_frame(self, window, x, y, lx, ly):
        wildth = 5
        pygame.draw.line(window, self.color[self.theme][1], (x, y), (x + lx, y), wildth)
        pygame.draw.line(window, self.color[self.theme][1], (x, y), (x, y + ly), wildth)
        pygame.draw.line(window, self.color[self.theme][1], (x, y + ly), (x + lx, y + ly), wildth)
        pygame.draw.line(window, self.color[self.theme][1], (x + lx, y), (x + lx, y + ly), wildth)

    def button(self, window, color_rect, coordinates, text, start_text):
        color_rect = self.color[self.theme][0]
        pygame.draw.rect(window, color_rect, coordinates)
        window.blit(pygame.font.SysFont('Comic Sans MS', 30).render(text, True, (0, 0, 0)),
                    start_text)

    def print_button(self, window, text):
        for i, el in enumerate(text):
            self.button(window, el[0], el[1], el[2], el[3])


class Sound:
    def __init__(self):
        self.vol = 10
        self.play_music(self.vol)

    def lower_sound(self):
        if self.vol > 0:
            self.vol -= 10
            pygame.mixer.music.set_volume(self.vol / 100.0)

    def louder_sound(self):
        if self.vol < 100:
            self.vol += 10
            pygame.mixer.music.set_volume(self.vol / 100.0)

    def play_music(self, volume):
        self.vol = volume
        pygame.mixer.music.load('assets/song.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.vol / 100.0)
