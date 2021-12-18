from pathlib import Path


def fire(xr, yr, xv, yv):
    xp, yp = 0, 0
    highest_y = 0
    while xp <= xr[1] + 1 and yp >= yr[0] -1:
        xp += xv
        yp += yv
        highest_y = max(yp, highest_y)

        if xp in range(xr[0], xr[1] + 1) and yp in range(yr[0], yr[1] + 1):
            return highest_y

        if xv > 0:
            xv -= 1
        elif xv < 0:
            xv += 1
        yv -= 1

    return None


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().strip()
    xr, yr = [[int(x) for x in s[s.find("=") + 1:].split("..")] for s in data.split(", ")]

    p1 = 0
    p2 = 0
    # we do a little bruteforcing
    # 300 for x and -150,150 for y seems like the sweet spot
    for xv in range(300):
        for yv in range(-150, 150):
            yp = fire(xr, yr, xv, yv)
            if yp is not None:
                p1 = max(yp, p1)
                p2 += 1

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
