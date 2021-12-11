from pathlib import Path


def check_n_flash(flashes, data, y, x):
    if data[y][x] > 9:
        data[y][x] = 0
        flashes.add((y, x))
        for yn in range(y - 1, y + 2):
            for xn in range(x - 1, x + 2):
                if 0 <= yn < len(data) and 0 <= xn < len(data[0]) and data[yn][xn] != 0:
                    data[yn][xn] += 1
                    check_n_flash(flashes, data, yn, xn)


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()
    data = [[int(n) for n in line] for line in data]

    p1 = 0
    p2 = 0
    i = 0
    while p2 == 0:
        flashes = set()
        for y, line in enumerate(data):
            for x, num in enumerate(line):
                data[y][x] = data[y][x] + 1
        for y, line in enumerate(data):
            for x, num in enumerate(line):
                check_n_flash(flashes, data, y, x)
        if p2 == 0 and len(flashes) == len(data) * len(line):
            p2 = i + 1
        if i < 100:
            p1 += len(flashes)
        i += 1

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
