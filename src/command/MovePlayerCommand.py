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

        # замедляется без спринта (в подкате и дивижении назад не спринтует)
        if (not player.is_sprinting or player.is_crouching or player.is_slowing) and self.on_ground(self.state, player):
            if player.speed.x > .09:
                player.speed.x -= .09
            elif player.speed.x > 0:
                player.speed.x = 0

        # ускоряется до *нулевой* скосрости
        if not (player.is_crouching or player.is_slowing) and self.on_ground(self.state, player):
            if player.speed.x < -.09:
                player.speed.x += .09
            elif player.speed.x < 0:
                player.speed.x = 0

        # регенерация стамины
        if not player.is_sprinting or not self.on_ground(self.state, player):
            player.stamina += 0.3
        if player.stamina > 100.0:
            player.stamina = 100.0
