from pygame import Vector2

from .Layer import Layer


class ArrayLayer(Layer):
    def __init__(self, cell_size, texture, game_state, array):
        """

        :type cell_size:
        :type texture:
        :type game_state: GameState
        :type array:      Vector2[][]
        """
        super().__init__(cell_size, texture)
        self.game_state = game_state
        self.array = array

    def render(self, surface):
        for y in range(self.game_state.world_height):
            for x in range(self.game_state.world_width):
                tile = self.array[y][x]
                if tile is not None:
                    self.render_tile(surface, Vector2(x, y), tile)
