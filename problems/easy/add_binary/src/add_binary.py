def add_binary(a, b, c):
    res = int(a) + int(b) + int(c)
    if res == 0:
        return "0", "0"
    if res == 1:
        return "1", "0"
    if res == 2:
        return "0", "1"
    if res == 3:
        return "1", "1"


class Solution:

    def addBinary(self, a: str, b: str) -> str:
        carry = "0"
        long_seq, short_seq = (a, b) if len(a) > len(b) else (b, a)
        seq_a, seq_b = long_seq, ["0"] * (len(long_seq) - len(short_seq)) + list(short_seq)
        result = ["0"] * len(long_seq)

        for i in range(len(result) - 1, -1, -1):
            result[i], carry = add_binary(seq_a[i], seq_b[i], carry)

        result = "".join(result)

        if carry == "1":
            return "1" + result

        return result
