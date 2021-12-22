from pathlib import Path
from functools import reduce


def intersect(b1, b2):
    return tuple((max(b1[x][0], b2[x][0]), min(b1[x][1], b2[x][1])) for x in range(3))


def box_size(box):
    return (abs(box[x][0] - box[x][1]) + 1 if box[x][0] <= box[x][1] else 0 for x in range(3))


def lights(box, next_boxes, bounds=None):
    if bounds:
        box = intersect(box, bounds)
    total_lights = reduce(lambda f, n: f * n, box_size(box))
    intr_li = []
    
    for b in next_boxes:
        intr = intersect(box, b)
        intr_s = box_size(intr)
        if 0 not in intr_s:
            intr_li.append(intr)

    for i, b in enumerate(intr_li):
        total_lights -= lights(b, intr_li[i + 1:], bounds)

    return total_lights


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()
    data = [(line.split()[0] == "on", [tuple(int(n) for n in r.split("=")[1].split("..")) for r in line.split(",")]) for line in data]

    p1 = p2 = 0
    for i, line in enumerate(data):
        if line[0]:
            p1 += lights(line[1], [l[1] for l in data[i + 1:]], ((-50, 50), (-50, 50), (-50, 50)))
            p2 += lights(line[1], [l[1] for l in data[i + 1:]])

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
