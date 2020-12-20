import pygame
import time

from mode.GameMode import GameMode


class EndGameMode(GameMode):
    def __init__(self):
        super().__init__()
        self.end_game = [
            ["Game Over", [500, 90]],
            ["Thank you for downloading OurGame_PyGame game.", [500, 150]],
            ["We hope, you were able to get pleasure.", [500, 210]],
            ["Team of developers: Ann, Andrew, Artyom.", [500, 270]],
            ["Assets by:  X", [500, 330]]
        ]

    def process_input(self):
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.notify_show_menu_requested()
            if event.type == pygame.QUIT:
                self.notify_quit_requested()

    def update(self):
        pass

    def render(self, window):
        for el in self.end_game:
            window.blit(
                pygame.font.SysFont('Comic Sans MS', 30).render(el[0], True, (0, 0, 0)),
                el[1])
            el[1][1] -= 20
        window.blit(
            pygame.font.SysFont('Comic Sans MS', 30).render("Press Space to go to Main menu", True, (0, 0, 0)),
            (500, 600))
        time.sleep(1)
