import pygame

from Tile import Tile

red = 255, 0, 0


class Gameboard():
    def __init__(self, columns):
        self.display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()
        self.surface = pygame.Surface((self.width, self.height))

        self.x1 = 0
        self.y1 = 0
        self.x2 = self.width
        self.y2 = self.height
        self.tiles = []
        self.tile = Tile(red, 100, 100, 500, 500)
        self.speed = 1
        self.acceleration = 1
        self.columns = columns
        self.borderCol = 255, 255, 255

    def display_board(self):
        distance = self.x2 / self.columns
        for i in range(self.columns - 1):
            from_pos = distance * (i + 1), 0
            to_pos = distance * (i + 1), self.height
            pygame.draw.line(self.display, self.borderCol, from_pos, to_pos, 5)

    def start(self):
        print("start")

    # def update(self):

    def addTile(self, tile):
        self.tiles.append(tile)
