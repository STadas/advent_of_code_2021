from pathlib import Path


def nemo(counts, days):
    counts = counts.copy()
    for day in range(days):
        temp = counts[0]
        for i in range(1, len(counts)):
            counts[i-1] = counts[i]
        counts[6] += temp
        counts[8] = temp
    return counts


def xd():
    data = [int(x) for x in open(str(Path(__file__).parent.resolve()) + "/input").read().split(",")]

    counts = [0] * 9
    for fish in data:
        counts[fish] += 1

    p1 = sum(nemo(counts, 80))
    print(f"{p1=}")

    p2 = sum(nemo(counts, 256))
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
