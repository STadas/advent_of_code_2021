from pathlib import Path


def xd():
    # with open(str(Path(__file__).parent.resolve()) + "/input") as f:
    #     data = f.read().splitlines()
    # data = list(map(int, data))

    # p1 = 0
    # prev = data[0]
    # for line in data:
    #     curr = line
    #     if curr > prev:
    #         p1 += 1
    #     prev = curr

    # p2 = 0
    # prev = sum(data[:3])
    # for i in range(1, len(data)-2):
    #     curr = sum(data[i:i+3])
    #     if curr > prev:
    #         p2 += 1
    #     prev = curr

    # print(f"{p1=}")
    # print(f"{p2=}")

    print("p1="+str(sum(map(lambda i: data[i] > data[i-1], range(1, len(data := list(map(int, open(str(Path(__file__).parent.resolve()) + "/input")))))))), "\np2=" + str(sum(map(lambda i: sum(data[i:i+3]) > sum(data[i-1:i+2]), range(1, len(data))))))


if __name__ == "__main__":
    xd()
