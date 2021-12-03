from pathlib import Path
from functools import reduce


def fltr(data, compare):
    i = 0
    filtered = list(data)
    while len(filtered) > 1:
        needed_bit = int(compare(sum([b[i] for b in filtered]), len(filtered) / 2))
        checked = list(filter(lambda x: x[i] == needed_bit, filtered))
        if len(checked) > 0:
            filtered = checked
        if len(filtered) == 1:
            break
        i += 1
    return int("".join(str(x) for x in filtered[0]), 2)


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()

    half_point = len(data) / 2

    data = [[int(x) for x in line] for line in data]
    one_c = reduce(lambda x, y: [xb + yb for xb, yb in zip(x, y)], data)
    cmn = int("".join(str(int(x >= half_point)) for x in one_c), 2)

    p1 = cmn * (~cmn & int("1" * len(data[0]), 2))
    p2 = fltr(data, lambda x, y: x >= y) * fltr(data, lambda x, y: x < y)

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
