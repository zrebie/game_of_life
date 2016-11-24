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

    def test_tick_with_one_cell_dies(self):
        """
        .*.
        =>
        ...
        """
        # GIVEN
        seed = set([(0, 0)])
        expected_1 = set()
        expected_2 = set()
        game_of_life = GameOfLife(seed)
        # WHEN & THEN
        self.assertEqual(game_of_life.tick(), expected_1)
        self.assertEqual(game_of_life.tick(), expected_2)

    def test_tick_block_should_survive(self):
        """
        **
        **
        =>
        **
        **
        """
        # GIVEN
        seed = set([(0, 0), (0, 1), (1, 0), (1, 1)])
        expected = seed
        game_of_life = GameOfLife(seed)
        # WHEN & THEN
        self.assertEqual(game_of_life.tick(), expected)

    def test_should_return_correct_neighbours(self):
        # GIVEN
        cell = (0, 0)
        expected_len = 8
        expected_neighbours = set([(-1, -1), (0, -1), (1, -1),
                                   (-1, 0), (1, 0),
                                   (-1, 1), (0, 1), (1, 1)])
        # WHEN
        neighbours = GameOfLife.get_neighbours(cell)
        # THEN
        self.assertEqual(expected_len, len(neighbours))
        self.assertEqual(expected_neighbours, neighbours)

    def test_should_return_correct_neighbours_any_cell(self):
        # GIVEN
        cell = (14, 3)
        expected_len = 8
        expected_neighbours = set([(13, 2), (14, 2), (15, 2),
                                   (13, 3), (15, 3),
                                   (13, 4), (14, 4), (15, 4)])
        # WHEN
        neighbours = GameOfLife.get_neighbours(cell)
        # THEN
        self.assertEqual(expected_len, len(neighbours))
        self.assertEqual(expected_neighbours, neighbours)

    def test_should_return_correct_set_of_alive_neighbours_of_cell(self):
        # GIVEN
        seed = set([(-1, -1), (-1, 0)])
        game_of_life = GameOfLife(seed)
        cell = (0, 0)
        expected_neighbours = set([(-1, -1), (-1, 0)])
        # WHEN
        alive_neighbours = game_of_life.get_alive_neighbours(cell)
        # THEN
        self.assertEqual(expected_neighbours, alive_neighbours)

    def test_should_return_correct_set_of_dead_neighbours_of_cell(self):
        # GIVEN
        seed = set([(-1, -1), (-1, 0)])
        game_of_life = GameOfLife(seed)
        cell = (0, 0)
        expected_dead_neighbours = set([(0, -1), (1, -1), (1, 0), (-1, 1), (0, 1), (1, 1)])
        # WHEN
        dead_neighbours = game_of_life.get_dead_neighbours(cell)
        # THEN
        self.assertEqual(expected_dead_neighbours, dead_neighbours)

    def test_should_return_correct_set_of_birth_candidates(self):
        """
        ....
        .**.
        ....
        """
        # GIVEN
        seed = set([(0, 0), (0, 1)])
        game_of_life = GameOfLife(seed)
        expected_birth_candidates = set([(-1, 1), (-1, 0), (-1, -1), (1, 0), (0, -1), (1, 1), (1, -1), (1, 2), (0, 2), (-1, 2)])
        # WHEN
        birth_candidates = game_of_life.get_birth_candidates()
        # THEN
        self.assertEqual(expected_birth_candidates, birth_candidates)


    def test_should_arise_from_dead_one_cell(self):
        """
        .*
        **

        =>

        **
        **

        """
        # GIVEN
        seed = set([(0, 0), (0, 1), (1, 1)])
        game_of_life = GameOfLife(seed)
        expected_births = set([(1, 0)])
        # WHEN
        births = game_of_life.get_births()
        # THEN
        self.assertEqual(expected_births, births)

    def test_should_tick_births_and_deaths_for_blinker(self):
        """
        ...
        ***
        ...
        =>
        .*.
        .*.
        .*.
        =>
        ...
        ***
        ...
        """
        # GIVEN
        seed = set([(-1, 0), (0, 0), (1, 0)])
        game_of_life = GameOfLife(seed)
        expected_generation_1 = set([(0, 1), (0, 0), (0, -1)])
        expected_generation_2 = set([(-1, 0), (0, 0), (1, 0)])
        # WHEN & THEN
        self.assertEqual(expected_generation_1, game_of_life.tick())
        self.assertEqual(expected_generation_2, game_of_life.tick())

if __name__ == "__main__":
    unittest.main()
