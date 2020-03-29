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
    (x,y) = world.userposition
    counter = 0

    res = fun.move(world, 'w')
    print(res)
    world.print_world()
    res = fun.move(world, 'd')
    print(res)
    world.print_world()
    res = fun.move(world, 'w')
    print(res)
    world.print_world()
    res = fun.move(world, 'w')
    print(res)
    world.print_world()
    res = fun.move(world, 'd')
    print(res)
    world.print_world()
    res = fun.move(world, 'd')
    print(res)
    world.print_world()
    res = fun.move(world, 's')
    print(res)
    world.print_world()
    res = fun.move(world, 's')
    print(res)
    world.print_world()
    res = fun.move(world, 'a')
    print(res)
    world.print_world()
    res = fun.move(world, 's')
    print(res)
    world.print_world()
    res = fun.move(world, 's')
    print(res)
    world.print_world()


if __name__ == "__main__":
    main()