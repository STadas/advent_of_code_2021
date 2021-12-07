from pathlib import Path


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().split("\n"*2)

    draw = tuple(int(x) for x in data[0].split(","))
    boards = [[[int(n) for n in l.split()] for l in s.splitlines()] for s in data[1:]]

    max_y = len(boards[0])
    max_x = len(boards[0][0])
    won_at = [len(draw)] * len(boards)
    win_sum = [0] * len(boards)

    for b in range(len(boards)):
        s_board = set(n for l in boards[b] for n in l)
        count_y = [0] * max_y
        furthest_y = [0] * max_y

        for y in range(max_y):
            count_x = 0
            furthest_x = 0

            for x in range(max_x):
                i = draw.index(boards[b][y][x]) if boards[b][y][x] in draw else None
                if i is not None:
                    count_x += 1
                    furthest_x = i if furthest_x < i else furthest_x
                    count_y[x] += 1
                    furthest_y[x] = i if furthest_y[x] < i else furthest_y[x]

                if count_y[x] == max_y and furthest_y[x] < won_at[b]:
                    won_at[b] = furthest_y[x]
                    win_sum[b] = sum(s_board.difference(draw[:furthest_y[x] + 1]))

            if count_x == max_x and furthest_x < won_at[b]:
                won_at[b] = furthest_x
                win_sum[b] = sum(s_board.difference(draw[:furthest_x + 1]))

    p1 = draw[min(won_at)] * win_sum[won_at.index(min(won_at))]
    p2 = draw[max(won_at)] * win_sum[won_at.index(max(won_at))]
    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
