from pathlib import Path


def step(grid):
    moved = False
    x_len = len(grid[0])
    y_len = len(grid)
    n_grid = [line[:] for line in grid]
    for x in range(x_len-1, -1, -1):
        for y in range(y_len-1, -1, -1):
            n_x = (x + 1) % x_len
            if grid[y][x] == ">" and grid[y][n_x] == ".":
                n_grid[y][n_x] = ">"
                n_grid[y][x] = "."
                moved = True

    grid = [line[:] for line in n_grid]
    for x in range(x_len-1, -1, -1):
        for y in range(y_len-1, -1, -1):
            n_y = (y + 1) % y_len
            if grid[y][x] == "v" and grid[n_y][x] == ".":
                n_grid[n_y][x] = "v"
                n_grid[y][x] = "."
                moved = True

    return n_grid, moved


def xd():
    data = [list(s) for s in open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()]

    p1 = 0
    while True:
        data, moved = step(data)
        p1 += 1
        if not moved:
            break

    p2 = 0
    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
