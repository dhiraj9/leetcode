class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        a = 0
        i = 1
        b = x
        while x:
            a = a * 10 + x % 10
            i *= 10
            x //= 10
        return a == b



