# Course: CS 30
# Period: 2
# Date created: 21/02/08
# Date last modified: 25/02/08
# Name: Laraib Bin Aas
# Description: Make a map that allows you to move in it
# Code adpated from https://github.com/kynite/FishingRPG

from player import Player

player = Player(1, 2)


class MapTile:
    """Parent Class to child classes"""
    def __init__(self, x, y):
        # x position of map tiles
        self.x = x
        # y position of map tiles
        self.y = y

    def __str__(self):
        """Gets the name of the child class and makes it a string"""
        return self.name


class mountain(MapTile):
    """location with golem"""
    def __init__(self, x, y):
        self.name = "mountain"
        # Position of graveyard tile
        super().__init__(x, y)


class cave(MapTile):
    """location with goblins"""
    def __init__(self, x, y):
        self.name = "cave"
        # Position of cave tile
        super().__init__(x, y)


class jungle(MapTile):
    """location with jungle"""
    def __init__(self, x, y):
        self.name = "jungle"
        # Position of field tile
        super().__init__(x, y)


class house(MapTile):
    """location with a house"""
    def __init__(self, x, y):
        self.name = "house"
        # Position of field tile
        super().__init__(x, y)


class end(MapTile):
    """location with the end"""
    def __init__(self, x, y):
        self.name = "end"
        # Position of end tile
        super().__init__(x, y)


# The map
world_map = [[end(0, 0), None, mountain(2, 0)],
             [cave(0, 1), jungle(1, 1), None],
             [None, player, house(2, 2)]]
