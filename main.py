import enum

import pygame

from mode import GameModeObserver, PlayGameMode, MenuGameMode, PauseMode, ChoosePerkMode, EndGameMode
from setup import LoadLevel


class UserInterface(GameModeObserver):
    class Modes(enum.Enum):
        Overlay = 0
        Play = 1
        Pause = 2
        Perk = 3
        End = 4

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1500, 960))
        pygame.display.set_caption("Our Game")
        pygame.display.set_icon(pygame.image.load("assets/Pandemonica.png"))

        self.play_game_mode = None
        self.overlay_pause_mode = None
        self.overlay_perks_mode = None
        self.end_game_mode = None
        self.load_level_requested()
        self.overlay_mode = MenuGameMode()
        self.overlay_mode.add_observer(self)
        self.current_mode = self.Modes.Overlay

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

    def show_menu_requested(self):
        with open('src/config.txt', 'w') as f:
            f.write(str(self.overlay_mode.settings.vol))
        self.overlay_mode = MenuGameMode()
        self.overlay_mode.add_observer(self)
        self.current_mode = self.Modes.Overlay

    def show_pause_requested(self):
        self.overlay_pause_mode = PauseMode()
        self.overlay_pause_mode.add_observer(self)
        self.current_mode = self.Modes.Pause

    def show_perks_requested(self):
        self.overlay_perks_mode = ChoosePerkMode()
        self.overlay_perks_mode.add_observer(self)
        self.current_mode = self.Modes.Perk

    def show_end_game_requested(self):
        self.end_game_mode = EndGameMode()
        self.end_game_mode.add_observer(self)
        self.current_mode = self.Modes.End

    def quit_requested(self):
        with open('src/config.txt', 'w') as f:
            f.write(str('10'))
        self.running = False

    def run(self):
        while self.running:
            if self.current_mode == self.Modes.Overlay:
                self.overlay_mode.process_input()
                self.overlay_mode.update()
            elif self.current_mode == self.Modes.Pause:
                self.overlay_pause_mode.process_input()
                self.overlay_mode.update()
            elif self.current_mode == self.Modes.Perk:
                self.overlay_perks_mode.process_input()
                self.overlay_perks_mode.update()

            elif self.current_mode == self.Modes.End:
                self.end_game_mode.process_input()
                self.end_game_mode.update()

            elif self.play_game_mode is not None:
                self.play_game_mode.process_input()
                self.play_game_mode.update()

            if self.play_game_mode is not None:
                self.play_game_mode.render(self.window)
            else:
                self.window.fill((0, 0, 0))
            if self.current_mode == self.Modes.Overlay:
                self.overlay_mode.render(self.window)
            if self.current_mode == self.Modes.End:
                self.end_game_mode.render(self.window)
            if self.current_mode == self.Modes.Perk:
                self.overlay_perks_mode.render(self.window)
            if self.current_mode == self.Modes.Pause:
                self.overlay_pause_mode.render(self.window)

            pygame.display.update()
            self.clock.tick(60)


UI = UserInterface()
UI.run()

pygame.quit()
