import pygame
from pygame.math import Vector2

from command import JumpCommand, MoveCommand
from state import GameState
from layer import UnitLayer

from .GameMode import GameMode


class PlayGameMode(GameMode):
    def __init__(self):
        super().__init__()

        self.cell_size = Vector2(16, 16)
        self.game_window = pygame.Surface((240, 160))

        self.state = GameState()
        self.player = self.state.units[0]

        self.layers = [None] * 3
        self.layers[2] = (UnitLayer(self.cell_size, "assets/herochar_spritesheet.png", self.state))
        self.background = None

        self.commands = []

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.notify_quit_requested()
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.notify_show_pause_requested()
                    break
                elif event.key == pygame.K_UP:
                    command = JumpCommand(self.state, self.player)
                    self.commands.append(command)
        command = MoveCommand(self.state, self.player)
        self.commands.append(command)

    def update(self):
        for command in self.commands:
            command.run()
        self.commands.clear()

    def render(self, window):
        self.game_window.fill((0, 0, 0))

        for layer in self.layers:
            layer.render(self.game_window)

        pygame.transform.scale(self.game_window, window.get_size(), window)
