import pygame
from pygame.math import Vector2

from state import GameState

from .GameMode import GameMode


class PlayGameMode(GameMode):
    def __init__(self):
        self.cell_size = Vector2(16, 16)
        self.game_window = pygame.Surface((240, 160))

        self.layers_count = 2

        self.state = GameState()
        self.layers = [None] * self.layers_count
        self.background = None

    def process_input(self):
        pass

    def update(self):
        pass

    def render(self, window):
        self.game_window.fill((0, 0, 0))

        # TODO: encapsulate to layer class
        if self.background is not None:
            image = pygame.image.load(self.background)
            self.game_window.blit(image, (0, 0))

        for layer in self.layers:
            layer.render(self.game_window)

        pygame.transform.scale(self.game_window, window.get_size(), window)
