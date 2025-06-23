# Game of Life 64
This is the [game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) implemented using only 64 bits of storage for the [bitwise challenge](https://github.com/zesterer/the-bitwise-challenge).

# Usage
```
# start from a random initial state
python gol.py

# start from a given state
python gol.py e0a0e00
```
# Interesting States
* `70402` simple glider
* `7700` lines cycle
* `3030` a box (ok maybe not that interesting)
* `e0a0e00` complex cycle

# Implementation
The state is treated as an 8x8 grid of 1-bit cells (alive or dead).

The number of neighbors is counted using a pre-computed bitmask for each position and python's built-in `int.bit_count()`.
The rest is pretty straightforward. Not a lot of interesting tricks we can do here.
