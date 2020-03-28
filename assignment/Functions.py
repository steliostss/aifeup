import World as wd
import operator

def move(world, direction, steps=1):
    X, Y = world.userposition
    targetX = X
    targetY = Y
    movement = world.decide_move(direction)
    
    # TODO: 
    # return movement(steps)
    # movement function will return True on success of False on Failure

def object_interaction_function(_first, _second):
    switcher = {
        'U' : "user"   ,
        'B' : "box"    ,
        'I' : "ice"    ,
        'H' : "hole"   ,
        'W' : "wall"   ,
        'F' : "finish" ,
        '-' : "space"
    }
    first = switcher.get(_first, "error")
    second = switcher.get(_second, "error")
    action_func = first+"_and_"+second
    return action_func

def create_direction_tuple(_direction):
    # this function takes as argument the desired direction and then
    # creates a tuple as shown below that will be "added" to the any position
    # affected by the movement and update it with a simple addition
    direction = {
        's' : ( 1 , 0 ) ,
        'w' : (-1 , 0 ) ,
        'a' : ( 0 , 1 ) ,
        'd' : ( 0 ,-1 )
    }
    return direction.get(_direction)

def update_positions(myP, myT,
                     nextP, nextT,
                     nextNextP, nextNextT):
    # given myPositon and myType, nextPosition and nextType
    # this function does 3 things:
    # 1. change current position to empty space
    world.map[myP[0], myP[1]] = '-'
    # 2. change nextPosition to myType
    world.map[nextP[0], nextP[1]] = myT
    # 3. change nextNextPosition to nextType
    world.map[nextNextP[0], nextNextP[1]] = nextT

def update_user_position (world, direction):
    world.userposition = tuple(map(sum, zip(world.userposition, direction)))
    return

def user_and_space (world, _direction):
    ( x , y ) = world.userposition
    direction_tuple = create_direction_tuple(_direction)
    world.map[x][y] = '-' # empty previous position
    update_user_position(world, direction_tuple) # update position
    ( x , y ) = world.userposition
    world.map[x][y] = 'U' # fill next
    return True

def user_and_box (world, _direction):
    ( x , y ) = world.userposition
    direction_tuple = create_direction_tuple(_direction)
    
def user_and_finish (world, _direction):
    ( x , y ) = world.userposition
    direction_tuple = create_direction_tuple(_direction)

def user_and_ice (world, _direction):
    ( x , y ) = world.userposition
    direction_tuple = create_direction_tuple(_direction)

def user_and_wall (world, _direction):
    return False
    
def user_and_hole (world, _direction):
    ( x , y ) = world.userposition
    direction_tuple = create_direction_tuple(_direction)

def box_and_wall (world, _direction):
    return False

def box_and_hole (world, _direction):
    ( x , y ) = world.userposition
    direction_tuple = create_direction_tuple(_direction)
    pass

def ice_and_wall (world, _direction):
    return False

def ice_and_space (world, _direction):
    pass

def ice_and_hole (world, _direction):
    ( x , y ) = world.userposition
    direction_tuple = create_direction_tuple(_direction)

def initialize2DList(X, Y):
    mylist = []
    for i in range(X):
        mylist.append([])
        for j in range(Y):
            mylist[i].append([])
    return mylist
