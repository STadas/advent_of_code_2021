from pathlib import Path
from functools import reduce


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()

    matching = {"(": ")", "[": "]", "{": "}", "<": ">"}
    table = {")": 3, "]": 57, "}": 1197, ">": 25137}
    table2 = {")": 1, "]": 2, "}": 3, ">": 4}

    p1 = 0
    scores = []
    for line in data:
        stack = []
        for c in line:
            if c in matching:
                stack.append(matching[c])
            else:
                if stack.pop() != c:
                    p1 += table[c]
                    break
        else:
            scores.append(reduce(lambda x, y: x * 5 + table2[y], (0, *reversed(stack))))
    p2 = sorted(scores)[len(scores) // 2]

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
