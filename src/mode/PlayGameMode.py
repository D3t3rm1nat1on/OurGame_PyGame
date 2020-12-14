import pygame
from pygame.math import Vector2

from command import JumpCommand, MovePlayerCommand, SprintCommand, SlowCommand, MoveEnemyCommand
from layer import UnitLayer
from state import GameState

from .GameMode import GameMode


class PlayGameMode(GameMode):
    def __init__(self):
        super().__init__()

        self.cell_size = Vector2(16, 16)
        self.game_window = pygame.Surface((240, 160))

        self.state = GameState()
        self.player = self.state.units[0]

        self.layers = [None] * 3
        self.layers[2] = (UnitLayer(self.cell_size, "assets/units_spritesheet_test.png", self.state))

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
                elif event.key == pygame.K_LEFT:
                    self.player.is_slowing = True
                elif event.key == pygame.K_RIGHT:
                    self.player.is_sprinting = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.is_slowing = False
                if event.key == pygame.K_RIGHT:
                    self.player.is_sprinting = False
        if self.player.is_slowing:
            command = SlowCommand(self.state, self.player)
            self.commands.append(command)
        elif self.player.is_sprinting:
            command = SprintCommand(self.state, self.player)
            self.commands.append(command)

        command = MovePlayerCommand(self.state, self.player)
        self.commands.append(command)

        for i in range(1, len(self.state.units)):
            command = MoveEnemyCommand(self.state, self.state.units[i], self.player)
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
