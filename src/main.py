import sys
from math import inf
from pathlib import Path

map_grid: list[list[float]] = []

standard_reward_map = {
    ".": -0.1,
    ";": -0.3,
    "+": -1.0,
    "x": -10.0,
    "O": 10.0,
    "@": -inf,
}

positive_reward_map = {".": 3.0, ";": 1.5, "+": 1.0, "x": 0.0, "O": 10.0, "@": -inf}

NUM_OF_ARGS = 7

if __name__ == "__main__":
    assert len(sys.argv) == NUM_OF_ARGS

    variant = sys.argv[3]

    reward_mapping = positive_reward_map if variant == "positive" else standard_reward_map

    with Path.open(Path(sys.argv[2])) as f:
        first_line = f.readline()
        w, h = map(int, first_line.strip("\n").split(" "))
        for line in f:
            mapped_line = [reward_mapping[x] for x in line.strip("\n")]
            map_grid.append(mapped_line)
