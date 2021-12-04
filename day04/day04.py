from pathlib import Path


def xd():
    data = open(str(Path(__file__).parent.resolve()) + "/input").read().split("\n\n")

    draw = [int(x) for x in data[0].split(",")]
    boards = []
    for section in data[1:]:
        board = []
        lines = section.splitlines()
        for y in range(len(lines)):
            board.append([])
            for num in lines[y].split():
                board[y].append(int(num))
        boards.append(board)

    max_y = len(boards[0])
    max_x = len(boards[0][0])

    won_at = [len(draw)] * len(boards)
    win_sum = [0] * len(boards)

    for b, board in enumerate(boards):
        s_board = set(n for l in board for n in l)
        for x in range(max_x):
            count = 0
            furthest = 0
            for y in range(max_y):
                for i, n in enumerate(draw):
                    if n == board[y][x]:
                        count += 1
                        if furthest < i:
                            furthest = i
                        break
            if count == max_y and furthest < won_at[b]:
                won_at[b] = furthest
                win_sum[b] = sum(s_board.difference(draw[:furthest + 1]))

        for y in range(max_y):
            count = 0
            furthest = 0
            for x in range(max_x):
                for i, n in enumerate(draw):
                    if n == board[y][x]:
                        count += 1
                        if furthest < i:
                            furthest = i
                        break
            if count == max_x and furthest < won_at[b]:
                won_at[b] = furthest
                win_sum[b] = sum(s_board.difference(draw[:furthest + 1]))

    p1 = draw[min(won_at)] * win_sum[won_at.index(min(won_at))]
    p2 = draw[max(won_at)] * win_sum[won_at.index(max(won_at))]

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
