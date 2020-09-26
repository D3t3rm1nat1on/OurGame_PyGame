import os
import pygame
import src.command as commands
import src.state as states
from pygame.math import Vector2

os.environ['SDL_VIDEO_CENTERED'] = '1'


class GameWindow():
    def __init__(self):
        pygame.init()
        self.window_proportion = 1
        self.game_state = states.GameState()
        self.player = self.game_state.unit
        self.window = pygame.display.set_mode((int(self.game_state.world_size.x) * self.window_proportion,
                                               int(self.game_state.world_size.y) * self.window_proportion))
        pygame.display.set_caption("Наша ахуенная игра")
        pygame.display.set_icon(pygame.image.load("Pandemonica.png"))
        self.clock = pygame.time.Clock()
        self.running = True

    def render(self):
        self.window.fill((53, 129, 227))  # ФОН
        player_collision = [int(x) for x in
                            (self.player.position.x, self.player.position.y, self.player.size.x, self.player.size.y)]
        pygame.draw.rect(self.window, (73, 111, 13), player_collision)
        ground_level = (
        int(self.game_state.ground.x) * self.window_proportion, int(self.game_state.ground.y) * self.window_proportion,
        int(self.game_state.world_size.x) * self.window_proportion,
        int(self.game_state.world_size.y) * self.window_proportion)
        pygame.draw.rect(self.window, (166, 111, 0), ground_level)
        pygame.display.update()

    def run(self):
        while self.running:
            self.process_input()
            self.update()
            self.render()
            self.clock.tick(60)

    def update(self):

        self.player.speed += self.game_state.gravity
        self.player.position += self.player.speed
        if self.player.position.y + self.player.size.y >= self.game_state.ground.y and self.player.speed.y >= 0:
            self.player.position.y = self.game_state.ground.y - self.player.size.y
            self.player.speed = Vector2(self.player.speed.x, 0)

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_UP:
                    if self.player.position.y + self.player.size.y >= self.game_state.ground.y:
                        self.player.speed -= Vector2(0, 10)


game = GameWindow()
game.run()
pygame.quit()
