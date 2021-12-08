from pathlib import Path


def chk(w, against, needed_len):
    w, against = set(w), set(against)
    return len(w & against) == needed_len and w != against


def decode(ws):
    d = {}
    for w in ws:
        wl = len(w)
        num = lm[wl] if wl in (lm := {2: 1, 3: 7, 4: 4, 7: 8}) else None
        if num:
            d[num] = w

    for w in ws:
        wl = len(w)
        if wl == 5:
            num = 3 if chk(w, d[1], 2) else 5 if chk(w, d[4], 3) else 2
            d[num] = w
        elif wl == 6:
            num = 9 if chk(w, d[4], 4) else 0 if chk(w, d[1], 2) else 6
            d[num] = w
    return {v: str(k) for k, v in d.items()}


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()

    p1, p2 = 0, 0
    for line in data:
        inp, outp = (x.split() for x in line.split(" | "))
        translator = decode(inp + outp)
        decoded = ""
        for w in outp:
            p1 += len(w) in (2, 3, 4, 7)
            for k in translator.keys():
                if set(w) == set(k):
                    decoded += translator[k]
                    break
        p2 += int(decoded)

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
