import pygame
from pygame.math import Vector2

from state import GameState
from layer import UnitLayer

from .GameMode import GameMode


class PlayGameMode(GameMode):
    def __init__(self):
        super().__init__()

        self.cell_size = Vector2(16, 16)
        self.game_window = pygame.Surface((240, 160))

        self.state = GameState()
        self.layers = [None] * 3
        self.layers[2] = (UnitLayer(self.cell_size, "assets/herochar_run_anim_strip_6.png", self.state))
        self.background = None

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.notify_quit_requested()
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.notify_quit_requested()
                    break

    def update(self):
        pass

    def render(self, window):
        self.game_window.fill((0, 0, 0))

        for layer in self.layers:
            layer.render(self.game_window)

        pygame.transform.scale(self.game_window, window.get_size(), window)
