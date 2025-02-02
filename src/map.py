from alias import coords, matrix


def is_out_of_bounds(h: int, w: int, state: coords) -> bool:
    x, y = state
    return x < 0 or y < 0 or x >= w or y >= h


def is_wall(state: coords, char_grid: matrix[str]) -> bool:
    x, y = state
    return char_grid[x][y] == "@"


def is_objetive_or_fire(state: coords, char_grid: matrix[str]) -> bool:
    x, y = state
    return char_grid[x][y] in ("O", "x")
