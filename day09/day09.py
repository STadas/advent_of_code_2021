from pathlib import Path
from functools import reduce


def basin(data, x, y, basin_coords):
    basin_coords.add((x, y))
    if y > 0 and data[y-1][x] != 9 and data[y-1][x] > data[y][x]:
        basin_coords.add((x, y-1))
        basin(data, x, y-1, basin_coords)
    if y < len(data) - 1 and data[y+1][x] != 9 and data[y+1][x] > data[y][x]:
        basin_coords.add((x, y+1))
        basin(data, x, y+1, basin_coords)
    if x > 0 and data[y][x-1] != 9 and data[y][x-1] > data[y][x]:
        basin_coords.add((x-1, y))
        basin(data, x-1, y, basin_coords)
    if x < len(data[y]) - 1 and data[y][x+1] != 9 and data[y][x+1] > data[y][x]:
        basin_coords.add((x+1, y))
        basin(data, x+1, y, basin_coords)


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()
    data = [[int(c) for c in line] for line in data]

    p1 = 0
    basin_sizes = []
    for y, line in enumerate(data):
        for x, depth in enumerate(line):
            checkem = []
            if y > 0:
                checkem.append(data[y-1][x])
            if y < len(data) - 1:
                checkem.append(data[y+1][x])
            if x > 0:
                checkem.append(data[y][x-1])
            if x < len(line) - 1:
                checkem.append(data[y][x+1])
            if all(depth < d for d in checkem):
                p1 += depth + 1
                basin(data, x, y, basin_coords := set())
                basin_sizes.append(len(basin_coords))
    p2 = reduce(lambda x, y: x * y, sorted(basin_sizes)[-3:])

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
