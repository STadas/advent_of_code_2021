"""pain"""
from pathlib import Path
from itertools import product, combinations
from collections import Counter


class Vector:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = int(x), int(y), int(z)

    def rotated(self, rot):
        n_vec = Vector(self.x, self.y, self.z)
        for _ in range(rot.x):
            n_vec.y, n_vec.z = n_vec.z, -n_vec.y

        for _ in range(rot.y):
            n_vec.z, n_vec.x = n_vec.x, -n_vec.z

        for _ in range(rot.z):
            n_vec.x, n_vec.y = n_vec.y, -n_vec.x

        return n_vec

    def as_tuple(self):
        return self.x, self.y, self.z

    def man_dist_to(self, other):
        return sum(abs(n) for n in (self - other).as_tuple())

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __sub__(self, other):
        return Vector(self.x - other.x,
                      self.y - other.y,
                      self.z - other.z)


rotations = {
    Vector(0,0,0),
	Vector(1,0,0),
	Vector(2,0,0),
	Vector(3,0,0),
	Vector(0,1,0),
	Vector(1,1,0),
	Vector(2,1,0),
	Vector(3,1,0),
	Vector(0,2,0),
	Vector(1,2,0),
	Vector(2,2,0),
	Vector(3,2,0),
	Vector(0,3,0),
	Vector(1,3,0),
	Vector(2,3,0),
	Vector(3,3,0),
	Vector(0,0,1),
	Vector(1,0,1),
	Vector(2,0,1),
	Vector(3,0,1),
	Vector(0,0,3),
	Vector(1,0,3),
	Vector(2,0,3),
	Vector(3,0,3),
}


class Scanner:
    def __init__(self, beacons):
        self.beacons = beacons

    def rotated(self, rot):
        return Scanner(set(b.rotated(rot) for b in self.beacons))

    def check(self, abs_beacons):
        for rot in rotations:
            rotated_s = self.rotated(rot)
            dist, count = Counter(rotated_s.distances(abs_beacons)).most_common(1)[0]
            if count >= 12:
                return dist, set(b - dist for b in rotated_s.beacons)

    def distances(self, abs_beacons):
        return (b2 - b1 for b1, b2 in product(abs_beacons, self.beacons))


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().split("\n\n")
    unsolved = set()
    scanner_positions = set()
    abs_beacons = None

    for section in data:
        section = section.splitlines()
        s = Scanner(set(Vector(*line.split(",")) for line in section[1:]))
        if abs_beacons is None:
            abs_beacons = s.beacons
        else:
            unsolved.add(s)

    while unsolved:
        print(len(unsolved))
        for s in unsolved:
            res = s.check(abs_beacons)
            if res is not None:
                pos, beacons = res
                scanner_positions.add(pos)
                abs_beacons.update(beacons)
                unsolved.remove(s)
                break

    p1 = len(abs_beacons)
    p2 = max(p1.man_dist_to(p2) for p1, p2 in combinations(scanner_positions, 2))
    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
