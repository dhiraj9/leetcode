class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            a = str(x)[::-1].lstrip('0')
            b = a[:len(a)-1]
            if int(b) * -1 < -2 ** 31:
                return 0
            return int(b) * -1
        if int(str(x)[::-1]) > 2 ** 31:
            return 0
        if x == 0:
            return 0
        return int(str(x)[::-1].lstrip('0'))