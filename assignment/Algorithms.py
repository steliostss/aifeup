import queue  
import User as usr
import World as wd
import sys
import Functions as fun
import copy


def DFS(world):

    my_stack = [] 
    best_path = sys.maxsize

    x,y = world.userposition
    direction = sys.random(world.available_movements[x][y]) #Chooses an direction from the available ones
    world.available_movements.remove(direction) #Removes this movement from the available ones because we are going to use it now
    new_world = copy.deepcopy(world)                 #Create a copy of the our world in order to execute the movement at the new copy 
    my_stack.append(world)                          #Add the previous instance of the world in the stack in case we want to backtrack later

    while (not my_stack): #If there are still instances of the world inside the stack continue trying to reach the end

        result = fun.move(new_world, direction)     #Checks to see if we can make the movement we wanted at the selected direction

        if result == 0 or result == -1 :                                    #If the movement is failed 
            if  world.available_movements[x][y].empty:                   #check if there aren't available movements left
               world = my_stack.pop()                                    #and remove the world instance from the stack
            else:                                                           #else
                direction = sys.random(world.available_movements[x][y])  #try another available movement
                world.available_movements.remove(direction)              #and remove it from the available
        elif result == 2:                                                   #if the result is 2 it means it has reached the end
            if len(new_world.path) < best_path:                             #then save this world as the best available path yet
                best_world = new_world                                      #if there is a smaller path discovered
                best_path = len(new_world.path)                             #update the best world and path
        elif result == 1:                                                   #if the movement was successfull, it means the user has been moved
            x,y = world.userposition                                     #so we get the new position of the user
            direction = sys.random(world.available_movements[x][y])      #choose an available movement for the new user position
            world.available_movements.remove(direction)                  #remove that movement for the available ones 
            new_world = copy.deepcopy(world)                             #create copy of the world to the execute the movement
            my_stack.append(new_world)                                      #add this new istance to the stack


    best_world.printWorld()

def BFS(world):
    
    my_queue = []
    my_queue.append(world) #We add the first instance of the world in the queue as it is already visited
    best_path = sys.maxsize
    index=0                              

    while (index != (len(my_queue)-1)):  

        new_world=copy.deepcopy(my_queue[index])  #We return to the "father node" which is the last element in the queue
        x,y = new_world.userposition

        while not new_world.available_movements[x][y].empty:            #While there are available movements continue 
            x,y = new_world.userposition                                
            direction = sys.random(new_world.available_movements[x][y]) #We choose on available movement 
            new_world.available_movements.remove(direction)             #and we remove it from the list and
            temp_world = copy.deepcopy(new_world)                       #make a backup of the world without any new movements
            result = fun.move(new_world, direction)                     #then we make the movement
            if result == 1 or result ==2:                               #if the movement is successful
                my_queue.append(new_world)                              #we add to the queue the new instance of the world because the "child node" is visited
                if result == 2:                                         #if the result is 2 means that we found the end of the path         
                    if len(new_world.path) < best_path:                 #we compare the path if it is better than the previously found         
                        best_world = new_world                          #and we save the world as the best one yet           
                        best_path = len(new_world.path)                 #same with its path
            new_world=temp_world                                        #then we return to the previous instance to the world 
                                                                        #to try the rest of the available movements
        index +=1                                                       
            
        
def IDDFS(world):  #In theory it should work

    max_depth=0
    find_end='false'

    my_stack = [] 
    best_path = sys.maxsize

    while find_end=='false':
        current_depth = 0                                   #The depth we are currently

        x,y = world.userposition
        direction = sys.random(world.available_movements[x][y]) #Chooses an direction from the available ones
        world.available_movements.remove(direction)         #Removes this movement from the available ones because we are going to use it now
        new_world = copy.deepcopy(world)                 #Create a copy of the our world in order to execute the movement at the new copy 
        my_stack.append(world)

        while current_depth != max_depth:           

            current_depth += 1
            result = fun.move(new_world, direction)     #Checks to see if we can make the movement we wanted at the selected direction

            if result == 0 or result == -1 :                                    #If the movement is failed 
                if  world.available_movements[x][y].empty:                   #check if there aren't available movements left
                    world = my_stack.pop()                                    #and remove the world instance from the stack
                else:                                                           #else
                    direction = sys.random(world.available_movements[x][y])  #try another available movement
                    world.available_movements.remove(direction)              #and remove it from the available
            elif result == 2:                                                   #if the result is 2 it means it has reached the end
                find_end='true'
            elif result == 1:                                                   #if the movement was successfull, it means the user has been moved
                x,y = world.userposition                                     #so we get the new position of the user
                direction = sys.random(world.available_movements[x][y])      #choose an available movement for the new user position
                world.available_movements.remove(direction)                  #remove that movement for the available ones 
                new_world = copy.deepcopy(world)                             #create copy of the world to the execute the movement
                my_stack.append(new_world)

        max_depth += 1