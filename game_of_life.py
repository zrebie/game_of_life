class GameOfLife(object):

    def __init__(self, seed):
        self.alive_cells = seed

    def tick(self):
        self.alive_cells = set()
        return self.alive_cells

    def get_alive_neighbours(self, cell):
        return set()

    @staticmethod
    def get_neighbours(cell):
        neighbours = set()
        deltas = set([(-1, -1), (0, -1), (1, -1),
                      (-1,  0),          (1,  0),
                      (-1,  1), (0,  1), (1,  1)])
        for dx, dy in deltas:
            neighbours_cell = (cell[0]+dx, cell[1]+dy)
            neighbours.add(neighbours_cell)
        return neighbours

def generator(seed):
    game_of_life = GameOfLife(seed)
    yield game_of_life.tick()

