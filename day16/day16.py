from pathlib import Path
import binascii
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
        p_len_id = p_body[0]
        p_body = p_body[1:]
        sp_pos = 0
        literal_vals = []

        if p_len_id == "0":
            sp_len_combined = int(p_body[:15], 2)
            p_body = p_body[15:]
            while sp_pos + 1 < sp_len_combined:
                sp_ver, sp_len, val = parse_packet(p_body[sp_pos:])
                p_ver += sp_ver
                sp_pos += sp_len
                literal_vals.append(val)
            return p_ver, 22 + sp_pos, op[p_type](literal_vals)
        else:
            sp_count = int(p_body[:11], 2)
            p_body = p_body[11:]
            for i in range(sp_count):
                sp_ver, sp_len, val = parse_packet(p_body[sp_pos:])
                p_ver += sp_ver
                sp_pos += sp_len
                literal_vals.append(val)
            return p_ver, 18 + sp_pos, op[p_type](literal_vals)


def xd():
    data = open(str(Path(__file__).parent.absolute()) + "/input").read().splitlines()

    bin_str = bin(int(data[0], 16))[2:].zfill(4)
    bin_str = "0" * ((4 - len(bin_str)) % 4) + bin_str

    p1, _, p2 = parse_packet(bin_str)
    print(f"{p1=}")
    print(f"{p2=}")


if __name__ == "__main__":
    xd()
