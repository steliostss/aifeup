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
    print('Press 1 to let the program to solve the game')
    print('Press 2 to choose level and algorithm to solve the game')
    print('Press 3 to play the game yourself')
    choice = input('--->>')

    if choice == '1':
        print('Press 1 to solve the game with BFS')
        print('Press 2 to slove the game with DFS')
        choice1 = input('--->>')

        if choice1 == '1':
            best_solutions = [ None for line in range(0,7) ]
            for i in range(1,7):
                world = wd.World(i)
                list_world = [ world ]
                best_world = alg.DFS(list_world, i)
                best_solutions[i-1] = best_world
    
            # for i in best_solutions:
            #     i[0].print_world()
            for i in best_solutions:
                # print(i)
                print(i[0].path)

                    for i in best_solutions:
                        i.print_world()
        elif choice1=='2':
            best_solutions = [ None for line in range(0,7) ]
            for i in range(1,7):
                world = wd.World(i)
                list_world = [ world ]
                best_world = alg.DFS(list_world, i)
                best_solutions[i-1] = best_world

            # for i in best_solutions:
            #     i[0].print_world()
            for i in best_solutions:
                # print(i)
                print(i[0].path)
    elif choice == '2':
        pass
    elif choice == '3':
        checklist = ['a', 's', 'w', 'd', 'r']
        movement = ''
        levels = 6
        res = 1
        i = 1
        lives = 3
        restart = False
        while i <= levels: 
            world = wd.World(i, lives)
            #list_world = [ world ]
            backup_world = copy.deepcopy(world)
            world.print_world()
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

            if res == 2 and not restart:
                print("\n!!!!!!!!!!!!!!!!!")
                print("!!!! success !!!!")
                print("!!!!!!!!!!!!!!!!!\n")
                i += 1
            res = 1


        else:
            print('Exiting..')



if __name__ == "__main__":
    main()
