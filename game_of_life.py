import unittest

class GameOfLife(object):
    def __init__(self, seed):
        self.alive_cells = seed

def generator(seed):
    return set([])


def test_game_of_life_object_initialization():
    # GIVEN
    seed = set([])
    # WHEN
    game_of_life = GameOfLife(seed)
    # THEN
    assert game_of_life.alive_cells == seed

def test_empty_seed_generation():
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
    next_generation = generator(seed)
    # THEN
    assert next_generation == expected
    
