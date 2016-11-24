class GameOfLife(object):
    
    def __init__(self, seed):
        self.alive_cells = seed

def generator(seed):
    yield set([])

