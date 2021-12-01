from pathlib import Path


def xd():
    # with open(str(Path(__file__).parent.resolve()) + "/input") as f:
    #     data = f.read().splitlines()
    # data = list(map(int, data))

    # p1 = 0
    # for i in range(len(data)):
    #     if data[i] > data[i-1]:
    #         p1 += 1

    # p2 = 0
    # for i in range(3, len(data)):
    #     if data[i] > data[i-3]:
    #         p2 += 1

    # print(f"{p1=}")
    # print(f"{p2=}")

    print("p1="+str(sum(map(lambda i: data[i] > data[i-1], range(1, len(data := list(map(int, open(str(Path(__file__).parent.resolve()) + "/input")))))))), "\np2=" + str(sum(map(lambda i: data[i] > data[i-3], range(3, len(data))))))


if __name__ == "__main__":
    xd()
