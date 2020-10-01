import os
import random

import pygame
from pygame.math import Vector2

import src.state as states
from command import JumpCommand, MoveCommand, MoveEnemyCommand
from state import GameState

os.environ['SDL_VIDEO_CENTERED'] = '1'


class GameWindow:
    def __init__(self):
        pygame.init()
        self.score = 0
        self.window_proportion = 1
        self.state = GameState()
        self.player = self.state.unit
        self.window = pygame.display.set_mode((int(self.state.world_size.x) * self.window_proportion,
                                               int(self.state.world_size.y) * self.window_proportion))
        pygame.display.set_caption("Наша ахуенная игра")
        pygame.display.set_icon(pygame.image.load("../assets/Pandemonica.png"))
        self.clock = pygame.time.Clock()
        self.running = True

        self.enemies = [states.Unit(position=Vector2(self.state.world_size.x, 20), speed=Vector2(-8, 0))]
        self.enemies.append(states.Unit(position=Vector2(self.state.world_size.x + 100, 20), speed=Vector2(-8, 0)))

        self.commands = []

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
                    command = JumpCommand(self.state, self.player)
                    self.commands.append(command)

        command = MoveCommand(self.state, self.player)
        self.commands.append(command)

    def update(self):
        for command in self.commands:
            command.run()
        self.commands.clear()

        for enemy in self.enemies:
            self.score += MoveEnemyCommand(self.state, enemy, self.player).run()

    def render(self):
        self.window.fill((53, 129, 227))  # ФОН
        player_collision = [int(x) for x in
                            (self.player.position.x, self.player.position.y, self.player.size.x, self.player.size.y)]
        enemy_collisions = []
        for enemy in self.enemies:
            enemy_collisions.append([int(x) for x in
                                     (enemy.position.x, enemy.position.y, enemy.size.x, enemy.size.y)])

        pygame.draw.rect(self.window, (73, 111, 13), player_collision)
        for enemy_collision in enemy_collisions:
            pygame.draw.rect(self.window, (140, 10, 13), enemy_collision)
        ground_level = (
            int(self.state.ground.x) * self.window_proportion,
            int(self.state.ground.y) * self.window_proportion,
            int(self.state.world_size.x) * self.window_proportion,
            int(self.state.world_size.y) * self.window_proportion)
        pygame.draw.rect(self.window, (166, 111, 0), ground_level)
        text = "Score: " + str(self.score)
        self.window.blit(pygame.font.SysFont('Comic Sans MS', 30).render(text, True, (0, 0, 0)), (0, 0))
        pygame.display.update()

    def run(self):
        while self.running:
            self.process_input()
            self.update()
            self.render()
            self.clock.tick(60)


game = GameWindow()
game.run()
pygame.quit()
