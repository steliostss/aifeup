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
    if len(sys.argv) != 1:
        print('Usage: python3 main.py')
        exit(1)
    checklist = ['a', 's', 'w', 'd', 'r']
    movement = ''
    res = 1
    for i in range(6):
        world = wd.World(5)
        backup_world = copy.deepcopy(world)
        world.print_world()
        while res != 2:
            movement = input("-------------- movement? >> ")
            while len(movement) != 1 or movement not in checklist:
                movement = input("-------------- movement? >> ")
            if movement == 'r' or res == -1 :
                world = copy.deepcopy(backup_world)
                world.print_world()
                continue
            res = fun.move(world, movement)
            world.print_world()
        print("\n!!!!!!!!!!!!!!!!!")
        print("!!!! success !!!!")
        print("!!!!!!!!!!!!!!!!!\n")
        res = 1

if __name__ == "__main__":
    main()