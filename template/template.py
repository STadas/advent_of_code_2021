from pathlib import Path


def xd():
    with open(str(Path(__file__).parent.resolve()) + "/input") as f:
        data = f.read()

    # data = data.splitlines()
    # data = tuple(map(int, data))

    p1 = 0
    for line in data:
        print(line)

    p2 = 0
    for i in data:
        pass

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
