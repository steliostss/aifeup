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

# given the direction (WASD)
# user moves in the grid (if possible)
def user_move (direction):
    pass    

def main (): 
    world = read_world(0) # read world
    print_world(world)

    sizeX = len(world)
    sizeY = len(world[0])
    print (sizeX, sizeY)

if __name__ == "__main__":
    main()