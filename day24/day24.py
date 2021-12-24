from pathlib import Path

# no i dont think i will brute force this (i say and try anyway before this for the meme)
# [9,  9,  9,  9,   9,   9,  9,   9,  9,   9,   9,   9,   9,   9]
# the instructions seem to repeat completely except for the following lists
# div z [1,  1,  1,  1,   26,  26, 1,   26, 1,   26,  1,   26,  26,  26]
# add x [13, 11, 11, 10, -14, -4,  11, -3,  12, -12,  13, -12, -15, -12] 
# add y [10, 16, 0,  13,  7,   11, 11,  10, 16,  8,   15,  2,   5,   10]
# n in the 2nd list is negative whenever n in the 1st is 26
# got a hint from someone that its a stack
# instead of caring about 1s, and 26s we can just check if n in 2nd list is > 0

def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()
    p1 = 99999999999999
    p2 = 11111111111111
    stack = []
    for i in range(14):
        mod1 = int(data[5 + 18*i].split()[-1])
        mod2 = int(data[15 + 18*i].split()[-1])

        if mod1 > 0:
            stack.append((i, mod2))
        else:
            j, mod2 = stack.pop()
            # was getting desperate after multiple guesses, saw a pretty
            # much identical solution to mine on reddit so shamelessly
            # cop(i)ed the abs(mod1) >/< mod2 part (which also spoiled p2)
            # i want to see my family eric
            p1 -= abs((mod1+mod2) * pow(10, (13 - (i if abs(mod1) > mod2 else j))))
            p2 += abs((mod1+mod2) * pow(10, (13 - (i if abs(mod1) < mod2 else j))))

    # and here i thought it would be easier during the last 2 days
    # thank you for reading my blog
    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
