class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        a = []
        for i in arr:
            c = 0
            d = i
            while i:
                c += i % 2
                i //= 2
            a.append((c, d))
        a.sort(key=lambda x: (x[0], x[1]))
        c = []
        for i in a:
            c.append(i[1])
        return c
