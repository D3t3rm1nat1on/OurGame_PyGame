import math

from .Layer import Layer


class UnitLayer(Layer):
    def __init__(self, cell_size, texture, game_state):
        """

        :type cell_size:
        :type texture:
        :type game_state: GameState
        """
        super().__init__(cell_size, texture)
        self.game_state = game_state

    def render(self, surface):
        for unit in self.game_state.units:
            self.render_tile(surface, unit.position, unit.tile)
            if unit.frame_index < unit.max_frame_index:
                unit.frame_index += 0.25
            else:
                unit.frame_index = 0
            frame_index = math.floor(unit.frame_index)
            unit.tile.x = frame_index
