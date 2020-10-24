import os
from typing import List, Any

import pygame
from pygame.math import Vector2

import src.state as states
from src.command import *
from src.state import GameState

os.environ['SDL_VIDEO_CENTERED'] = '1'


class GameWindow:
    commands: List[Command]

    def __init__(self):
        pygame.init()
        self.window_proportion = 1
        self.state = GameState()
        self.state.ground = pygame.Rect(self.state.ground, self.state.world_size)
        self.player = states.Player(full_size=Vector2(40, 80), affected_by_gravity=True)
        self.window = pygame.display.set_mode((int(self.state.world_size.x) * self.window_proportion,
                                               int(self.state.world_size.y) * self.window_proportion))
        pygame.display.set_caption("Наша игра")
        pygame.display.set_icon(pygame.image.load("../assets/Pandemonica.png"))
        self.clock = pygame.time.Clock()
        self.running = True

        self.state.enemies.append(
            states.Unit(position=Vector2(self.state.world_size.x + 100, 20), speed=Vector2(-8, 0)))
        self.state.enemies.append(
            states.Unit(position=Vector2(self.state.world_size.x, self.state.ground.y - 100), speed=Vector2(-6, 0),
                        full_size=Vector2(50, 50), affected_by_gravity=False))
        bird = states.UnitBird(position=Vector2(self.state.world_size.x, self.state.ground.y - 100),
                               speed=Vector2(-6, 0),
                               full_size=Vector2(25, 25), affected_by_gravity=False)
        self.state.enemies.append(bird)

        bomb = states.UnitBirdBomb(position=Vector2(self.state.world_size.x, self.state.ground.y - 100),
                                   speed=Vector2(-5, 0),
                                   full_size=Vector2(35, 35), affected_by_gravity=False)
        self.state.enemies.append(bomb)
        self.state.enemies.clear()
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
                elif event.key == pygame.K_DOWN:
                    command = CrouchCommand(self.state, self.player)
                    self.commands.append(command)
                elif event.key == pygame.K_RIGHT:
                    self.player.is_sprinting = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    if self.player.is_crouching:
                        self.player.is_crouching = False
                        self.player.rect_collision.size = self.player.full_size
                        self.player.position.y -= self.player.full_size.y - self.player.crouch_size.y
                        self.player.speed.x = 0
                if event.key == pygame.K_RIGHT:
                    if self.player.is_sprinting:
                        self.player.is_sprinting = False

        if self.player.is_sprinting:
            command = SprintCommand(self.state, self.player)
            self.commands.append(command)

        command = MovePlayerCommand(self.state, self.player)
        self.commands.append(command)

    def update(self):
        for command in self.commands:
            command.run()
        self.commands.clear()

        for enemy in self.state.enemies:
            MoveEnemyCommand(self.state, enemy, self.player).run()

    def render(self):
        self.window.fill((53, 129, 227))

        ground = pygame.Rect(
            int(self.state.ground.x) * self.window_proportion,
            int(self.state.ground.y) * self.window_proportion,
            int(self.state.world_size.x) * self.window_proportion,
            int(self.state.world_size.y) * self.window_proportion)
        ground_color = (166, 111, 0)
        pygame.draw.rect(self.window, ground_color, ground)

        pygame.draw.line(self.window, (0, 0, 0), (self.state.border_left, 0),
                         (self.state.border_left, self.state.world_size.y))
        pygame.draw.line(self.window, (0, 0, 0), (self.state.border_right, 0),
                         (self.state.border_right, self.state.world_size.y))

        player_collision = self.player.rect_collision
        enemy_collisions = []
        for enemy in self.state.enemies:
            enemy_collisions.append(enemy.rect_collision)

        pygame.draw.rect(self.window, (73, 111, 13), player_collision, 3)
        for enemy_collision in enemy_collisions:
            pygame.draw.rect(self.window, (140, 10, 13), enemy_collision, 3)

        text = "Score: " + str(self.state.score)
        self.window.blit(pygame.font.SysFont('Comic Sans MS', 30).render(text, True, (0, 0, 0)), (0, 0))
        self.window.blit(pygame.font.SysFont('Comic Sans MS', 30).render(str(self.player.speed.x), True, (0, 0, 0)), (150, 0))

        pygame.draw.rect(self.window, (0, 200, 50), (0, 50, self.player.stamina * 2, 40))

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
