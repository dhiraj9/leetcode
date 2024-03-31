class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        c, d = 0, 0
        for i, j in enumerate(a):
            c += 2**i * int(j)
        for i, j in enumerate(b):
            d += 2**i * int(j)
        e = c + d
        if not e: return "0"
        f = ""
        while e:
            f += str(e % 2)
            e = e // 2
        return f[::-1]



