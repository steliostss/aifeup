'''
    Before editing file, read notes.md

'''

import sys

import User as usr
import World as wd
import Functions as fun
import queue
import copy

def main ():

    # check if program is called with the correct arguments
    if len(sys.argv) != 2:
        print('Usage: main.py <level>')
        exit(1)

    movement = ''
    res = 1
    level = sys.argv[1]
    world = wd.World(level,1)
    backup_world = copy.deepcopy(world)
    world.print_world()
    while res != 2:
        movement = input("-------------- movement? >> ")
        while len(movement) != 1:
            movement = input("-------------- movement? >> ")
        if movement == 'r':
            world = copy.deepcopy(backup_world)
            world.print_world()
            continue
        res = fun.move(world, movement)
        world.print_world()
    print("\n\nsuccess!!!!")





if __name__ == "__main__":
    main()