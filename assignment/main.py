'''
    Before editing file, read notes.md

'''

import sys

import User as usr
import World as wd
import Functions as fun
import queue
import copy
import Algorithms as alg

def main ():

    # check if program is called with the correct arguments
    if len(sys.argv) != 1:
        print('Usage: python3 main.py')
        exit(1)
    # work_with_input()
    best_solutions = [ None for line in range(1,7) ]
    for i in range(1,7):
        world = wd.World(i)
        list_world = [ world ]
        best_world = alg.DFS(list_world, i)
        best_solutions[i] = best_world
    
    for i in best_solutions:
        i[0].print_world()

if __name__ == "__main__":
    main()