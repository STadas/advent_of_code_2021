from pathlib import Path
from collections import defaultdict


def xd():
    data = open(str(Path(__file__).parent.resolve()) + "/input").read().splitlines()

    grid = defaultdict(lambda: 0)
    grid2 = defaultdict(lambda: 0)
    for line in data:
        x1, y1, x2, y2 = [int(x) for x in line.replace(" -> ", ",").split(",")]
        if y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2 + 1):
                grid[x, y1] += 1
                grid2[x, y1] += 1

        elif x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2 + 1):
                grid[x1, y] += 1
                grid2[x1, y] += 1

        else:
            x = x1
            y = y1
            do_while = True
            while do_while:
                do_while = x != x2 and y != y2
                grid2[x, y] += 1
                x += 1 if x1 < x2 else -1
                y += 1 if y1 < y2 else -1

    p1 = sum(x > 1 for x in grid.values())
    p2 = sum(x > 1 for x in grid2.values())

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
