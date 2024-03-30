class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = Counter(s)
        c = 0
        b = False
        for j, i in a.items():
            if i % 2 == 0:
                c += i
            else:
                c += i - 1
                i -= i - 1
            if i == 1:
                b = True
        if b:
            c += 1
        return c



