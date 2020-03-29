import World as wd
import operator

def move(world, direction, steps=1):
    direction_tuple = create_direction_tuple(direction) # based on direction, create the dir_tuple (x,y)
    x , y = tuple(map(sum, zip(world.userposition, direction_tuple))) # x,y represent the object that the user interacts with
    interaction_object = world.map[x][y]
    
    movement_function = object_interaction_function('U', interaction_object)
    result = movement_function(world, direction_tuple)

    return result

    # movement_function will return:
    # 0 on failure
    # 1 on success
    # 2 on finish

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

def user_and_space (world, _direction): # done
    ( x , y ) = world.userposition
    ( i , j ) = tuple(map(sum, zip( world.userposition, _direction)))
    world.map[i][j] = 'U' # fill next position
    world.map[x][y] = '-' # empty previous position
    world.userposition = tuple(map(sum, zip(world.userposition, _direction))) # update position
    return 1 # = success

def user_and_finish (world, _direction): # done
    ( x , y ) = world.userposition
    world.map[x][y] = '-' # empty previous position
    world.userposition = tuple(map(sum, zip(world.userposition, _direction))) # update position
    ( x , y ) = world.userposition
    world.map[x][y] = 'U' # reach end
    return 2 # = finish

def user_and_box (world, _direction): # done
    ( i1 , j1 ) = tuple(map(sum, zip( world.userposition, _direction)))
    ( i2 , j2 ) = tuple(map(sum, zip( ( i1 , j1 )       , _direction)))
    type1 = world.map[i1][j1]
    type2 = world.map[i2][j2]

    interaction_function = object_interaction_function(type1, type2)
    result = interaction_function(world, _direction)
    if result == 0:
        return result
    else: # here: most probably if not sure result = 1 and not 2
        result = user_and_space(world, _direction) # so call this function to fill the gap
    return result

def user_and_wall (world, _direction): # done
    return 0
    
def user_and_hole (world, _direction): # done
    return 0

def user_and_ice (world, _direction): # 
    ( i1 , j1 ) = tuple(map(sum, zip( world.userposition, _direction)))

def box_and_wall (world, _direction): # done
    return 0

def box_and_hole (world, _direction): # done
    ( i1 , j1 ) = tuple(map(sum, zip( world.userposition, _direction)))
    ( i2 , j2 ) = tuple(map(sum, zip( ( i1 , j1 )       , _direction)))
    world.map[i1][j1] = '-'
    world.map[i2][j2] = '-'
    return 1

def box_and_finish (world, _direction): # done
    return 1

def ice_and_finish (world, _direction): # done
    return 0

def ice_and_wall (world, _direction): # done
    return 0

def ice_and_space (world, _direction): #
    pass

def ice_and_hole (world, _direction): # done
    ( i1 , j1 ) = tuple(map(sum, zip( world.userposition, _direction)))
    ( i2 , j2 ) = tuple(map(sum, zip( ( i1 , j1 )       , _direction)))
    world.map[i1][j1] = '-'
    world.map[i2][j2] = '-'
    return 1

def initialize2DList(X, Y):
    mylist = []
    for i in range(X):
        mylist.append([])
        for j in range(Y):
            mylist[i].append([])
    return mylist
