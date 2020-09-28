import pygame, sys
from pygame import font

''' окно '''


class Menu:
    def __init__(self):
        self.window = pygame.display.set_mode((1600, 900))
        pygame.display.set_caption('Welcom to the club, buddy')
        self.clock = pygame.time.Clock()
        self.running = True

    def render(self):
        self.clock.tick(60)
        self.window.blit(pygame.image.load("background.jpg"), (0, 0))
        text = ["Let's go!", "Settings", "Results", "Achivements", "Check the connection"]
        self.print_button((255, 20, 147), (150, 90, 500, 50), text)

    def print_button(self, color, size, text):
        for i, el in enumerate(text):
            pygame.draw.rect(self.window, color, (150, 90 + (i) * 40 + 20 * i, 500, 40));
            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            text1 = myfont.render(el, True, (0, 0, 0))
            self.window.blit(text1, (300, 90 + (i) * 40 + 20 * i))
        pygame.display.update()

    def catch_action(self):
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 150 <= x <= 650 and 90 <= y <= 140:
                    self.running = False
                    import src.main as g
                    game = g.GameWindow()
                    game.run()
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()

    def run(self):
        while self.running:
            self.render()
            self.catch_action()


pygame.init()
pygame.font.init()
menu = Menu()
menu.run()
