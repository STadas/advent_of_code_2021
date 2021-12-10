from pathlib import Path


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()
    table = {")": 3, "]": 57, "}": 1197, ">": 25137}
    table2 = {")": 1, "]": 2, "}": 3, ">": 4}

    p1 = 0
    scores = []
    for line in data:
        stack = []
        corrupted = False
        for c in line:
            if c == "(":
                stack.append(")")
            elif c == "[":
                stack.append("]")
            elif c == "{":
                stack.append("}")
            elif c == "<":
                stack.append(">")
            else:
                closing = stack.pop()
                if closing != c:
                    corrupted = True
                    p1 += table[c]
                    break
        if not corrupted:
            score = 0
            while len(stack) > 0:
                c = stack.pop()
                score *= 5
                score += table2[c]
            scores.append(score)
    p2 = sorted(scores)[len(scores) // 2]

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
