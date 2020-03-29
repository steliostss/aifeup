'''
    Before editing file, read notes.md

'''

import sys

import User as usr
import World as wd
import Functions as fun

import queue

def main ():

    # check if program is called with the correct arguments
    if len(sys.argv) != 2:
        print('Usage: main.py <level>')
        exit(1)

    level = sys.argv[1]
    world = wd.World(level,1)
    world.print_world()
    counter = 0

    myq = queue.Queue(maxsize=1000)
    while counter <= 10:
        (x,y) = world.userposition



if __name__ == "__main__":
    main()