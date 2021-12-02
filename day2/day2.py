from pathlib import Path
from functools import (partial,
                       reduce)


def xd():
    # with open(str(Path(__file__).parent.resolve()) + "/input") as f:
    #     data = f.read()

    # data = data.splitlines()

    # pos = 0
    # depth = 0
    # depth2 = 0
    # aim = 0

    # for line in data:
    #     op, units = line.split()
    #     units = int(units)

    #     if op[0] == "f":
    #         pos += units
    #         depth2 -= units * aim

    #     elif op[0] == "u":
    #         depth -= units
    #         aim += units

    #     elif op[0] == "d":
    #         depth += units
    #         aim -= units

    # p1 = pos * depth
    # p2 = pos * depth2

    # print(f"{p1=}")
    # print(f"{p2=}")


    # partial(lambda pos, aim, p1d, p2d: print(f"p1={pos * p1d}\np2={pos * p2d}"))(
    #     *[(
    #         pos := x[1] if x[0][0] == "f" else 0,
    #         aim := x[1] if x[0][0] == "d" else -x[1] if x[0][0] == "u" else 0,
    #         depth := x[1] if x[0][0] == "d" else -x[1] if x[0][0] == "u" else 0,
    #         depth2 := 0
    #     ) if i== 0 else (
    #         pos := pos + (x[1] if x[0][0] == "f" else 0),
    #         aim := aim + (x[1] if x[0][0] == "d" else -x[1] if x[0][0] == "u" else 0),
    #         depth := depth + (x[1] if x[0][0] == "d" else -x[1] if x[0][0] == "u" else 0),
    #         depth2 := depth2 + (aim * x[1] if x[0][0] == "f" else 0),
    #     ) for i, x in enumerate(list(map(lambda x: (x[0], int(x.split()[1])),
    #                                      open(str(Path(__file__).parent.resolve()) + "/input"))))
    #     ][-1]
    # )

    partial(lambda pos, aim, p1d, p2d: print(f"p1={pos * p1d}\np2={pos * p2d}"))(*[(pos := x[1] if x[0][0] == "f" else 0, aim := x[1] if x[0][0] == "d" else -x[1] if x[0][0] == "u" else 0, depth := x[1] if x[0][0] == "d" else -x[1] if x[0][0] == "u" else 0, depth2 := 0) if i== 0 else (pos := pos + (x[1] if x[0][0] == "f" else 0), aim := aim + (x[1] if x[0][0] == "d" else -x[1] if x[0][0] == "u" else 0), depth := depth + (x[1] if x[0][0] == "d" else -x[1] if x[0][0] == "u" else 0), depth2 := depth2 + (aim * x[1] if x[0][0] == "f" else 0)) for i, x in enumerate(list(map(lambda x: (x[0], int(x.split()[1])), open(str(Path(__file__).parent.resolve()) + "/input"))))][-1])


if __name__ == "__main__":
    xd()
