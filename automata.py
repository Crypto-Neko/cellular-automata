import os   # Necessary to clear screen for demonstration.
from time import sleep


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
        return str(self.s)
    
    __repr__ = __str__


#################################################################################################################
# Represents an automaton object, including implementations of the main functions driving the dynamical system. #
#                                                                                                               #
# Automaton.tiles: A matrix containing the tiles of the grid so self.tiles[y][x] gives the tile at (x, y).      #
#                                                                                                               #
# Automaton.update_tiles: Run time forward one step, applying the rules of the dynamical system one time.       #
# Automaton.show_grid: Print the grid in the form of an x_size-by-y_size matrix.                                #
# Automaton.play: Show the evolution of the state of the automaton through time as an animated grid.            #
#################################################################################################################
class Automaton():
    def __init__(self, x_size, y_size, tiles):

        if not isinstance(tiles, list):
            return "Please make sure tiles is a list."

        self.tiles = []
        i = 0
        while i < y_size:
            j = 0
            row = []
            while j < x_size:
                row.append(Tile(j, i, 0))
                j+=1
            self.tiles.append(row)
            i+=1
        for tile in tiles:
            self.tiles[tile.y][tile.x] = tile


    # Moves the automaton forward one step in time according to pre-programmed rules. Updates the automaton
    # a total of n times using recursion.
    def update_tiles(self, n):

        # Make new lists to store the updated tiles and grid so that the original matrices
        # are not updated while the rules are in the process of being applied.
        new_tiles = []
        x_size = len(self.tiles[0])
        y_size = len(self.tiles)
        i = 0
        while i < x_size:
            j = 0
            row = []
            while j < y_size:
                row.append(Tile(j, i, 0))
                j+=1
            new_tiles.append(row)
            i+=1
        for row in self.tiles:
            for tile in row:
                new_tiles[tile.y][tile.x] = Tile(tile.x, tile.y, tile.s)

        # Update the new tiles and grid matrices according to pre-programmed rules.
        for row in self.tiles:
            for tile in row:
                left_state = self.tiles[tile.y][(tile.x - 1) % x_size].s
                right_state = self.tiles[tile.y][(tile.x + 1) % x_size].s
                up_state = self.tiles[(tile.y - 1) % y_size][tile.x].s
                down_state = self.tiles[(tile.y + 1) % y_size][tile.x].s

                pop = left_state + right_state + up_state + down_state
                state = tile.s

                if state == 1:
                    if pop < 2:
                        new_tiles[tile.y][tile.x].s = 0
                    if pop == 2 or pop == 3:
                        new_tiles[tile.y][tile.x].s = 1
                    if pop > 3:
                        new_tiles[tile.y][tile.x].s = 0
                if state == 0 and pop == 3:
                    new_tiles[tile.y][tile.x].s = 1

        self.tiles = new_tiles
        if n != 1:
            self.update_tiles(n-1);

    # Demonstrate the evolution of the automaton through time in the form of an animated grid. WIP.
    def show_grid(self):
        j = 0
        while j < len(self.tiles[0]):
            i = 0
            while i < len(self.tiles):
                print(str(self.tiles[j][i]), end=" ")
                i+=1
            print()
            j+=1

    def __str__(self):
        self.show_grid()
        return str()

    __repr__ = __str__

    # Play the evolution of the system forward in the terminal.
    def play(self, n=1):
        os.system("clear")
        while True:
            self.show_grid()
            sleep(2)
            self.update_tiles(1)
            os.system("clear")


#### CURRENT TESTING CODE ####

# Basic test
tile1 = Tile(0, 0, 1)
tile2 = Tile(1, 0, 0)
tile3 = Tile(0, 1, 0)
tile4 = Tile(1, 1, 1)
tiles = [Tile(0, 0, 1), Tile(1, 0, 1), Tile(2, 0, 1), Tile(0, 1, 0), Tile(1, 1, 1), Tile(2, 1, 0), Tile(0, 2, 1), Tile(1, 2, 1), Tile(2, 2, 1), Tile(3, 3, 1), Tile(3, 4, 1), Tile(2, 4, 1), Tile(2, 3, 1)]
automaton = Automaton(10, 10, tiles)

# Smoke
tile1 = Tile(0, 0, 1)
tile2 = Tile(1, 0, 1)
tile3 = Tile(0, 1, 1)
tile4 = Tile(1, 1, 1)
tile5 = Tile(2, 2, 1)
tile6 = Tile(3, 3, 1)
tile7 = Tile(3, 4, 1)
tile8 = Tile(4, 3, 1)
tiles = [tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8]
smoke = Automaton(10, 10, tiles)
