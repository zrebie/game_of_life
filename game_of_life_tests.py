import unittest
from game_of_life import GameOfLife, generator

class TestGameOfLife(unittest.TestCase):

    def test_game_of_life_object_initialization(self):
        # GIVEN
        seed = set([])
        # WHEN
        game_of_life = GameOfLife(seed)
        # THEN
        self.assertEqual(game_of_life.alive_cells, seed)
    
    def test_game_of_life_empty_tick(self):
        # GIVEN
        seed = set()
        game_of_life = GameOfLife(seed)
        # WHEN
        next_generation = game_of_life.tick()
        # THEN
        self.assertEqual(next_generation, seed)

    def test_empty_seed_generation(self):
        """
        ...
        ...
        ...
        
        =>
        
        ...
        ...
        ...
        """
        # GIVEN
        seed = set([])
        expected = set([])
        # WHEN
        next_generation = next(generator(seed))
        # THEN
        self.assertEqual(next_generation, expected)
# 
#     def test_tick_block_should_survive(self):
#         """
#         **
#         **
#         =>
#         **
#         **
#         """
#         # GIVEN
#         seed = set([(0,0), (0,1),(1,0),(1,1)])
#         expected = seed
#         game_of_life = GameOfLife(seed)
#         # WHEN & THEN
#         self.assertEqual(game_of_life.tick(), expected)
    
    def test_should_return_correct_neighbours(self):
        # GIVEN
        cell = (0,0)
        expected_len = 8
        expected_neighbours = set([(-1,-1), (0,-1), (1, -1),
                                   (-1,0),     (1, 0),
                                   (-1,1), (0,1), (1, 1)])
        # WHEN
        neighbours = GameOfLife.get_neighbours(cell)
        # THEN
        self.assertEqual(expected_len, len(neighbours))
        self.assertEqual(expected_neighbours, neighbours)

    def test_should_return_correct_neighbours_any_cell(self):
        # GIVEN
        cell = (14,3)
        expected_len = 8
        expected_neighbours = set([(13,2), (14,2), (15, 2),
                                   (13,3),     (15, 3),
                                   (13,4), (14,4), (15, 4)])
        # WHEN
        neighbours = GameOfLife.get_neighbours(cell)
        # THEN
        self.assertEqual(expected_len, len(neighbours))
        self.assertEqual(expected_neighbours, neighbours)

    def test_should_return_empty_set_of_alive_neighbours_of_cell(self):
        # GIVEN
        seed = set((-1,-1))
        game_of_life = GameOfLife(seed)
        cell = (0,0)
        expected_len = 0
        expected_neighbours = set()
        # WHEN
        alive_neighbours = game_of_life.get_alive_neighbours(cell) 
        # THEN
        self.assertEqual(expected_len, len(alive_neighbours))
        self.assertEqual(expected_neighbours, alive_neighbours)

    def test_tick_with_one_cell_dies(self):
        # GIVEN
        seed = set([(0,0)])
        expected_1 = set()
        expected_2 = set()
        game_of_life = GameOfLife(seed)
        # WHEN & THEN
        self.assertEqual(game_of_life.tick(), expected_1)
        self.assertEqual(game_of_life.tick(), expected_2)


if __name__ == "__main__":
    unittest.main()
