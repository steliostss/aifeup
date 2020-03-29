import queue
import User as usr
import World as wd
import sys
import Functions as fun


def DFS(World):

    my_world = wd.World(0,6)
    my_queue = queue.Queue() 
    best_path = sys.maxsize

    x,y = my_world.userposition
    direction = sys.random(my_world.available_movements[x][y])
    my_world.available_movements.remove(direction)
    new_world = my_world.deepcopy()
    my_queue.add(my_world)

    while (not my_queue.empty): #<--the condition that will end the loop needs to be added here

        result = fun.move(new_world, direction)

        if result == 0 or result == -1 :
            my_world = my_queue.pop()
        elif result == 2:
            if len(new_world.path) < best_path:
                best_world = new_world
                best_path = len(new_world.path)

        x,y = my_world.userposition
        direction = sys.random(my_world.available_movements[x][y])
        my_world.available_movements.remove(direction)
        new_world = my_world.deepcopy()
        my_queue.add(my_world)


    new_world.printWorld()

def BFS(World):
    
    my_world = wd.World(0,6)

            
                 