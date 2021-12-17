from pathlib import Path
from functools import reduce


op = {
    0: sum,
    1: lambda li: reduce(lambda x, y: x * y, li),
    2: min,
    3: max,
    5: lambda li: li[0] > li[1],
    6: lambda li: li[0] < li[1],
    7: lambda li: li[0] == li[1],
}


def parse_packet(p):
    p_ver, p_type, p_body = int(p[:3], 2), int(p[3:6], 2), p[6:]

    if p_type == 4:
        lit_str = ""
        i = 0
        while i < len(p_body):
            lit_str += p_body[i+1:i+5]
            if p_body[i] == "1":
                i += 5
            else:
                break
        return p_ver, 7 + len(lit_str) + i // 5, int(lit_str, 2)
    else:
        p_len_id, p_body = p_body[0], p_body[1:]
        mod = 15 if p_len_id == "0" else 11
        sp_limit, p_body = int(p_body[:mod], 2), p_body[mod:]

        sp_pos = 0
        lit_vals = []

        if p_len_id == "0":
            while sp_pos + 1 < sp_limit:
                sp_ver, sp_len, val = parse_packet(p_body[sp_pos:])
                p_ver += sp_ver
                sp_pos += sp_len
                lit_vals.append(val)
        else:
            for i in range(sp_limit):
                sp_ver, sp_len, val = parse_packet(p_body[sp_pos:])
                p_ver += sp_ver
                sp_pos += sp_len
                lit_vals.append(val)
        return p_ver, mod + 7 + sp_pos, op[p_type](lit_vals)


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()
    bin_str = bin(int(data[0], 16))[2:].zfill(4)
    p1, _, p2 = parse_packet("0" * ((4 - len(bin_str)) % 4) + bin_str)
    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
