from pathlib import Path


def xd():
    data = sorted([int(x) for x in open(str(Path(__file__).parent.absolute()) + "/input").read().split(",")])

    m = data[len(data) // 2]
    p1 = sum(abs(m - n) for n in data)

    m = sum(data) // len(data)
    p2 = sum(((d := abs(m - n)) * (d + 1)) // 2 for n in data)

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
