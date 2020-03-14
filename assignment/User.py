class User: 
    def __init__(self, _position, _lives, _world):
        self.position = self.find_user_position(_world)
        self.lives = _lives

    def find_user_position(self, _world):
        i = 0
        sizeX = _world.X
        sizeY = _world.Y
        while (i < sizeX):
            j = 0
            while j < sizeY:
                if _world.map[i][j] == 'U':
                    user_position = (i, j)
                    return
                j+=1
            i+=1

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

    #called when user presses W
def move_up (world, steps=1):
    global user_position, sizeX, sizeY
    X, Y = user_position
    target = world[X-1][Y]
    if (target == "W" or target == "H"):
        return False
    else:
        if (target == "F"):
            #TODO END GAME HERE
            pass
        elif (target == "-"):
            world[X-1][Y] = 'U'
            world[X][Y] = '-'
            user_position = (X-1, Y)            
        else: # target == "B"
            if (X-2 >= 0):
                if (world[X-2][Y] == '-'):
                    world[X-1][Y] = 'U'
                    world[X][Y] = '-'
                    user_position = (X-1, Y)
                    world[X-2][Y] = 'B'
                elif (world[X-2][Y] == 'H'):
                    world[X-1][Y] = 'U'
                    world[X][Y] = '-'
                    user_position = (X-1, Y)
                    world[X-2][Y] = '-'

    #called when user presses S
    def move_down (self, world, steps=1):
        global user_position, sizeX, sizeY
        target = world[X+1][Y]
        if (target == "W" or target == "H"):
            return False
        else:
            if (target == "F"):
                #TODO END GAME HERE
                pass
            elif (target == "B"):
                pass
            elif (target == "-"):
                pass

    #called when user presses D
    def move_right (self, world, steps=1):
        global user_position, sizeX, sizeY
        target = world[X][Y+1]
        if (target == "W" or target == "H"):
            return False
        else:
            if (target == "F"):
                #TODO END GAME HERE
                pass
            elif (target == "B"):
                pass
            elif (target == "-"):
                pass

    #called when user presses A
    def move_left (self, world, steps=1):
        global user_position, sizeX, sizeY
        target = world[X][Y-1]
        if (target == "W" or target == "H"):
            return False
        else:
            if (target == "F"):
                #TODO END GAME HERE
                pass
            elif (target == "B"):
                pass
            elif (target == "-"):
                pass

    # given the direction (WASD)
    # user moves in the grid (if possible)
    def user_move (self, world, direction):
        if direction == "W":
            move_up(world)
        elif direction == "A":
            move_left(world)
        elif direction == "S":
            move_down(world)
        elif direction == "D":
            move_right(world)
        else: 
            return
        return

