import queue
import User as usr
import World as wd
import sys
import Functions as fun


def BFS(World):

    my_world = wd.World(0,6)
    my_queue = queue.Queue() 

    while (not finish_condition): #<--the condition that will end the loop needs to be added here

        x,y = my_world.userposition
        my_world.check_neighbours(x,y)
        direction = random(my_world.available_movements)
        my_world.available_movements.remove(direction)
        new_world = my_world.deepcopy()
        my_queue.add(my_world)

        result = fun.move(new_world, direction)

        if != result:
            my_world = my_queue.pop()

    new_world.printWorld()

def DFS(World):
    
    my_world = wd.World(0,6)

            
                 