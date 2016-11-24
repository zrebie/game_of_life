class GameOfLife(object):

    def __init__(self, seed):
        self.alive_cells = seed

    def tick(self):
        next_generation = set()
        for cell in self.alive_cells:
            if len(self.get_alive_neighbours(cell)) in [2,3]:
                next_generation.add(cell)
        self.alive_cells = next_generation
        return self.alive_cells

    def get_births(self):
        return set([cell for cell in self.get_birth_candidates() if len(self.get_alive_neighbours(cell))==3])

    def get_birth_candidates(self):
        birth_candidates = set()
        for cell in self.alive_cells:
            birth_candidates = birth_candidates.union(self.get_dead_neighbours(cell))
        return birth_candidates
    
    def get_alive_neighbours(self, cell):
        alive_neighbours = set()
        for neighbour in self.get_neighbours(cell):
            if neighbour in self.alive_cells:
                alive_neighbours.add(neighbour)
        return alive_neighbours

    def get_dead_neighbours(self, cell):
        alive_neighbours = set()
        for neighbour in self.get_neighbours(cell):
            if neighbour not in self.alive_cells:
                alive_neighbours.add(neighbour)
        return alive_neighbours

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

