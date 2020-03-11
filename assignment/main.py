'''
    # - = Empty
    # I = Ice
    # U = User
    # B = Box 
    # W = Wall
    # H = Hole
    # F = Finish

    # TODO 
    # track moves & pushes

    ###################################
    # INPUT
    # R = Restart Level
    # Arrows
'''

# read the world line by line
# give as argument the level you want to play
def read_world (levelid):
    levelid = str(levelid) 
    with open("./levels/level"+levelid+".txt") as f:
        world = [line.split() for line in f]
    return world

def print_world (world):
    for i in world: 
        for item in i: 
            print(item, end=' ')
        print()

def find_user_position(world):
    global user_position, sizeX, sizeY
    i = 0
    while (i < sizeX):
        j = 0
        while j < sizeY:
            if world[i][j] == 'U':
                user_position = (i, j)
                return
            j+=1
        i+=1

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
def move_down (world, steps=1):
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
def move_right (world, steps=1):
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
def move_left (world, steps=1):
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
def user_move (world, direction):
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

def main (): 
    global user_position, sizeX, sizeY
    world = read_world(0) # read world
    print_world(world)

    sizeX = len(world)
    sizeY = len(world[0])
    print (sizeX, sizeY)
    find_user_position(world)
    print (user_position)
    user_move (world, 'W')
    # user_move (world, 'W')
    # user_move (world, 'W')
    # user_move (world, 'W')

    print_world(world)



user_position = (0,0)
sizeX = 0
sizeY = 0
if __name__ == "__main__":
    main()