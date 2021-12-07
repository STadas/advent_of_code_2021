from pathlib import Path


def add_or_default(dict_, key, val = 1, default = 1):
    if key in dict_:
        dict_[key] += val
    else:
        dict_[key] = default


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()

    grid = {}
    grid2 = {}
    for line in data:
        x1, y1, x2, y2 = (int(x) for x in line.replace(" -> ", ",").split(","))

        if y1 == y2:
            mod = 1 if x1 < x2 else -1
            for i in range(abs(x2 - x1) + 1):
                add_or_default(grid, (x1 + mod * i, y1))
                add_or_default(grid2, (x1 + mod * i, y1))

        elif x1 == x2:
            mod = 1 if y1 < y2 else -1
            for i in range(abs(y2 - y1) + 1):
                add_or_default(grid, (x1, y1 + mod * i))
                add_or_default(grid2, (x1, y1 + mod * i))

        else:
            x_mod = 1 if x1 < x2 else -1
            y_mod = 1 if y1 < y2 else -1
            for i in range(abs(x2 - x1) + 1):
                add_or_default(grid2, (x1 + i * x_mod, y1 + i * y_mod))

    p1 = sum(x > 1 for x in grid.values())
    p2 = sum(x > 1 for x in grid2.values())

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
