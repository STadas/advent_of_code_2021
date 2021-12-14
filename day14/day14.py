from pathlib import Path


def default_val(d, k, default):
    if k not in d:
        d[k] = default


def do_steps(p_counts, rules, template, steps):
    for _ in range(steps):
        n_counts = {}
        for pair, count in p_counts.items():
            default_val(n_counts, pair1 := pair[0] + rules[pair], 0)
            default_val(n_counts, pair2 := rules[pair] + pair[1], 0)
            n_counts[pair1] += count
            n_counts[pair2] += count
        p_counts = n_counts

    c_counts = {}
    for pair, count in p_counts.items():
        default_val(c_counts, ch := pair[0], 0)
        c_counts[ch] += count
    c_counts[template[-1]] += 1

    return max(c_counts.values()) - min(c_counts.values())


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()

    template = data[0]
    rules = {p: ch for p, ch in (d.split(" -> ") for d in data[2:])}

    p_counts = {}
    for i in range(len(template) - 1):
        default_val(p_counts, pair := template[i] + template[i+1], 0)
        p_counts[pair] += 1

    p1 = do_steps(p_counts.copy(), rules, template, 10)
    p2 = do_steps(p_counts.copy(), rules, template, 40)

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
