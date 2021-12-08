from pathlib import Path


def check(word, against, needed_len):
    word = set(word)
    against = set(against)
    return len(word & against) == needed_len and word != against


def decode(inp, outp):
    decoded = {}
    combined = inp + outp
    for word in combined:
        if len(word) == 2:
            decoded["1"] = word
        elif len(word) == 3:
            decoded["7"] = word
        elif len(word) == 4:
            decoded["4"] = word
        elif len(word) == 7:
            decoded["8"] = word

    for word in combined:
        if len(word) == 5:
            if check(word, decoded["1"], 2):
                decoded["3"] = word
            elif check(word, decoded["4"], 3):
                decoded["5"] = word
            else:
                decoded["2"] = word
        elif len(word) == 6:
            if check(word, decoded["4"], 4):
                decoded["9"] = word
            elif check(word, decoded["1"], 2):
                decoded["0"] = word
            else:
                decoded["6"] = word
    return {v: k for k, v in decoded.items()}


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()

    p1 = 0
    p2 = 0
    for line in data:
        inp, outp = (x.split() for x in line.split(" | "))
        translator = decode(inp, outp)
        decoded = ""
        for word in outp:
            if len(word) in (2, 3, 4, 7):
                p1 += 1
            for k in translator.keys():
                if set(word) == set(k):
                    decoded += translator[k]
                    break
        p2 += int(decoded)

    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
