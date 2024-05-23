class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0' and b == '0':
            return "0"
        a = a[::-1]
        c = 0
        d = 0
        for i in a:
            c += int(i) * 2 ** d
            d += 1
        b = b[::-1]
        e = 0
        for i, j in enumerate(b):
            e += int(j) * 2 ** i
        c = c + e
        f = ""
        while c > 0:
            f += str(c % 2)
            c //= 2
        return f[::-1]


