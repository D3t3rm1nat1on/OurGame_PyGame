import math

from pygame.math import Vector2

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
        self.animations = [
            {
                'name': 'p_run',
                'row': 0,
                'max_index': 6
            },
            {
                'name': 'p_jump_up',
                'row': 1,
                'max_index': 3,
            },
            {
                'name': 'p_jump_down',
                'row': 2,
                'max_index': 3,
            },
            {
                'name': 'g_run',
                'row': 3,
                'max_index': 6,
            },
            {
                'name': 'b_fly',
                'row': 4,
                'max_index': 3,
            },
            {
                'name': 'coin',
                'row': 5,
                'max_index': 6,
            },
        ]

    def render(self, surface):
        for unit in self.game_state.units:
            tile_x = math.floor(unit.frame_index)
            animation = self.animations[unit.state.value]
            tile_y = animation['row']
            if tile_x < animation['max_index']:
                unit.frame_index += 0.25
            else:
                tile_x = 0
                unit.frame_index = 0
            tile = Vector2(tile_x, tile_y)
            self.render_tile(surface, unit.position, tile, unit.size)
