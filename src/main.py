import os
import pygame
import src.command as commands
import src.state as states

os.environ['SDL_VIDEO_CENTERED'] = '1'


class GameWindow():
    def __init__(self):
        pygame.init()
        self.rect = 1
        self.game_state = states.GameState()
        self.player = self.game_state.unit
        self.window = pygame.display.set_mode((int(self.game_state.world_size.x) * self.rect, int(self.game_state.world_size.y) * self.rect))
        #self.window = pygame.display.set_mode((1600, 900))
        pygame.display.set_caption("Наша ахуенная игра")
        pygame.display.set_icon(pygame.image.load("Pandemonica.png"))
        self.clock = pygame.time.Clock()
        self.running = True

    def render(self):
        self.window.fill((123, 124, 6))
        pygame.draw.rect(self.window, (166, 111, 0), (10, 10, 200, 200))
        ground_level = (int(self.game_state.ground.x) * self.rect, int(self.game_state.ground.y) * self.rect, int(self.game_state.world_size.x) * self.rect, int(self.game_state.world_size.y) * self.rect)
        pygame.draw.rect(self.window, (166, 111, 0), ground_level)
        pygame.display.update()

    def run(self):
        while self.running:
            self.render()
            self.clock.tick(60)


game = GameWindow()
game.run()
pygame.quit()
