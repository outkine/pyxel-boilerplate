from pyxel import *
from math import floor


class Tilemap:
    def __init__(self, relative=True, size=8, colkey=0):
        self.x = 0
        self.y = 0
        self.relative = relative
        self.size = size
        self.colkey = colkey

    def get(self, tm, x, y):
        return tilemap(tm).get(self.x * self.size + x, self.y * self.size + y)

    def set(self, tm, x, y, data):
        return tilemap(tm).set(self.x * self.size + x, self.y * self.size + y,
                               data)

    def find_all(self, tm, tile):
        return [(x, y) for x in range(self.size) for y in range(self.size)
                if self.get(tm, x, y) == tile]

    def find(self, tm, tile):
        res = self.find_all(tm, tile)
        if not res:
            raise Exception(f'Could not find tile {tile} in tilemap {tm}')
        return res[0]

    def draw(self, tm, colkey=0):
        bltm(0, 0, tm, self.x * self.size, self.y * self.size, self.size,
             self.colkey)


def sprite(x, y, n, m=0, size=8, colkey=0):
    blt(x * size, y * size, 0, n * size, m * size, size, size, colkey)


def mouse_tile_pos(tile_size=8, screen_size=64):
    return floor(mouse_x * size / screen_size), floor(mouse_y * size /
                                                      screen_size)
