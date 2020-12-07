import enum

import pygame

from mode import GameModeObserver, PlayGameMode, MenuGameMode
from setup import LoadLevel


class UserInterface(GameModeObserver):
    class Modes(enum.Enum):
        Overlay = 0
        Play = 1

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1500, 960))
        pygame.display.set_caption("Our Game")
        pygame.display.set_icon(pygame.image.load("assets/Pandemonica.png"))

        self.play_game_mode = None
        self.overlay_mode = MenuGameMode()
        self.overlay_mode.add_observer(self)
        self.current_mode = self.Modes.Overlay

        # self.game = PlayGameMode()
        # self.game.add_observer(self)
        # LoadLevel("assets/sample_map.tmx", self.game).run()

        # self.menu = MenuGameMode()
        # self.menu.add_observer(self)

        self.clock = pygame.time.Clock()
        self.running = True

    def load_level_requested(self):
        if self.play_game_mode is None:
            self.play_game_mode = PlayGameMode()
            self.play_game_mode.add_observer(self)
        LoadLevel("assets/sample_map.tmx", self.play_game_mode).run()
        self.current_mode = self.Modes.Play

    def show_game_requested(self):
        if self.play_game_mode is not None:
            self.current_mode = self.Modes.Play

    def quit_requested(self):
        self.running = False

    def run(self):
        while self.running:
            if self.current_mode == self.Modes.Overlay:
                self.overlay_mode.process_input()
                self.overlay_mode.update()
            elif self.play_game_mode is not None:
                self.play_game_mode.process_input()
                self.play_game_mode.update()

            if self.play_game_mode is not None:
                self.play_game_mode.render(self.window)
            else:
                self.window.fill((0, 0, 0))
            if self.current_mode == self.Modes.Overlay:
                self.overlay_mode.render(self.window)

            # self.game.process_input()
            # self.game.update()
            # self.game.render(self.window)
            # self.menu.process_input()
            # self.menu.render(self.window)
            pygame.display.update()
            self.clock.tick(60)


UI = UserInterface()
UI.run()

pygame.quit()
