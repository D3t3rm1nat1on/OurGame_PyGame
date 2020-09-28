import pygame, sys
from pygame import font

''' окно '''


class Menu:
    def __init__(self):
        self.window = pygame.display.set_mode((1600, 900))
        pygame.display.set_icon(pygame.image.load("Pandemonica.png"))
        pygame.display.set_caption('Welcom to the club, buddy')
        self.clock = pygame.time.Clock()
        self.running = True
        self.settings = Settings()
        self.num_ren = 0
        self.renders = [self.render0, self.render1]

    def render0(self):
        self.clock.tick(60)
        self.window.blit(pygame.image.load("background.jpg"), (0, 0))
        self.window.blit(pygame.font.SysFont('Comic Sans MS', 30).render('Start menu', True, (0, 0, 0)),
                         (300, 20))
        text = ["Let's go!", "Settings", "Results", "Achievements", "Check the connection"]
        self.print_button((255, 20, 147), (150, 90, 500, 50), text)
        pygame.display.update()

    def render1(self):
        self.clock.tick(60)
        self.window.blit(pygame.image.load("background.jpg"), (0, 0))
        self.window.blit(pygame.font.SysFont('Comic Sans MS', 30).render('Settings', True, (0, 0, 0)),
                         (300, 20))
        self.to_main_menu()
        text = ["Sound:" + str(self.settings.vol ) + "%", "Unlocked themes", "Change connection"]
        self.print_button((255, 20, 147), (150, 90, 500, 50), text)
        self.print_vol_change((255, 20, 147))
        pygame.display.update()

    def print_vol_change(self, color):
        pygame.draw.rect(self.window, color, (110, 90, 30, 40))
        self.window.blit(pygame.font.SysFont('Comic Sans MS', 30).render('-', True, (0, 0, 0)),
                         (120, 85))
        pygame.draw.rect(self.window, color, (660, 90, 30, 40))
        self.window.blit(pygame.font.SysFont('Comic Sans MS', 30).render('+', True, (0, 0, 0)),
                         (670, 85))

    def to_main_menu(self):
        pygame.draw.rect(self.window, (255, 20, 147), (0, 0, 190, 40))
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text1 = font.render('To main menu', True, (0, 0, 0))
        self.window.blit(text1, (0, 0))

    def print_button(self, color, size, text):
        for i, el in enumerate(text):
            pygame.draw.rect(self.window, color, (150, 90 + i * 40 + 20 * i, 500, 40))
            font1 = pygame.font.SysFont('Comic Sans MS', 30)
            text1 = font1.render(el, True, (0, 0, 0))
            self.window.blit(text1, (300, 90 + i * 40 + 20 * i))

    def catch_action(self):
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.num_ren == 0 and 150 <= x <= 650 and 90 <= y <= 130:
                    self.running = False
                    import src.main as g
                    game = g.GameWindow()
                    game.run()
                if self.num_ren == 0 and 150 <= x <= 650 and 150 <= y <= 190:
                    self.num_ren = 1
                if self.num_ren != 0 and 0 <= x <= 190 and 0 <= y <= 40:
                    self.num_ren = 0
                if self.num_ren == 1 and 110 <= x <= 150 and 90 <= y <= 130:
                    self.settings.lower_sound()
                if self.num_ren == 1 and 660 <= x <= 700 and 90 <= y <= 130:
                    self.settings.louder_sound()
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()

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
            pygame.mixer.music.set_volume(self.vol/100.0)

    def louder_sound(self):
        if self.vol < 100:
            self.vol += 10
            pygame.mixer.music.set_volume(self.vol/100.0)

    def play_music(self, volume):
        self.vol = volume
        pygame.mixer.music.load('song.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.vol / 100.0)


pygame.init()
pygame.font.init()
menu = Menu()

menu.run()
