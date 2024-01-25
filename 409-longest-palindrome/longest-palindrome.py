class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = Counter(s)
        b = 0
        c = False
        for i in a.values():
            if i % 2 == 0:
                b += i
            else:
                b += i - 1
                c = True
        if c:
            b += 1
        return b
        



