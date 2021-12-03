from pathlib import Path
from functools import reduce


def fltr(data, compare):
    i = 0
    filtered = list(data)
    while len(filtered) > 1:
        bit = int(compare(sum([b[i] if b[i] else -1 for b in filtered]), 0))
        checked = list(filter(lambda x: x[i] == bit, filtered))
        if len(checked) > 0:
            filtered = checked
        if len(filtered) == 1:
            break
        i += 1
    return int("".join(str(x) for x in filtered[0]), 2)


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()

    data = [[int(x) for x in line] for line in data]
    one_c = reduce(lambda x, y: [xb + (1 if yb else -1) for xb, yb in zip(x, y)], data)
    cmn = int("".join(str(int(x >= 0)) for x in one_c), 2)

    p1 = cmn * (~cmn & int("1" * len(data[0]), 2))
    p2 = fltr(data, lambda x, y: x >= y) * fltr(data, lambda x, y: x < y)

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
