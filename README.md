# game_of_life

## What?
Kata dojo experiment for a Conway Game of Life - https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

Code Kata is a term coined by Dave Thomas, co-author of the book The Pragmatic Programmer, in a bow to the Japanese concept of kata in the martial arts. A code kata is an exercise in programming which helps a programmer hone their skills through practice and repetition. https://en.wikipedia.org/wiki/Kata_(programming)


## Rules
The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead, or "populated" or "unpopulated" (the difference may seem minor, except when viewing it as an early model of human/urban behavior simulation or how one views a blank space on a grid). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

* Any live cell with fewer than two live neighbours dies, as if caused by under-population.
* Any live cell with two or three live neighbours lives on to the next generation.
* Any live cell with more than three live neighbours dies, as if by over-population.
* Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed—births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick (in other words, each generation is a pure function of the preceding one). The rules continue to be applied repeatedly to create further generations.

## Requirements
Python 3.5

# Implementation rules
* TDD 
* kata rules - 
## Implementation notes
* TDD
* empty
* generator (with yield)
* objectize
* tick 
* save state
* tick_with_one_death
* tick with stable survivor
* create get_alive_neibours(cell)
* create get_neighbours(cell)
* implement set of alive_cells
* births empty
* births candidates = (dead_neighbours(cell)   set.union(*dead_with_one_live_neighbour)
* birth correct  (foreach candidate if len(live_neighbours==3 ))
* refactor
* blinker (tick = set.union(survivors and births)
