# - = Empty
# I = Ice
# U = User
# B = Box 
# W = Wall
# H = Hole
# F = Finish
# Lives

# TODO 
# track moves & pushes

###################################
# INPUT
# R = Restart Level
# Arrows

Lives = 6

# read the world line by line
# give as argument the level you want to play
def read_world (levelid):
    levelid = str(levelid) 
    with open("./levels/level"+levelid+".txt") as f:
        world = [line.split() for line in f]
    return world

world = read_world (1) # read world

for i in world:
    print(i)