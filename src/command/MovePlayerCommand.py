from .MoveCommand import MoveCommand


class MovePlayerCommand(MoveCommand):
    def __init__(self, state, player):
        super().__init__(state, player)

    def run(self):
        super().run()
        player = self.unit
        # зона игрока
        if player.rect_collision.left <= self.state.border_left:
            player.position.x = self.state.border_left
        if player.rect_collision.right >= self.state.border_right:
            player.position.x = self.state.border_right - self.unit.rect_collision.size[0]


