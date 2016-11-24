class GameOfLife(object):
    
    def __init__(self, seed):
        self.alive_cells = seed

    def tick(self):
        return self.alive_cells

def generator(seed):
    yield set([])

