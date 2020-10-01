import pygame, sys
from pygame import font


class Menu:
    def __init__(self):
        self.window = pygame.display.set_mode((1600, 900))
        pygame.display.set_icon(pygame.image.load("Pandemonica.png"))
        pygame.display.set_caption('Welcome to the club, buddy')
        self.clock = pygame.time.Clock()
        self.running = True
        self.settings = Settings()
        self.text = [
            [(255, 20, 147), (150, 90, 500, 40), "Let's go!", (300, 90), False],
            [(255, 20, 147), (150, 150, 500, 40), "Settings", (300, 150), False, 1],
            [(255, 20, 147), (150, 210, 500, 40), "Results", (300, 210), False, 2],
            [(255, 20, 147), (150, 270, 500, 40), "Achievements", (300, 270), False, 3],
            [(255, 20, 147), (150, 330, 500, 40), "Check the connection", (300, 330), False, 4]]

        self.text_settings = [
            [(255, 20, 147), (150, 90, 500, 40), "Sound:" + str(self.settings.vol) + "%", (300, 90), False],
            [(255, 20, 147), (150, 150, 500, 40), "Unlocked themes", (300, 150), False],
            [(255, 20, 147), (150, 210, 500, 40), "Change connection", (300, 210), False],
            [(255, 20, 147), (0, 0, 190, 40), 'To main menu', (0, 0), False],
            [(255, 20, 147), (110, 90, 30, 40), '-', (120, 85), False],
            [(255, 20, 147), (660, 90, 30, 40), '+', (670, 85), False]]

        self.num_ren = 0
        self.renders = [self.render0, self.render1]

    def button(self, color_rect, coordinates, text, start_text):
        pygame.draw.rect(self.window, color_rect, coordinates)
        self.window.blit(pygame.font.SysFont('Comic Sans MS', 30).render(text, True, (0, 0, 0)),
                         start_text)

    def render0(self):
        self.clock.tick(60)
        self.window.blit(pygame.image.load("background.jpg"), (0, 0))
        self.window.blit(pygame.font.SysFont('Comic Sans MS', 30).render('Start menu', True, (0, 0, 0)),
                         (300, 20))
        self.print_button(self.text)
        for el in self.text:
            if el[4]:
                self.draw_frame(el[1][0], el[1][1], el[1][2], el[1][3])
        pygame.display.update()

    def render1(self):
        self.clock.tick(60)
        self.window.blit(pygame.image.load("background.jpg"), (0, 0))
        self.window.blit(pygame.font.SysFont('Comic Sans MS', 30).render('Settings', True, (0, 0, 0)),
                         (300, 20))
        self.text_settings[0][2] = "Sound:" + str(self.settings.vol) + "%"
        self.print_button(self.text_settings)
        for el in self.text_settings:
            if el[4]:
                self.draw_frame(el[1][0], el[1][1], el[1][2], el[1][3])
        pygame.display.update()

    def print_button(self, text):
        for i, el in enumerate(text):
            self.button(el[0], el[1], el[2], el[3])

    def catch_action(self):
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if self.num_ren == 0:
                self.chosen_button(x, y, self.text)
            if self.num_ren == 1:
                self.chosen_button(x, y, self.text_settings)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.num_ren == 0 and 150 <= x <= 650 and 90 <= y <= 130:
                    self.running = False
                    import src.main as g
                    game = g.GameWindow()
                    game.run()
                self.into_new_render(x, y)
                if self.num_ren == 1 and 110 <= x <= 150 and 90 <= y <= 130:
                    self.settings.lower_sound()
                if self.num_ren == 1 and 660 <= x <= 700 and 90 <= y <= 130:
                    self.settings.louder_sound()
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()

    def chosen_button(self, x, y, temp):
        for el in temp:
            if el[1][0] <= x <= (el[1][0] + el[1][2]) and el[1][1] <= y <= (el[1][3] + el[1][1]):
                el[4] = True
            else:
                el[4] = False

    def into_new_render(self, x, y):
        for el in self.text:
            if self.num_ren == 0 and el[1][0] <= x <= (el[1][0] + el[1][2]) and el[1][1] <= y <= (el[1][3] + el[1][1]):
                self.num_ren = el[5]
        if self.num_ren != 0 and 0 <= x <= 190 and 0 <= y <= 40:
            self.num_ren = 0

    def draw_frame(self, x, y, lx, ly):
        wildth = 5
        pygame.draw.line(self.window, (176, 255, 46), (x, y), (x + lx, y), wildth)
        pygame.draw.line(self.window, (176, 255, 46), (x, y), (x, y + ly), wildth)
        pygame.draw.line(self.window, (176, 255, 46), (x, y + ly), (x + lx, y + ly), wildth)
        pygame.draw.line(self.window, (176, 255, 46), (x + lx, y), (x + lx, y + ly), wildth)

    def run(self):

        while self.running:
            for j, function in enumerate(self.renders):
                if j == self.num_ren:
                    function()
            self.catch_action()


class Settings:
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
        pygame.mixer.music.load('song.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.vol / 100.0)


pygame.init()
pygame.font.init()
menu = Menu()
menu.run()
