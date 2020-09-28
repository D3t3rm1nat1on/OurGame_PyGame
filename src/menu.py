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
            start_button = pygame.draw.rect(self.window, (255, 20, 147), (150, 90, 500, 50));
            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            text = myfont.render('Start game', False, (0, 0, 0))
            self.window.blit(text, (300, 90))
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
        self.render()
        while self.running:
            self.catch_action()


pygame.init()
pygame.font.init()
menu = Menu()
menu.run()
