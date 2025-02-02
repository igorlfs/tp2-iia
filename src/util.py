from enum import Enum

from alias import coords, matrix

DEFAULT_EXPECTED_VALUE = 0.1

# A bit wonky because we have to consider the transposition
POLICY_TO_CHAR = ["<", ">", "^", "v"]


class Action(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


def get_initial_expected_value(h: int, w: int, char_grid: matrix[str]) -> matrix[list[float]]:
    return [
        [
            [DEFAULT_EXPECTED_VALUE] * 4 if char_grid[i][j] not in ("@", "O", "x") else []
            for j in range(h)
        ]
        for i in range(w)
    ]


def get_policy(
    h: int, w: int, char_grid: matrix[str], expected_value: matrix[list[float]]
) -> matrix[str]:
    policy: matrix[str] = []

    for i in range(w):
        policy.append([])
        for j in range(h):
            result = expected_value[i][j]
            char = (not result and char_grid[i][j]) or POLICY_TO_CHAR[result.index(max(result))]
            policy[i].append(char)

    return policy


def get_new_state_location(action: Action, current_state: coords) -> coords:
    x, y = current_state
    match action:
        case Action.UP:
            return (x - 1, y)
        case Action.DOWN:
            return (x + 1, y)
        case Action.LEFT:
            return (x, y - 1)
        case Action.RIGHT:
            return (x, y + 1)


def print_policy(h: int, w: int, policy: matrix[str]) -> None:
    for i in range(h):
        for j in range(w):
            print(policy[i][j], end="")
        print()
