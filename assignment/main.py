# - = Empty
# I = Ice
# U = User
# B = Box 
# W = Wall
# H = Hole
# F = Finish

# TODO 
# track moves & pushes

###################################
# INPUT
# R = Restart Level
# Arrows

class World:

    def __init__(self, lives):
        super().__init__()
        lives = 6

    # read the world line by line
    # give as argument the level you want to play
    def read_world (self, levelid):
        levelid = str(levelid) 
        with open("./levels/level"+levelid+".txt") as f:
            world = [line.split() for line in f]
        return world

    def user_move (self, direction):
        


def main (): 
    world = World.read_world (1) # read world


if __name__ == "__main__":
    main()