from pathlib import Path


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().split("\n\n")
    dots, folds = (sec.splitlines() for sec in data)
    dots = set(tuple(int(x) for x in d.split(",")) for d in dots)
    folds = [[f.split("=")[0][-1], int(f.split("=")[1])] for f in folds]

    p1 = None
    for f in folds:
        folded_dots = set()
        if f[0] == "x":
            max_x = f[1]
            for d in dots:
                if d[0] > f[1]:
                    folded_dots.add((f[1] - (d[0] - f[1]), d[1]))
                else:
                    folded_dots.add(tuple(d))
        elif f[0] == "y":
            max_y = f[1]
            for d in dots:
                if d[1] > f[1]:
                    folded_dots.add((d[0], f[1] - (d[1] - f[1])))
                else:
                    folded_dots.add(tuple(d))
        dots = folded_dots

        if p1 is None:
            p1 = len(dots)

    p2 = []
    for y in range(max_y):
        p2.append("".join("#" if (x, y) in dots else " " for x in range(max_x)))

    print(f"{p1=}")
    print("p2=")
    for line in p2:
        print(line)


if __name__ == "__main__":
    xd()
