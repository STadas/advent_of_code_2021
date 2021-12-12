from pathlib import Path
import time


def dfs(graph, p, part2=False):
    if p[-1] == "end":
        return [p]
    done = []
    for n in graph[p[-1]]:
        if part2:
            lowers = tuple(c for c in p if c.islower())
            no_dupes = len(lowers) == len(set(lowers))
        if n.isupper() or ((n not in p or (part2 and no_dupes)) and n != "start"):
            for d in dfs(graph, p + [n], part2):
                done.append(d)
    return done


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()

    graph = {}
    for line in data:
        a, b = line.split("-")
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
        graph[a].add(b)
        graph[b].add(a)

    last = time.time()
    p1 = len(dfs(graph, ["start"]))
    p2 = len(dfs(graph, ["start"], True))
    print("duration", str(time.time() - last)[:5])

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
