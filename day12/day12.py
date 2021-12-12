from pathlib import Path


def dfs(graph, p, part2=False):
    if p[-1] == "end":
        return [p]
    done = []
    k = p[-1]
    for n in graph[k]:
        if part2:
            lowers = tuple(filter(lambda c: c.islower(), p))
            no_dupes = len(lowers) == len(set(lowers))
        if n.isupper() or ((n not in p or (part2 and no_dupes)) and n != "start"):
            for d in dfs(graph, p + [n], part2):
                done.append(d)
    return done


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()

    p1 = 0
    graph = {}
    for line in data:
        a, b = line.split("-")
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    p1 = len(dfs(graph, ["start"]))
    p2 = len(dfs(graph, ["start"], True))

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
