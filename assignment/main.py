'''
    Before editing file, read notes.md

    # TODO 
    # track moves & pushes

'''

import sys

import User as usr
import World as wd
import Functions as fun

def main ():

    # check if program is called with the correct arguments
    if len(sys.argv) != 2:
        print('Usage: main.py <level>')
        exit(1)

    level = sys.argv[1]
    world = wd.World(level,6)
    world.print_world()
    print("position is: ", world.userposition)
    # fun.user_and_space(world,'w')
    # print("going up")
    # world.print_world()
    # print("position is: ", world.userposition)

if __name__ == "__main__":
    main()