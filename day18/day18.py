from pathlib import Path


def explode(line):
    depth = 0
    for i, c in enumerate(line):
        depth += 1 if c == "[" else -1 if c == "]" else 0
        if depth == 5:
            for j in range(i - 1, -1, -1):
                if isinstance(line[j], int):
                    line[j] += line[i + 1]
                    break
            for j in range(i + 3, len(line)):
                if isinstance(line[j], int):
                    line[j] += line[i + 2]
                    break
            line[i:i + 4] = [0]
            return True


def split(line):
    for i, c in enumerate(line):
        if isinstance(c, int) and c >= 10:
            line[i:i + 1] = ["[", c // 2, -(-c // 2),"]"]
            return True


def magnitude(line):
    while len(line) > 1:
        for i, c in enumerate(line):
            if isinstance(c, int) and isinstance(line[i + 1], int):
                line[i - 1:i + 3] = [c * 3 + line[i + 1] * 2]
                break
    return line[0]


def reduce(line):
    while True:
        if not explode(line) and not split(line):
            return line


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()
    for i, line in enumerate(data):
        data[i] = [int(c) if c.isnumeric() else c for c in filter(lambda x: x != ",", line)]
    added = data[0]
    for line in data[1:]:
        added = reduce(["[", *added, *line,"]"])
    p1 = magnitude(added)
    p2 = max(magnitude(reduce(["[", *first, *second, "]"])) for first in data for second in data)
    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
