import pygame

from mode import GameModeObserver, PlayGameMode, MenuGameMode
from setup import LoadLevel


class UserInterface(GameModeObserver):
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1500, 960))
        pygame.display.set_caption("Our Game")
        pygame.display.set_icon(pygame.image.load("assets/Pandemonica.png"))

        # self.game = PlayGameMode()
        # self.game.add_observer(self)
        # LoadLevel("assets/sample_map.tmx", self.game).run()

        self.menu = MenuGameMode()
        self.menu.add_observer(self)

        self.clock = pygame.time.Clock()
        self.running = True

    def quit_requested(self):
        self.running = False

    def run(self):
        while self.running:
            self.menu.process_input()
            self.menu.render(self.window)
            # self.game.process_input()
            # self.game.render(self.window)
            pygame.display.update()
            self.clock.tick(60)


UI = UserInterface()
UI.run()

pygame.quit()
