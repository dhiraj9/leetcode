class Solution:
    def firstBadVersion(self, n: int) -> int:
        a, b = 1, n
        while a < b:
            c = (a + b) // 2
            if isBadVersion(c) == False:
                a = c + 1
            else:
                b = c
        return b



