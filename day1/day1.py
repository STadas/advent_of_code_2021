from pathlib import Path


def xd():
    with open(str(Path(__file__).parent.resolve()) + "/input") as f:
        data = f.read().splitlines()

    data = tuple(map(int, data))

    p1 = 0
    prev = data[0]
    for line in data:
        curr = line
        if curr > prev:
            p1 += 1
        prev = curr

    p2 = 0
    prev = sum(data[:3])
    for i in range(1, len(data)-2):
        curr = sum(data[i:i+3])
        if curr > prev:
            p2 += 1
        prev = curr

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
