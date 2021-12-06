from pathlib import Path


def xd():
    data = [int(x) for x in open(str(Path(__file__).parent.resolve()) + "/input").read().split(",")]
    counts = [data.count(i) for i in range(9)]

    for day in range(256):
        if day == 80:
            p1 = sum(counts)

        temp = counts[0]
        for i in range(1, 9):
            counts[i-1] = counts[i]
        counts[6] += temp
        counts[8] = temp

    p2 = sum(counts)

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
