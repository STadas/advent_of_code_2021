from pathlib import Path


def xd():
    data = open(str(Path(__file__).parent.resolve()) + "/input").read()#.splitlines()

    p1 = 0
    for line in data:
        print(line)

    p2 = 0
    for line in data:
        pass

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
