import random
import sys
from math import inf
from pathlib import Path

from map import is_objetive_or_fire, is_out_of_bounds, is_wall
from util import (
    Action,
    get_initial_expected_value,
    get_new_state_location,
    get_policy,
    go_left,
    go_right,
    matrix,
    print_policy,
)

STANDARD_REWARD_MAP = {
    ".": -0.1,
    ";": -0.3,
    "+": -1.0,
    "x": -10.0,
    "O": 10.0,
    "@": -inf,
}

POSITIVE_REWARD_MAP = {".": 3.0, ";": 1.5, "+": 1.0, "x": 0.0, "O": 10.0, "@": -inf}

LEARNING_RATE = 0.1
DISCOUNT_RATE = 0.9
EPSILON_GREEDY = 0.1

NUM_OF_ARGS = 6

STOCHASTIC_GO_LEFT = 0.1
STOCHASTIC_GO_RIGHT = 0.1

SEED = 123456
random.seed(SEED)

if __name__ == "__main__":
    assert len(sys.argv) == NUM_OF_ARGS

    path_to_file_map = sys.argv[1]
    variant = sys.argv[2]
    x_init = sys.argv[3]
    y_init = sys.argv[4]
    num_steps = sys.argv[5]

    reward_mapping = POSITIVE_REWARD_MAP if variant == "positive" else STANDARD_REWARD_MAP

    char_grid: matrix[str] = []
    reward_grid: matrix[float] = []

    with Path.open(Path(path_to_file_map)) as f:
        W, H = map(int, f.readline().strip("\n").split(" "))
        for line in f:
            mapped_line = [reward_mapping[x] for x in line.strip("\n")]
            reward_grid.append(mapped_line)
            char_grid.append(list(line.strip("\n")))

    # Transpose data
    char_grid = [list(x) for x in zip(*char_grid, strict=True)]
    reward_grid = [list(x) for x in zip(*reward_grid, strict=True)]

    # UP, DOWN, LEFT, RIGHT
    expected_value = get_initial_expected_value(H, W, char_grid)

    initial_state = (int(x_init), int(y_init))

    current_state = initial_state

    for _ in range(int(num_steps)):
        x, y = current_state
        current_expected_value = expected_value[x][y]
        action = (
            random.randrange(0, 4)
            if random.random() < EPSILON_GREEDY
            else current_expected_value.index(max(current_expected_value))
        )

        actual_action = action
        if variant == "stochastic":
            direction = random.random()
            if direction <= STOCHASTIC_GO_LEFT:
                actual_action = go_left(Action(action))
            elif STOCHASTIC_GO_LEFT < direction <= STOCHASTIC_GO_RIGHT + STOCHASTIC_GO_LEFT:
                actual_action = go_right(Action(action))

        new_state_location = get_new_state_location(Action(actual_action), current_state)

        actual_new_state = (
            current_state
            if is_out_of_bounds(H, W, new_state_location) or is_wall(new_state_location, char_grid)
            else new_state_location
        )
        new_x, new_y = actual_new_state

        q = current_expected_value[action]
        r = reward_grid[new_x][new_y]

        if is_objetive_or_fire(actual_new_state, char_grid):
            expected_value[x][y][action] = q + LEARNING_RATE * (r - q)
            current_state = initial_state
            continue

        new_expected_value = expected_value[new_x][new_y]
        best_reward_new_state = max(new_expected_value)

        expected_value[x][y][action] = q + LEARNING_RATE * (
            r + DISCOUNT_RATE * best_reward_new_state - q
        )

        current_state = actual_new_state

    policy = get_policy(H, W, char_grid, expected_value)

    # Transpose data
    policy = [list(x) for x in zip(*policy, strict=True)]

    print_policy(H, W, policy)
