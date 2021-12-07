from pathlib import Path
from statistics import median, mean
from math import floor, ceil


def xd():
    data = sorted([int(x) for x in open(str(Path(__file__).parent.resolve()) + "/input").read().split(",")])

    sf, sc = 0, 0
    mf, mc = floor(median(data)), ceil(median(data))
    for n in data:
        sf += abs(mf - n)
        sc += abs(mc - n)
    p1 = min(sf, sc)

    sf, sc = 0, 0
    mf, mc = floor(mean(data)), ceil(mean(data))
    for n in data:
        sf += sum(range(abs(mf - n) + 1))
        sc += sum(range(abs(mc - n) + 1))
    p2 = min(sf, sc)

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
