from pathlib import Path


tr = {"#": "1", ".": "0"}


def new_pixel(x, y, algo, img, outside):
    bin_str = ""
    for yy in range(y-1, y+2):
        for xx in range(x-1, x+2):
            if yy not in range(len(img)) or xx not in range(len(img[0])):
                bin_str += tr[outside]
            else:
                bin_str += tr[img[yy][xx]]
    return algo[int(bin_str, 2)]


def apply_algo(algo, img, outside):
    new_img = []
    for y in range(-1, len(img) + 1):
        new_line = ""
        for x in range(-1, len(img[0]) + 1):
            new_line += new_pixel(x, y, algo, img, outside)
        new_img.append(new_line)
    outside = new_pixel(-2, -2, algo, img, outside)
    return new_img, outside


def xd():
    algo, img = open(str(Path(__file__).parent.absolute()) + "/input").read().split("\n\n")
    img = img.splitlines()

    outside = "."
    for i in range(50):
        img, outside = apply_algo(algo, img, outside)
        if i == 1:
            p1 = sum(line.count("#") for line in img)

    p2 = sum(line.count("#") for line in img)
    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
