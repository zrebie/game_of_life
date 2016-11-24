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

if __name__ == "__main__":
    unittest.main()
