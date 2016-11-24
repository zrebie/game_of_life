class GameOfLife(object):
    
    def __init__(self, seed):
        self.alive_cells = seed

    def tick(self):
        return self.alive_cells

def generator(seed):
    game_of_life = GameOfLife(seed)
    yield game_of_life.tick()

