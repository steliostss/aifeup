import queue
import User as usr
import World as wd
import sys


def printMap(map, moves): #Prints the final map with the path
    for x, pos in enumerate(map[0]):
        if pos == "U":
            start = x

    i = start
    j = 0
    pos = set()
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(map):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("* ", end="")
            else:
                print(col + " ", end="")
        print()
        


def validate(map, moves):  #Checks if it is possible to make to given move
    for x, pos in enumerate(map[0]):
        if pos == "U":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(map[0]) and 0 <= j < len(map)):
            return False
        elif (map[j][i] == "W" or map[j][i] == "H"):
            return False

    return True


def findEnd(map, moves):   #Finds where the end is located
    for x, pos in enumerate(map[0]):
        if pos == "U":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if map[j][i] == "F":
        print("The path is: " + moves)
        printMap(map, moves)
        return True

    return False


# MAIN ALGORITHM

my_queue = queue.Queue() 
my_queue.put("")
possible_paths = ""

my_world = wd.World(0,6)
map = my_world.map

user_position = my_world.userposition
print(user_position)

while not findEnd(map, possible_paths): 
    possible_paths = my_queue.get()
    #print(possible_paths)
    for j in ["L", "R", "U", "D"]:
        test_put = possible_paths + j   #Adds all possible directions to the var
        if validate(map, test_put):     #Checks if that direction is valid if it is
            my_queue.put(test_put)      #we add it to the queue, otherwise we don't

            
                 