from pathlib import Path
from collections import Counter


def do_steps(p_counts, rules, template, steps):
    for _ in range(steps):
        n_counts = Counter()
        for pair, count in p_counts.items():
            n_counts[pair[0] + rules[pair]] += count
            n_counts[rules[pair] + pair[1]] += count
        p_counts = n_counts

    c_counts = Counter()
    for pair, count in p_counts.items():
        c_counts[pair[0]] += count
    c_counts[template[-1]] += 1

    return max(c_counts.values()) - min(c_counts.values())


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()

    template = data[0]
    rules = {p: ch for p, ch in (d.split(" -> ") for d in data[2:])}

    p_counts = Counter()
    for i in range(len(template) - 1):
        p_counts[template[i] + template[i+1]] += 1

    p1 = do_steps(p_counts.copy(), rules, template, 10)
    p2 = do_steps(p_counts.copy(), rules, template, 40)

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
