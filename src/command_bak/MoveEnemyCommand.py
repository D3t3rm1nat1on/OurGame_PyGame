import random
from datetime import datetime
from pygame.math import Vector2

from src.state_bak import Unit
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
        if enemy.rect_collision.right <= -enemy.full_size.x:
            rand = random.randint(self.state.world_size.x / 2, self.state.world_size.x)
            enemy.position = Vector2(rand, self.state.ground.y - 100)
            self.state.score += 1

        if not self.unit.is_alive:
            self.state.enemies.remove(self.unit)

        # враг ударил игрока
        if self.unit.rect_collision.colliderect(self.player_unit.rect_collision):
            self.unit.hit()
            if self.unit.is_killable:
                self.state.enemies.remove(self.unit)
            self.player_unit.position.x -= 20
            if self.player_unit.position.x < 0:
                print("LOG: PakeT T H I C C")
                self.serialize()
                self.state.score = 0
                self.player_unit.position.y = 0
                self.player_unit.position.x = 200

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
