class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = Counter(s)
        c = 0
        b = False
        for i in a.values():
            if i % 2 == 0:
                c += i
            if i == 1:
                b = True
            if i % 2 == 1:
                c += i - 1
                b = True
        if b:
            c += 1
        return c

