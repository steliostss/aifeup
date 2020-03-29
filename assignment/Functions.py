import World as wd
import operator

def move(world, direction):
    direction_tuple = create_direction_tuple(direction) # based on direction, create the dir_tuple (x,y)
    x , y = tuple(map(sum, zip(world.userposition, direction_tuple))) # x,y represent the object that the user interacts with
    interaction_object = world.map[x][y]
    
    movement_function = object_interaction_function('U', interaction_object)
    result = choose_interaction(world, movement_function, direction_tuple)

    return result

    # movement_function will return:
    # -1 on restart
    #  0 on failure
    #  1 on success
    #  2 on finish

def choose_interaction(world, function, direction):
    if function == "user_and_space":
        result = user_and_space(world, direction)
    elif function == "user_and_finish":
        result = user_and_finish(world, direction)
    elif function == "user_and_box":
        result = user_and_box(world, direction)
    elif function == "user_and_wall":
        result = user_and_wall(world, direction)
    elif function == "user_and_hole":
        result = user_and_hole(world, direction)
    elif function == "user_and_ice":
        result = user_and_ice(world, direction)
    elif function == "box_and_wall":
        result = box_and_wall(world, direction)
    elif function == "box_and_space":
        result = box_and_space(world, direction)
    elif function == "box_and_hole":
        result = box_and_hole(world, direction)
    elif function == "box_and_finish":
        result = box_and_finish(world, direction)
    elif function == "box_and_ice":
        result = box_and_ice(world, direction)
    elif function == "ice_and_wall":
        result = ice_and_wall(world, direction)
    elif function == "ice_and_box":
        result = ice_and_box(world, direction)
    elif function == "ice_and_box":
        result = ice_and_box(world, direction)
    elif function == "ice_and_space":
        result = ice_and_space(world, direction)
    elif function == "ice_and_hole":
        result = ice_and_hole(world, direction)

    return result

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

def user_and_space (world, _direction): # done
    ( x , y ) = world.userposition
    ( i , j ) = tuple(map(sum, zip( world.userposition, _direction)))
    world.map[i][j] = 'U' # fill next position
    world.map[x][y] = '-' # empty previous position
    world.userposition = tuple(map(sum, zip(world.userposition, _direction))) # update position
    world.path.append(world.userposition)
    world.check_neighbours()
    return 1 # = success

def user_and_finish (world, _direction): # done
    ( x , y ) = world.userposition
    world.map[x][y] = '-' # empty previous position
    world.userposition = tuple(map(sum, zip(world.userposition, _direction))) # update position
    ( x , y ) = world.userposition
    world.map[x][y] = 'U' # reach end
    world.path.append(world.userposition)
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
        world.path.append(world.userposition)
        world.check_neighbours()
    return result

def user_and_wall (world, _direction): # done
    return 0
    
def user_and_hole (world, _direction): # done
    return 0

def user_and_ice (world, _direction): # done
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
        world.path.append(world.userposition)
        world.check_neighbours()
    return result

def box_and_wall (world, _direction): # done
    return 0

def box_and_space (world, _direction): # 
    ( i1 , j1 ) = tuple(map(sum, zip( world.userposition, _direction)))
    ( i2 , j2 ) = tuple(map(sum, zip( ( i1 , j1 )       , _direction)))
    world.map[i1][j1] = '-' # empty previous position
    world.map[i2][j2] = 'B' # fill next position
    return 1 # = success

def box_and_hole (world, _direction): # done
    ( i1 , j1 ) = tuple(map(sum, zip( world.userposition, _direction)))
    ( i2 , j2 ) = tuple(map(sum, zip( ( i1 , j1 )       , _direction)))
    world.map[i1][j1] = '-'
    world.map[i2][j2] = '-'
    return 1

def box_and_finish (world, _direction): # done
    (i,j) = tuple(map(sum, zip(world.userposition, _direction))) # ice
    result = world.check_finish_condition((i,j), _direction)
    if result: # we are able to finish
        return 0 # no movement performed
    else:
        return -1 # restart

def box_and_ice (world, _direction): # done
    return 0

def ice_and_finish (world, _direction): # done
    (i,j) = tuple(map(sum, zip(world.userposition, _direction))) # ice
    result = world.check_finish_condition((i,j), _direction)
    if result: # we are able to finish
        return 0 # no movement performed
    else:
        return -1 # restart

def ice_and_wall (world, _direction): # done
    return 0

def ice_and_box (world, _direction): # done
    return 0

def ice_and_space (world, _direction): # done
    ( i1 , j1 ) = tuple(map(sum, zip( world.userposition, _direction))) # ice
    ( i2 , j2 ) = tuple(map(sum, zip( ( i1 , j1 )       , _direction))) # space
    ( i3 , j3 ) = tuple(map(sum, zip( ( i2 , j2 )       , _direction))) # space

    world.map[i1][j1] = '-' # empty previous position
    
    condition = (0 <= i3 < world.X and 0 <= j3 < world.Y)
    while (condition and world.map[i3][j3] != '-'):
        
        if world.map[i3][j3] in ['W','B']:
            world.map[i2][j2] = 'I' # fill next position
            result = 1

        elif world.map[i3][j3] == 'H':
            world.map[i2][j2] = '-' # fill next position
            world.map[i3][j3] = '-'
            result = 1

        elif world.map[i3][j3] == 'F':
            world.map[i2][j2] = 'I' # fill next position
            result = world.check_finish_condition((i2,j2))

        (i2,j2) = (i3,j3)
        (i3,j3) = tuple(map(sum, zip((i3,j3), _direction)))
        condition = (0 <= i3 < world.X) and (0 <= j3 < world.Y)

    return result # = success

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
