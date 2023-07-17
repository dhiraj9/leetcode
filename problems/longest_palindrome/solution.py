class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = {}
        for i in s:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        c = 0
        found = False
        for i, j in a.items():
            if j % 2 == 0:
                c += j
            else:
                c += j - 1
                found = True
        if found:
            c += 1
        return c
            
            

