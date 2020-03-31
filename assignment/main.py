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
    while 1:
        print('Press 1 to let AI solve the game.')
        print('Press 2 to play the game yourself.')
        print('Press e to exit.')
        choice = input('--->> ')

        if choice == '1':
            print("Wait...")
            print("If waiting period exceed 1 minute, press CTRL+C and restart.")
            result_BFS = fun.prepare_and_call_BFS()
            result_DFS = fun.prepare_and_call_DFS()
            results = [result_BFS, result_DFS]
            # results = [result_BFS]
            fun.print_results(results)
        elif choice == '2':
            fun.work_with_input()
        elif choice == 'e':
            print("Bye.")
            quit()
        else:
            print("Retry.")
            print()

if __name__ == "__main__":
    main()
