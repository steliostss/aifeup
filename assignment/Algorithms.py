import queue  
import User as usr
import World as wd
import sys
import Functions as fun
import copy
import random

def DFS(list_world):
    my_stack = [] 
    best_path = sys.maxsize                                     # biggest available integer
    x,y = list_world[0].userposition
    direction = random.choice(list_world[0].available_movements[x][y])  # Chooses an direction from the available ones
    list_world[0].available_movements[x][y].remove(direction)           # Removes this movement from the available ones because we are going to use it now
    new_world = copy.deepcopy(list_world)                            # Create a copy of the our world in order to execute the movement at the new copy 
    my_stack.append(list_world)                                      # Add the previous instance of the world in the stack in case we want to backtrack later

    while (my_stack):                                           # If there are still instances of the world inside the stack continue trying to reach the end

        result = fun.move(new_world, direction)                 # Checks to see if we can make the movement we wanted at the selected direction

        if result == 0 or result == -1 :                                    # If the movement failed 
            if not list_world[0].available_movements[x][y]:                         # check if there aren't available movements left
                try:
                    new_world = my_stack.pop()                              # and remove the world instance from the stack                    
                except IndexError as err :
                    print(err, ": empty stack")
                    break
            else:
                direction = random.choice(list_world[0].available_movements[x][y])  # try another available movement
                list_world[0].available_movements[x][y].remove(direction)           # and remove it from the available
        elif result == 2:      
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            list_world[0].print_world()                                             # if the result is 2 it means it has reached the end
            if len(new_world[0].path) < best_path:                             # then save this world as the best available path yet
                best_world = copy.copy(new_world)                           # if there is a smaller path discovered
                best_path = len(new_world[0].path)                             # update the best world and path
            try:
                new_world = my_stack.pop()                                  # and remove the world instance from the stack                    
            except IndexError as err :
                print(err, ": empty stack")
                break
        elif result == 1:                                                   # if the movement was successfull, it means the user has been moved
            # print(x,y)
            x,y = list_world[0].userposition                                        # so we get the new position of the user
            list_world[0].check_neighbours()
            direction = random.choice(list_world[0].available_movements[x][y])      # choose an available movement for the new user position
            list_world[0].available_movements[x][y].remove(direction)               # remove that movement for the available ones 
            list_world[0].print_world()
            new_world = copy.deepcopy(list_world)                                # create copy of the world to the execute the movement
            new_world = check_and_add_node(new_world, my_stack)         # add this new istance to the stack

    return best_world

def BFS(list_world):
    queue = []
    queue.append(list_world)                              # We add the first instance of the world in the queue as it is already visited
    best_path = sys.maxsize
    index=0                              

    while index != (len(queue)-1):  

        new_world = copy.deepcopy(queue[index])        # We return to the "father node" which is the last element in the queue
        x,y = new_world[0].userposition

        while not new_world[0].available_movements[x][y]:  # While there are available movements continue 
            x,y = new_world[0].userposition
            direction = random.choice(new_world[0].available_movements[x][y])  # We choose on available movement 
            new_world[0].available_movements[x][y].remove(direction)           # and we remove it from the list and
            temp_world = copy.deepcopy(new_world)                           # make a backup of the world without any new movements
            result = fun.move(new_world, direction)                         # then we make the movement

            if result == 0 or result == -1 :
                if not new_world[0].available_movements[x][y]:
                    del queue[index]                        # delete the object to save "memory"
                    index -= 1                              # move index back to be incremented again out of the loop
                    break
                else:
                    pass                                    # you still have available moves but movement was not succesful
            elif result == 1 :
                temp = copy.deepcopy(new_world)
                check_and_add_node(temp, queue)  # succesful movement, add to queue go on to next available
            elif result == 2 :
                if len(new_world[0].path) < best_path:     # we compare the path if it is better than the previously found
                    best_world = copy.copy(new_world)                           # if there is a smaller path discovered
                    best_path = len(new_world[0].path)                             # update the best world and path
        index += 1
    return best_world[0]

'''
this function checks if there is an existing world in the struct
if there isn't then it add the new list_world[0].
if there is then it returns the existing
'''
def check_and_add_node(temp, struct):
    for i in range(0, len(struct)):
        position1 = temp[0].struct[i].userposition
        position2 = struct[i][0].userposition
        map1 = temp[0].struct[i].map
        map2 = struct[i][0].map
        result = fun.compare_worlds(position1, position2, map1, map2)
        if result:
            temp[0] = struct[i][0]
            break
    if not result:
        struct.append(temp[0])
    return temp

def work_with_input():
    checklist = ['a', 's', 'w', 'd', 'r']
    movement = ''
    levels = 6
    res = 1
    i = 1
    lives = 3
    moves = 0
    restart = False
    while i <= levels:
        if restart == True:
            lives = 4
        world = wd.World(i, lives)
        backup_world = copy.deepcopy(list_world[0])
        list_world[0].print_world()
        print ("\n*** LIVES : ", list_world[0].lives, " MOVES: ", moves, "***\n")
        restart = False

        while res != 2:
            movement = input("-------------- movement? >> ")
            while (len(movement) != 1 or movement not in checklist) and not restart:
                movement = input("-------------- movement? >> ")
            if movement == 'r' or res == -1 :
                list_world[0].lives -= 1
                if list_world[0].lives > 0:
                    lives = list_world[0].lives
                    world = copy.deepcopy(backup_world)
                    list_world[0].lives = lives
                    list_world[0].print_world()
                    print ("\n*** LIVES : ", list_world[0].lives, " MOVES: ", moves, "***\n")
                    restart = False
                    continue
                else:
                    i = 1
                    print("---------DEAD---------")
                    print()
                    print("You have to start again from level 1. Sorry")
                    restart = True
                    break

            res = fun.move(world, movement)
            list_world[0].print_world()
            if res == 1:
                moves += 1
            print ("\n*** LIVES : ", list_world[0].lives, " MOVES: ", moves, "***\n")
        
        if res == 2 and not restart:
            print("\n!!!!!!!!!!!!!!!!!")
            print("!!!! success !!!!")
            print("!!!!!!!!!!!!!!!!!\n")
            i += 1
            lives += 1
            moves=0
        res = 1

def Greedy_Search(lsit_world):
    pass


