import pygame
from pygame.math import Vector2

from command import JumpCommand, MovePlayerCommand, SprintCommand, SlowCommand, MoveEnemyCommand, MoveCommand, \
    MoveItemCommand
from layer import UnitLayer, ItemLayer
from state import GameState

from .GameMode import GameMode


class PlayGameMode(GameMode):

    def __init__(self):
        super().__init__()

        self.cell_size = Vector2(16, 16)
        self.game_window = pygame.Surface((240, 160))

        self.state = GameState()
        self.player = self.state.units[0]

        self.layers = [None] * 5
        self.layers[3] = (UnitLayer(self.cell_size, "assets/units_spritesheet.png", self.state))
        self.layers[4] = (ItemLayer(self.cell_size, "assets/units_spritesheet.png", self.state))

        self.commands = []

    def process_input(self):
        if self.state.lives < 0:
            self.notify_end_game_requested()
            self.state.lives = 0

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

        for item in self.state.items:
            command = MoveItemCommand(self.state, item, self.player)
            # command = MoveCommand(self.state, item)
            self.commands.append(command)

    def update(self):
        for command in self.commands:
            command.run()
        self.commands.clear()

        # background rolling
        if self.layers[0].position.x > -self.game_window.get_width() and self.layers[1].position.x > 0:
            self.layers[0].position.x -= 0.5
            self.layers[1].position.x -= 0.5
        else:
            self.layers[0].position.x = 0
            self.layers[1].position.x = 240

        # update counters
        if self.state.magnet_counter > 0:
            self.state.magnet_counter -= 1
        if self.state.x2_counter > 0:
            self.state.x2_counter -= 1

    def render(self, window):
        self.game_window.fill((0, 0, 0))

        for layer in self.layers:
            layer.render(self.game_window)

        pygame.transform.scale(self.game_window, window.get_size(), window)

        text = "Score: " + str(self.state.score)
        window.blit(pygame.font.SysFont('Comic Sans MS', 30).render(text, True, (0, 0, 0)), (0, 0))
        window.blit(
            pygame.font.SysFont('Comic Sans MS', 10).render(str(self.player.speed.x), True, (0, 0, 0)),
            (150, 0))
        pygame.draw.rect(window, (0, 30, 8), (0, 50, self.player.stamina, 15))
        text = "Lives: " + str(self.state.lives)
        window.blit(pygame.font.SysFont('Comic Sans MS', 30).render(text, True, (0, 0, 0)), (0, 70))
        # pygame.draw.rect(window, (0, 30, 8), (0, 70, self.player.stamina, 15))
