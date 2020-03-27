class User: 
    #called when user presses W
    def move_up (world, steps=1):
        global user_position, sizeX, sizeY
        X, Y = user_position
        target = world[X-1][Y]
        if (target == "W" or target == "H"):
            return False
        else:
            if (target == "F"):
                #TODO END GAME HERE
                pass
            elif (target == "-"):
                world[X-1][Y] = 'U'
                world[X][Y] = '-'
                user_position = (X-1, Y)            
            else: # target == "B"
                if (X-2 >= 0):
                    if (world[X-2][Y] == '-'):
                        world[X-1][Y] = 'U'
                        world[X][Y] = '-'
                        user_position = (X-1, Y)
                        world[X-2][Y] = 'B'
                    elif (world[X-2][Y] == 'H'):
                        world[X-1][Y] = 'U'
                        world[X][Y] = '-'
                        user_position = (X-1, Y)
                        world[X-2][Y] = '-'

    #called when user presses S
    def move_down (self, world, steps=1):
        global user_position, sizeX, sizeY
        target = world[X+1][Y]
        if (target == "W" or target == "H"):
            return False
        else:
            if (target == "F"):
                #TODO END GAME HERE
                pass
            elif (target == "B"):
                pass
            elif (target == "-"):
                pass

    #called when user presses D
    def move_right (self, world, steps=1):
        global user_position, sizeX, sizeY
        target = world[X][Y+1]
        if (target == "W" or target == "H"):
            return False
        else:
            if (target == "F"):
                #TODO END GAME HERE
                pass
            elif (target == "B"):
                pass
            elif (target == "-"):
                pass

    #called when user presses A
    def move_left (self, world, steps=1):
        global user_position, sizeX, sizeY
        target = world[X][Y-1]
        if (target == "W" or target == "H"):
            return False
        else:
            if (target == "F"):
                #TODO END GAME HERE
                pass
            elif (target == "B"):
                pass
            elif (target == "-"):
                pass

    # given the direction (WASD)
    # user moves in the grid (if possible)
    def user_move (self, world, direction):
        if direction == "s":
            move_up(world)
        elif direction == "a":
            move_left(world)
        elif direction == "s":
            move_down(world)
        elif direction == "d":
            move_right(world)
        else: 
            return
        return

