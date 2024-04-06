class Solution:
    def countBits(self, n: int) -> List[int]:
        r = []
        for i in range(n + 1):
            c = 0
            while i:
                c += i % 2
                i //= 2
            r.append(c)
        return r
            
