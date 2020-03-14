class World:
    def __init__(self, _level):
        self.map = self.read_world(_level)
        self.X = len(self.map)
        self.Y = len(self.map[0])
    
    def print_world (self):
        for i in self.map: 
            for item in i: 
                print(item, end=' ')
            print()

    # read the world line by line
    # give as argument the level you want to play
    def read_world (self, levelid):
        levelid = str(levelid) 
        with open("./levels/level"+levelid+".txt") as f:
            world = [line.split() for line in f]
        return world