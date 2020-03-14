'''
    Before editing file, read notes.md

    # TODO 
    # track moves & pushes

'''

import User as usr
import World as wd

def main ():
    
    # check if program is called with the correct arguments
    if len(sys.argv) != 2:
        print('Usage: main.py level')
        exit(1)
        
    level = sys.argv[1]
    world = wd.World(level)
    world.print_world()

if __name__ == "__main__":
    main()