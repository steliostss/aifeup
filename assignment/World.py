class World:

    def __init__(self, _level, _lives):
        # initialize class instance and attributes
        self.map = self.read_world(_level)
        self.X = len(self.map)
        self.Y = len(self.map[0])
        self.userposition = self.find_user_position()
        self.lives = _lives

    def move(self, direction, steps=1):
        X, Y = self.userposition
        targetX = X
        targetY = Y
        movement = self.decide_move(direction)

    def decide_move(self, direction):
        # based on input movement this function returns the
        # name of the function to be called 
        movements = {
            "up" : 'w',
            "down" : 's',
            "left" : 'a',
            "right" : 'd'
        }
        movement = movements.get(direction, '0')
        move_func = "move"+'_'+movement
        # the move_func variable holds the name of 
        # the function that will be called to 
        # move to the specific direction.
        # it can be called with move_func()
        return move_func

    def update_positions(self, _direction, 
                        _myPosition, _myType, 
                        _nextPosition, _nextType):
        # given myPositon and myType, nextPosition and nextType
        # this function does 3 things:
        # 1. change current position to empty space
        # 2. change nextPosition to myType
        # 3. change nextNextPosition to nextType 
        pass

    def update_user_position (self, _direction):
        x, y = self.position
        if   (_direction == 'W'):
            self.position = (x-1, y)
        elif (_direction == 'S') :
            self.position = (x+1, y)
        elif (_direction == 'A'):
            self.position = (x, y-1)
        else: # _direction = 'D'
            self.position = (x, y+1)

    def find_user_position(self, ):
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
                    user_position = (i, j)
                    return
                j+=1
            i+=1

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

