import numpy as np


###################################################################################
# Represents a tile object, holding a tile and its state on the grid representing #
# the space in which the automaton is evolving. Takes x and y coordinates and the #
# state s as input.                                                               #
#                                                                                 #
# Tile.x: The horizontal position of the tile.                                    #
# Tile.y: The vertical positon of the tile.                                       #
# Tile.s: The current state of the tile, either on or off.                        #
###################################################################################
class Tile():
    def __init__(self, x, y, s):
        self.x = int(x)
        self.y = int(y)
        if s == 0 or s == 1:
            self.s = s
        else:
            return "Please pass either 0 or 1 for the state."

    def __str__(self):
        return str("(" + str(self.x) +", " + str(self.y) + ", " + str(self.s) + ")")
    
    __repr__ = __str__


#################################################################################################################
# Represents an automaton object, including implementations of the main functions driving the dynamical system. #
#                                                                                                               #
# Automaton.tiles: A matrix containing the tiles of the grid so self.tiles[y][x] gives the tile at (x, y).      #
# Automaton.grid: A matrix containing the states of each tile such that self.grid[y][x] gives tile.s at (x, y). #
#                                                                                                               #
# Automaton.update_tiles: Run time forward one step, applying the rules of the dynamical system one time.       #
# Automaton.show: Show the evolution of the state of the automaton through time as an animated grid.            #
#################################################################################################################
class Automaton():
    def __init__(self, x_size, y_size, tiles):
        self.tiles = [[0]*y_size]
        self.grid = [[0]*y_size]
        i = 1
        while i < x_size:
            self.tiles.append([0]*y_size)
            self.grid.append([0]*y_size)
            i+=1
        if not isinstance(tiles, list):
            return "Please make sure tiles is a list."
        for tile in tiles:
            if tile.x > -1 and tile.y > -1 and tile.x < x_size and tile.y < y_size:
                self.tiles[tile.y][tile.x] = tile
                self.grid[tile.y][tile.x] = tile.s

    # Moves the automaton forward one step in time according to pre-programmed rules.
    def update_tiles(self):

        # Make new lists to store the updated tiles and grid so that the original matrices
        # are not updated while the rules are in the process of being applied.
        new_tiles = [[0]*len(self.grid)]
        new_grid = [[0]*len(self.grid)]
        x_size = len(self.grid[0])
        i = 0
        while i < x_size:
            new_tiles.append([0]*y_size)
            new_grid.append([0]*y_size)
        for column in self.tiles:
            for tile in column:
                new_tiles[tile.y][tile.x] = Tile(tile.x, tile.x, tile.s)
                new_grid[tile.y][tile.x] = tile.s

        # Update the new tiles and grid matrices according to pre-programmed rules.
        for column in self.tiles:
            for tile in column:
                left_state = self.grid[tile.y][tile.x - 1]
                right_state = self.grid[tile.y][tile.x + 1]
                up_state = self.grid[tile.y + 1][tile.x]
                down_state = self.grid[tile.y - 1][tile.x]

    # Demonstrate the evolution of the automaton through time in the form of an animated grid. WIP.
    def show(self):
        return 0


#### CURRENT TESTING CODE ####
tile1 = Tile(0, 0, 1)
tile2 = Tile(1, 0, 0)
tile3 = Tile(0, 1, 0)
tile4 = Tile(1, 1, 1)
tiles = [tile1, tile2, tile3, tile4]
automaton = Automaton(2, 2, tiles)
