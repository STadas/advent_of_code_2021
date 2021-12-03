from pathlib import Path
from functools import reduce


def xd():
    with open(str(Path(__file__).parent.resolve()) + "/input") as f:
        data = f.read()

    data = data.splitlines()
    threshold = len(data) / 2

    data = [[int(x) for x in line] for line in data]
    one_counts = reduce(lambda x, y: [xb + yb for xb, yb in zip(x, y)], data)
    gamma = sum([int(x > threshold) * (2 ** i) for i, x in enumerate(reversed(one_counts))])
    epsilon = sum([int(x < threshold) * (2 ** i) for i, x in enumerate(reversed(one_counts))])
    p1 = gamma * epsilon

    i = 0
    filtered = list(data)
    while len(filtered) > 1:
        needed_bit = int(sum([b[i] for b in filtered]) >= len(filtered) / 2)
        checked = list(filter(lambda x: x[i] == needed_bit, filtered))
        if len(checked) > 0:
            filtered = checked
        if len(filtered) == 1:
            break
        i += 1

    print(filtered[0])
    oxygen_gen = sum([int(x * (2**i)) for i, x in enumerate(reversed(filtered[0]))])
    print(oxygen_gen)

    i = 0
    filtered = list(data)
    while len(filtered) > 1:
        needed_bit = int(sum([b[i] for b in filtered]) < len(filtered) / 2)
        checked = list(filter(lambda x: x[i] == needed_bit, filtered))
        if len(checked) > 0:
            filtered = checked
        if len(filtered) == 1:
            break
        i += 1

    co_scrubber = sum([int(x * (2**i)) for i, x in enumerate(reversed(filtered[0]))])

    p2 = co_scrubber * oxygen_gen

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
