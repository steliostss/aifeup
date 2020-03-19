import World as wd

def switch_case (first, second):
    switcher = {
        "user"   : 'U' ,
        "box"    : 'B' ,
        "ice"    : 'I' ,
        "hole"   : 'H' ,
        "wall"   : 'W' ,
        "finish" : 'F' ,
        "space"  : '-'
    }
    first = switcher.get(first, "error")
    second = switcher.get(second, "error")
    action_func = first+"_and_"+second
    return action_func

def update_positions(world, myP, myT, 
                    nextP, nextT, 
                    nextNextP, nextNextT, ):
    # given myPositon and myType, nextPosition and nextType
    # this function does 3 things:
    # 1. change current position to empty space
    world.map[myP[0], myP[1]] = '-'
    # 2. change nextPosition to myType
    world.map[nextP[0], nextP[1]] = myT
    # 3. change nextNextPosition to nextType
    world.map[nextNextP[0], nextNextP[1]] = nextT

def update_user_position (world, direction):
    x, y = world.position
    if   (direction == 'W'):
        world.position = (x-1, y)
    elif (direction == 'S') :
        world.position = (x+1, y)
    elif (direction == 'A'):
        world.position = (x, y-1)
    else: # direction = 'D'
        world.position = (x, y+1)

def user_and_space (world, direction):
    pass

def user_and_box (world, direction):
    pass

def user_and_finish (world, direction):
    pass

def user_and_ice (world, direction):
    pass

def user_and_wall (world, direction):
    pass

def user_and_hole (world, direction):
    pass

def box_and_wall (world, direction):
    pass

def box_and_hole (world, direction):
    pass

def ice_and_wall (world, direction):
    pass

def ice_and_hole (world, direction):
    pass

