import World as wd
import operator
import Algorithms as alg

def move(list_world, direction): # DONE
    direction_tuple = create_direction_tuple(direction) # based on direction, create the dir_tuple (x,y)
    x , y = tuple(map(sum, zip(list_world[0].userposition, direction_tuple))) # x,y represent the object that the user interacts with
    interaction_object = list_world[0].map[x][y]
    # print("interaction_object: ", interaction_object)
    movement_function = object_interaction_function('U', interaction_object)
    # print("movement_function: ", movement_function)
    
    result = choose_interaction(list_world, movement_function, direction_tuple)
    list_world[0].check_neighbours()
    return result

    # movement_function will return:
    # -1 on restart
    #  0 on failure
    #  1 on success
    #  2 on finish

def choose_interaction(list_world, function, direction): # DONE
    if function == "user_and_space":
        result = user_and_space(list_world, direction)
    elif function == "user_and_finish":
        result = user_and_finish(list_world, direction)
    elif function == "user_and_box":
        result = user_and_box(list_world, direction)
    elif function == "user_and_wall":
        result = user_and_wall(list_world, direction)
    elif function == "user_and_hole":
        result = user_and_hole(list_world, direction)
    elif function == "user_and_ice":
        result = user_and_ice(list_world, direction)
    elif function == "box_and_wall":
        result = box_and_wall(list_world, direction)
    elif function == "box_and_space":
        result = box_and_space(list_world, direction)
    elif function == "box_and_hole":
        result = box_and_hole(list_world, direction)
    elif function == "box_and_box":
        result = box_and_box(list_world, direction)
    elif function == "ice_and_ice":
        result = ice_and_ice(list_world, direction)
    elif function == "box_and_finish":
        result = box_and_finish(list_world, direction)
    elif function == "box_and_ice":
        result = box_and_ice(list_world, direction)
    elif function == "ice_and_wall":
        result = ice_and_wall(list_world, direction)
    elif function == "ice_and_box":
        result = ice_and_box(list_world, direction)
    elif function == "ice_and_box":
        result = ice_and_box(list_world, direction)
    elif function == "ice_and_space":
        result = ice_and_space(list_world, direction)
    elif function == "ice_and_hole":
        result = ice_and_hole(list_world, direction)

    return result

def object_interaction_function(_first, _second): # DONE
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

def create_direction_tuple(_direction): # DONE
    # this function takes as argument the desired direction and then
    # creates a tuple as shown below that will be "added" to the any position
    # affected by the movement and update it with a simple addition
    direction = {
        's' : ( 1 , 0 ) ,
        'w' : (-1 , 0 ) ,
        'a' : ( 0 ,-1 ) ,
        'd' : ( 0 ,1 )
    }
    return direction.get(_direction)

def user_and_space (list_world, _direction): # DONE
    ( x , y ) = list_world[0].userposition
    ( i , j ) = tuple(map(sum, zip( list_world[0].userposition, _direction)))
    list_world[0].map[i][j] = 'U' # fill next position
    list_world[0].map[x][y] = '-' # empty previous position
    list_world[0].userposition = tuple(map(sum, zip(list_world[0].userposition, _direction))) # update position
    list_world[0].path.append(list_world[0].userposition)
    list_world[0].check_neighbours()
    return 1 # = success

def user_and_finish (list_world, _direction):
    ( x , y ) = list_world[0].userposition
    list_world[0].map[x][y] = '-' # empty previous position
    list_world[0].userposition = tuple(map(sum, zip(list_world[0].userposition, _direction))) # update position
    ( x , y ) = list_world[0].userposition
    list_world[0].map[x][y] = 'U' # reach end
    list_world[0].path.append(list_world[0].userposition)
    return 2 # = finish

def user_and_box (list_world, _direction):
    ( i1 , j1 ) = tuple(map(sum, zip( list_world[0].userposition, _direction)))
    ( i2 , j2 ) = tuple(map(sum, zip( ( i1 , j1 )       , _direction)))
    type1 = list_world[0].map[i1][j1]
    type2 = list_world[0].map[i2][j2]
    interaction_function = object_interaction_function(type1, type2)
    result = choose_interaction(list_world, interaction_function, _direction)
    if result == 0:
        return result
    else: # here: most probably if not sure result = 1 and not 2
        result = user_and_space(list_world, _direction) # so call this function to fill the gap
        list_world[0].path.append(list_world[0].userposition)
        list_world[0].check_neighbours()
    return result

def user_and_wall (list_world, _direction):
    return 0
    
def user_and_hole (list_world, _direction):
    return 0

def user_and_ice (list_world, _direction):
    ( i1 , j1 ) = tuple(map(sum, zip( list_world[0].userposition, _direction)))
    ( i2 , j2 ) = tuple(map(sum, zip( ( i1 , j1 )       , _direction)))
    type1 = list_world[0].map[i1][j1] # ice
    type2 = list_world[0].map[i2][j2] # next position
    interaction_function = object_interaction_function(type1, type2)
    result = choose_interaction(list_world, interaction_function, _direction)
    if result == 0:
        return result
    else: # here: most probably if not sure result = 1 and not 2
        result = user_and_space(list_world, _direction) # so call this function to fill the gap
        list_world[0].path.append(list_world[0].userposition)
        list_world[0].check_neighbours()
    return result

def box_and_wall (list_world, _direction):
    return 0

def box_and_space (list_world, _direction):
    ( i1 , j1 ) = tuple(map(sum, zip( list_world[0].userposition, _direction)))
    ( i2 , j2 ) = tuple(map(sum, zip( ( i1 , j1 )       , _direction)))
    list_world[0].map[i1][j1] = '-' # empty previous position
    list_world[0].map[i2][j2] = 'B' # fill next position
    return 1 # = success

def box_and_hole (list_world, _direction):
    ( i1 , j1 ) = tuple(map(sum, zip( list_world[0].userposition, _direction)))
    ( i2 , j2 ) = tuple(map(sum, zip( ( i1 , j1 )       , _direction)))
    list_world[0].map[i1][j1] = '-'
    list_world[0].map[i2][j2] = '-'
    return 1

def box_and_finish (list_world, _direction):
    result = list_world[0].check_finish_condition()
    if result: # we are able to finish
        return 0 # no movement performed
    else:
        return -1 # restart

def box_and_ice (list_world, _direction):
    return 0

def ice_and_finish (list_world, _direction):
    result = list_world[0].check_finish_condition()
    if result: # we are able to finish
        return 0 # no movement performed
    else:
        return -1 # restart

def ice_and_wall (list_world, _direction):
    return 0

def ice_and_box (list_world, _direction):
    return 0

def ice_and_space (list_world, _direction):
    ( i1 , j1 ) = tuple(map(sum, zip( list_world[0].userposition, _direction))) # ice
    ( i2 , j2 ) = tuple(map(sum, zip( ( i1 , j1 )       , _direction))) # space
    ( i3 , j3 ) = tuple(map(sum, zip( ( i2 , j2 )       , _direction))) # next position

    list_world[0].map[i1][j1] = '-' # empty previous position
    
    condition = (0 <= i3 < list_world[0].X and 0 <= j3 < list_world[0].Y)
    while (condition and list_world[0].map[i3][j3] != '-'):

        if list_world[0].map[i3][j3] in ['W','B']:
            list_world[0].map[i2][j2] = 'I' # fill next position
            return 1

        elif list_world[0].map[i3][j3] == 'H':
            list_world[0].map[i2][j2] = '-' # fill next position
            list_world[0].map[i3][j3] = '-'
            return 1

        elif list_world[0].map[i3][j3] == 'F':
            list_world[0].map[i2][j2] = 'I' # fill next position
            return list_world[0].check_finish_condition()

        (i2,j2) = (i3,j3)
        (i3,j3) = tuple(map(sum, zip((i3,j3), _direction)))
        condition = (0 <= i3 < list_world[0].X) and (0 <= j3 < list_world[0].Y)

def ice_and_hole (list_world, _direction):
    ( i1 , j1 ) = tuple(map(sum, zip( list_world[0].userposition, _direction)))
    ( i2 , j2 ) = tuple(map(sum, zip( ( i1 , j1 )       , _direction)))
    list_world[0].map[i1][j1] = '-'
    list_world[0].map[i2][j2] = '-'
    return 1

def box_and_box(list_world, direction):
    return 0

def ice_and_ice(list_world, direction):
    return 0

def initialize2DList(X, Y):
    mylist = []
    for i in range(X):
        mylist.append([])
        for j in range(Y):
            mylist[i].append([])
    return mylist

def compare_maps(map1, map2):
    for i in range(0,len(map1)):
        for j in range(0, len(map1[0])):
            if map1[i][j] != map2[i][j]:
                return False
    return True

def compare_worlds(map1, map2):
    return (compare_maps(map1, map2))

def print_results(results):
    for i in results:
        for algorithm in i:
            print(algorithm[0].path)
            algorithm[0].print_world()
            print(algorithm[0].path)   

def prepare_and_call_BFS():
    best_solutions = [ None for line in range(0,7) ]
    for i in range(1,7):
        world = wd.World(i)
        list_world = [ world ]
        best_world = alg.DFS(list_world, i)
        best_solutions[i-1] = best_world

    return best_solutions

def prepare_and_call_DFS():
    best_solutions = [ None for line in range(0,7) ]
    for i in range(1,7):
        world = wd.World(i)
        list_world = [ world ]
        best_world = alg.DFS(list_world, i)
        best_solutions[i-1] = best_world

    return best_solutions