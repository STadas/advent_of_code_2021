from pathlib import Path
from itertools import product


def roll_det(player_pos, curr_d):
    for _ in range(3):
        player_pos = (player_pos + curr_d - 1) % 10 + 1
        curr_d = curr_d % 100 + 1
    return player_pos, curr_d


def roll_dirac(pos_1, pos_2, s1=0, s2=0, cache={}):
    if (pos_1, pos_2, s1, s2) in cache:
        return cache[pos_1, pos_2, s1, s2]

    w1 = w2 = 0
    for rolls in product((1, 2, 3), repeat=3):
        n_pos = (pos_1 + sum(rolls) - 1) % 10 + 1
        if s1 + n_pos >= 21:
            w1 += 1
        else:
            next_w1, next_w2 = roll_dirac(pos_2, n_pos, s2, s1 + n_pos, cache)
            w1 += next_w2
            w2 += next_w1

    cache[pos_1, pos_2, s1, s2] = w1, w2
    return w1, w2


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()
    pos_1, pos_2 = (int(section.split()[-1]) for section in data)
    
    roll_count = s1 = s2 = 0
    curr_d = 1
    while s1 < 1000 and s2 < 1000:
        pos_1, curr_d = roll_det(pos_1, curr_d)
        s1, s2 = s2, s1 + pos_1
        pos_1, pos_2 = pos_2, pos_1
        roll_count += 3

    p1 = min(s1, s2) * roll_count
    p2 = max(roll_dirac(*(int(section.split()[-1]) for section in data)))

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
