import math
import random

from pygame.math import Vector2

from .MoveCommand import MoveCommand


class MoveEnemyCommand(MoveCommand):
    def __init__(self, state, enemy, player_unit):
        super().__init__(state, enemy)
        self.player_unit = player_unit

    def run(self):
        super().run()
        enemy = self.unit
        # враг ушел за экран (успешный dodge)
        if enemy.rect_collision.right <= -enemy.full_size.x:
            rand = random.randint(self.state.world_size.x / 2, self.state.world_size.x)
            enemy.position = Vector2(rand, self.state.ground.y - 100)
            self.state.score += 1
        # враг ударил игрока
        if self.unit.rect_collision.colliderect(self.player_unit.rect_collision):
            #rand = random.randint(self.state.world_size.x / 2, self.state.world_size.x)
            #self.unit.position = Vector2(rand, self.state.ground.y - 100)
            enemy.is_alive = False
            self.player_unit.position.x -= 20
            if self.player_unit.position.x < 0:
                print("LOG: PakeT T H I C C")

    def unique_movement(self):
        if self.unit.type == 'bird':
            self.unit.angle += 5
            cos = math.cos(math.radians(self.unit.angle))
            sin = math.sin(math.radians(self.unit.angle))
            self.unit.rad_speed = 2 * Vector2(cos, sin)
            self.unit.speed = self.unit.const_speed + self.unit.rad_speed

