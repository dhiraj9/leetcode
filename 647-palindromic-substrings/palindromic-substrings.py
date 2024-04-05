class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                a = s[i:j]
                if a == a[::-1]:
                    c += 1
        return c
