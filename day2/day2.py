from pathlib import Path


def xd():
    with open(str(Path(__file__).parent.resolve()) + "/input") as f:
        data = f.read()

    data = data.splitlines()

    pos = 0
    depth = 0
    depth2 = 0
    aim = 0

    for line in data:
        op, units = line.split()
        units = int(units)

        if op == "forward":
            pos += units
            depth2 -= units * aim

        elif op == "up":
            depth -= units
            aim += units

        elif op == "down":
            depth += units
            aim -= units

    p1 = pos * depth
    p2 = pos * depth2

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
