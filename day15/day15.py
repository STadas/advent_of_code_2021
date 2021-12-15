from pathlib import Path


def dijkfdsa(nodes, edges):
    lengths = {n: float('inf') for n in nodes}
    lengths[(0, 0)] = 0

    adj = {n: {} for n in nodes}
    for (u, v), w_uv in edges.items():
        adj[u][v] = w_uv

    temp_nodes = [n for n in nodes]
    while len(temp_nodes) > 0:
        upper_bounds = {v: lengths[v] for v in temp_nodes}
        u = min(upper_bounds, key=upper_bounds.get)
        temp_nodes.remove(u)

        for v, w_uv in adj[u].items():
            lengths[v] = min(lengths[v], lengths[u] + w_uv)

    return lengths


def xd():
    data = [[int(x) for x in line] for line in open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()]
    y_len, x_len = len(data), len(data[0])
    nodes = tuple((x, y) for y in range(y_len) for x in range(x_len))
    edges = {}
    for x, y in nodes:
        if x > 0:
            edges[(x, y), (x-1, y)] = data[y][x-1]
        if y > 0:
            edges[(x, y), (x, y-1)] = data[y-1][x]
        if x < x_len - 1:
            edges[(x, y), (x+1, y)] = data[y][x+1]
        if y < y_len - 1:
            edges[(x, y), (x, y+1)] = data[y+1][x]
    p1 = dijkfdsa(nodes, edges)[x_len - 1, y_len - 1]

    n_data = []
    n_y_len, n_x_len = y_len * 5, x_len * 5
    for y in range(n_y_len):
        n_line = []
        for x in range(n_x_len):
            mod = (x // x_len) + (y // y_len)
            n_line.append((data[y%y_len][x%x_len] + mod - 1) % 9 + 1)
        n_data.append(n_line)

    nodes = tuple((x, y) for y in range(n_y_len) for x in range(n_x_len))
    edges = {}
    for x, y in nodes:
        if x > 0:
            edges[(x, y), (x-1, y)] = n_data[y][x-1]
        if y > 0:
            edges[(x, y), (x, y-1)] = n_data[y-1][x]
        if x < n_x_len - 1:
            edges[(x, y), (x+1, y)] = n_data[y][x+1]
        if y < n_y_len - 1:
            edges[(x, y), (x, y+1)] = n_data[y+1][x]

    # why yes this does take around 4 hours on my laptop how could you tell?
    p2 = dijkfdsa(nodes, edges)[n_x_len - 1, n_y_len - 1]

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
