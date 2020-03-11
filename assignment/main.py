import matplotlib as plt

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

def read_world (levelid):
    levelid = str(levelid) 
    with open("./levels/level"+levelid+".txt") as f:
        lines = f.read().splitlines()
    return lines

world = []

lines = read_world (1)

for i in lines:
    world.append(i)

    # for spot in i: 
    #     world.append(spot)

for line in world:
    print (line)