import random
from datetime import datetime
import pygame
from pygame.math import Vector2

from mode import PlayGameMode
from state import Unit
from mode import PlayGameMode

from .MoveCommand import MoveCommand


class MoveEnemyCommand(MoveCommand):
    player_unit: Unit

    def __init__(self, state, enemy, player_unit):
        super().__init__(state, enemy)
        self.player_unit = player_unit

    def run(self):
        super().run()
        enemy = self.unit
        # враг ушел за экран (успешный dodge)
        if enemy.position.x + enemy.size.x <= -enemy.size.x:
            rand_x = random.randint(int(self.state.world_size.x * 1.2), int(self.state.world_size.x * 1.5))
            rand_y = random.randint(self.state.ground_level - 2, self.state.ground_level)
            enemy.position = Vector2(rand_x, rand_y)
            self.state.score += 1

        if not enemy.is_alive:
            self.state.units.remove(enemy)

        enemy_col = pygame.Rect(enemy.position.elementwise() * Vector2(16, 16),
                                enemy.size.elementwise() * Vector2(16, 16))
        player_col = pygame.Rect(self.player_unit.position.elementwise() * Vector2(16, 16), (16, 16))
        # враг ударил игрока
        if enemy_col.colliderect(player_col) and (enemy.position.x - self.player_unit.position.x) < 0.75:
            self.player_unit.position.x -= 0.75 - (enemy.position.x - self.player_unit.position.x)
            if self.player_unit.position.x < 0:
                print("LOG: PakeT T H I C C")
                self.state.lives -= 1
                self.player_unit.position.y = 0
                self.player_unit.position.x = 200
                if self.state.lives < 0:
                    self.serialize()
                    self.state.score = 0

    def serialize(self):
        now = datetime.now()
        date = '.'.join([str(now.day), str(now.month), str(now.year)])
        result = [1, self.state.score, date]
        with open('results.txt', 'r') as f:
            nums = f.read().splitlines()
        results = []
        for res in nums:
            res = res.split()
            results.append([int(res[0]) + 1, int(res[1]), res[2]])
        results.append(result)
        results.sort(key=lambda x: x[0])
        all_score = [x[1] for x in results]
        best_score_idx = all_score.index(max(all_score))
        results[0], results[best_score_idx] = results[best_score_idx], results[0]
        temp = results[1:]
        temp.sort(key=lambda x: x[0])
        temp.insert(0, results[0])
        print("------")
        print(*results, sep='\n', end='\n\n')
        results = temp[:10]
        print(*results, sep='\n', end='\n\n')
        with open('results.txt', 'w') as f:
            for res in results:
                res = list(map(str, res))
                f.write(' '.join(res))
                f.write('\n')
            print()
        tmp = 0
        with open('money.txt', 'r') as f:
            tmp = int(f.read())
        with open('money.txt', 'w') as f:
            f.write(str(self.state.money + tmp))
