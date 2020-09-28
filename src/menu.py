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
        pygame.display.update()

    def print_button(self, color, size, text):
        for i, el in enumerate(text):
            pygame.draw.rect(self.window, color, (150, 90 + i * 40 + 20 * i, 500, 40));
            font1 = pygame.font.SysFont('Comic Sans MS', 30)
            text1 = font1.render(el, True, (0, 0, 0))
            self.window.blit(text1, (300, 90 + i * 40 + 20 * i))
        pygame.display.update()

    def catch_action(self):
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 150 <= x <= 650 and 90 <= y <= 130:
                    self.running = False
                    import src.main as g
                    game = g.GameWindow()
                    game.run()
                if 150 <= x <= 650 and 150 <= y <= 190:
                    self.num_ren = 1;
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()

    def play_music(self):
            pygame.mixer.music.load('song.mp3')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.2)

    def run(self):
        self.play_music()
        while self.running:
            for j, function in enumerate(self.renders):
                if j == self.num_ren:
                    function()
            self.catch_action()


pygame.init()
pygame.font.init()
menu = Menu()

menu.run()
