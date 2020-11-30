import os

import tmx
from pygame import Vector2

from layer import ArrayLayer, ImageLayer


class LoadLevel:
    def __init__(self, file_name, game_mode):
        """

        :type file_name: String
        :type game_mode: PlayGameMode
        """
        self.file_name = file_name
        self.game_mode = game_mode
        self.map_layers = 2

    def run(self):
        state = self.game_mode.state

        if not os.path.exists(self.file_name):
            raise RuntimeError("No file {}".format(self.file_name))
        tile_map = tmx.TileMap.load(self.file_name)
        if tile_map.orientation != "orthogonal":
            raise RuntimeError("Error in {}: invalid orientation".format(self.file_name))
        if len(tile_map.layers) != self.map_layers:
            raise RuntimeError("Error in {}: 2 layers are expected".format(self.file_name))

        state.world_size = Vector2(tile_map.width, tile_map.height)
        image = self.decode_background(tile_map.layers[0]).source
        self.game_mode.layers[0] = ImageLayer(image)

        tileset, array = self.decode_array_layer(tile_map, tile_map.layers[1])
        cell_size = Vector2(tileset.tilewidth, tileset.tileheight)
        state.ground[:] = array
        image_file = tileset.image.source
        self.game_mode.layers[1] = ArrayLayer(cell_size, image_file, state, state.ground)

    def decode_array_layer(self, tile_map, layer):
        """

        :type tile_map: tmx.TileMap
        :type layer:    tmx.Layer
        """
        tileset = self.decode_layer(tile_map, layer)

        array = [None] * tile_map.height
        for y in range(tile_map.height):
            array[y] = [None] * tile_map.width
            for x in range(tile_map.width):
                tile = layer.tiles[x + y * tile_map.width]
                if tile.gid == 0:
                    continue
                lid = tile.gid - tileset.firstgid
                if lid < 0 or lid >= tileset.tilecount:
                    raise RuntimeError("Error in {}: invalid tile id".format(self.file_name))
                tile_x = lid % tileset.columns
                tile_y = lid // tileset.columns
                array[y][x] = Vector2(tile_x, tile_y)
        return tileset, array

    def decode_layer(self, tile_map, layer):
        """

        :type tile_map: tmx.TileMap
        :param layer:
        :return: tileset
        """
        if not isinstance(layer, tmx.Layer):
            raise RuntimeError("Error in {}: invalid layer type".format(self.file_name))
        if len(layer.tiles) != tile_map.width * tile_map.height:
            raise RuntimeError("Error in {}: invalid tiles count".format(self.file_name))

        # Guess which tileset is used by this layer
        gid = None
        for tile in layer.tiles:
            if tile.gid != 0:
                gid = tile.gid
                break
        if gid is None:
            if len(tile_map.tilesets) == 0:
                raise RuntimeError("Error in {}: no tilesets".format(self.file_name))
            tileset = tile_map.tilesets[0]
        else:
            tileset = None
            for t in tile_map.tilesets:
                if t.firstgid <= gid < t.firstgid + t.tilecount:
                    tileset = t
                    break
            if tileset is None:
                raise RuntimeError("Error in {}: no corresponding tileset".format(self.file_name))

        # Check the tileset
        if tileset.columns <= 0:
            raise RuntimeError("Error in {}: invalid columns count".format(self.file_name))
        if tileset.image.data is not None:
            raise RuntimeError("Error in {}: embedded tileset image is not supported".format(self.file_name))

        return tileset

    def decode_background(self, layer):
        if not isinstance(layer, tmx.ImageLayer):
            raise RuntimeError("Error in {}: invalid layer type".format(self.file_name))

        image = layer.image
        if image.data is not None:
            raise RuntimeError("Error in {}: embedded tileset image is not supported".format(self.file_name))

        return image
