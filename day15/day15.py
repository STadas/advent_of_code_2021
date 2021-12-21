from pathlib import Path
import heapq as hq


def deezstra(edges, start, goal):
    q = [(0, start)]
    costs = {start: 0}
    while goal not in costs:
        p_cost, p_from = hq.heappop(q)
        for n, cost in edges[p_from].items():
            if n not in costs or cost + costs[p_from] < p_cost:
                costs[n] = cost + costs[p_from]
                hq.heappush(q, (cost + costs[p_from], n))
    return costs[goal]


def gen_grid(data, x_len, y_len):
    nodes = tuple((x, y) for y in range(y_len) for x in range(x_len))
    edges = {n: {} for n in nodes}
    for x, y in nodes:
        if x > 0:
            edges[(x, y)][(x-1, y)] = data[y][x-1]
        if y > 0:
            edges[(x, y)][(x, y-1)] = data[y-1][x]
        if x < x_len - 1:
            edges[(x, y)][(x+1, y)] = data[y][x+1]
        if y < y_len - 1:
            edges[(x, y)][(x, y+1)] = data[y+1][x]
    return edges


def xd():
    data = [[int(x) for x in line] for line in open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()]
    y_len, x_len = len(data), len(data[0])
    p2_y_len, p2_x_len = y_len * 5, x_len * 5

    p1 = deezstra(gen_grid(data, len(data), len(data[0])), (0, 0), (x_len - 1, y_len - 1))
    n_data = []
    for y in range(p2_y_len):
        n_line = []
        for x in range(p2_x_len):
            n_line.append((data[y%y_len][x%x_len] + (x // x_len) + (y // y_len) - 1) % 9 + 1)
        n_data.append(n_line)
    p2 = deezstra(gen_grid(n_data, p2_y_len, p2_x_len), (0, 0), (p2_x_len - 1, p2_y_len - 1))

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
