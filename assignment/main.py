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
    levels = 6
    res = 1
    i = 1
    lives = 3
    moves = 0
    restart = False
    while i <= levels:
        if restart == True:
            lives = 4
        world = wd.World(i, lives)
        backup_world = copy.deepcopy(world)
        world.print_world()
        print ("\n*** LIVES : ", world.lives, " MOVES: ", moves, "***\n")
        restart = False

        while res != 2:
            movement = input("-------------- movement? >> ")
            while (len(movement) != 1 or movement not in checklist) and not restart:
                movement = input("-------------- movement? >> ")
            if movement == 'r' or res == -1 :
                world.lives -= 1
                if world.lives > 0:
                    lives = world.lives
                    world = copy.deepcopy(backup_world)
                    world.lives = lives
                    world.print_world()
                    print ("\n*** LIVES : ", world.lives, " MOVES: ", moves, "***\n")
                    restart = False
                    continue
                else:
                    i = 1
                    print("---------DEAD---------")
                    print()
                    print("You have to start again from level 1. Sorry")
                    restart = True
                    break

            res = fun.move(world, movement)
            world.print_world()
            if res == 1:
                moves += 1
            print ("\n*** LIVES : ", world.lives, " MOVES: ", moves, "***\n")
        
        if res == 2 and not restart:
            print("\n!!!!!!!!!!!!!!!!!")
            print("!!!! success !!!!")
            print("!!!!!!!!!!!!!!!!!\n")
            i += 1
            lives += 1
            moves=0
        res = 1

if __name__ == "__main__":
    main()