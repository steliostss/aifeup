import World as wd
import operator
import Functions as fun

class World:

    def __init__(self, _level, _lives=4):
        # initialize class instance and attributes
        self.map = self.read_world(_level)
        self.X = len(self.map)
        self.Y = len(self.map[0])
        self.userposition = self.find_user_position()
        self.lives = _lives
        self.path = []
        self.path.append(self.userposition)
        self.available_movements = fun.initialize2DList(self.X, self.Y)
        self.update_available_movements()

    def find_user_position(self):
        # this function searches the grid and looks for
        # the position of the user. it returns a tuple
        # with the coordinates
        i = 0
        sizeX = self.X
        sizeY = self.Y
        while (i < sizeX):
            j = 0
            while j < sizeY:
                if self.map[i][j] == 'U':
                    return (i, j)
                j+=1
            i+=1

    def update_available_movements(self):
        sizeX = self.X
        sizeY = self.Y        
        i = 0
        while (i < sizeX):
            j = 0
            while (j < sizeY):
                self.check_neighbours(i,j)
                j+=1
            i+=1

    def check_neighbours(self, i, j):
        # this functions checks all neighbours and IF they ARE NOT 'W'
        # aka Wall, then it adds the "movement" to the available_movements
        # class attribute
        directions = {
            (-1,0)  : 'w', # up
            (1,0)   : 's', # down
            (0,-1)  : 'a', # left
            (0,1)   : 'd'  # right
        }
        if self.map[i][j] == 'W' or self.map[i][j] == 'F' or self.map[i][j] == 'H':
            return
        self.available_movements[i][j] = []
        for dir_tuple in directions:
            x , y = tuple(map(sum, zip( (i,j), dir_tuple)))
            condition = (x >= 0 and x < self.X and y >= 0 and y < self.Y)
            if condition:
                if self.map[x][y] != 'W':
                    self.available_movements[i][j].append(directions.get(dir_tuple))
                    print(self.available_movements[i][j])

    def print_world (self):
        for i in self.map: 
            for item in i: 
                print(item, end=' ')
            print()

    def read_world (self, levelid):
        # read the world line by line
        # give as argument the level you want to play
        levelid = str(levelid) 
        with open("./levels/level"+levelid+".txt") as f:
            world = [line.split() for line in f]
        return world
