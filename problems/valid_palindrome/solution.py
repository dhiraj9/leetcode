class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''
        s = s.lower()
        for i in s:
            if i.isalnum():
                a += i
        l = 0
        r = len(a)-1
        while l <= r:
            if a[l] != a[r]:
                return False
            l += 1
            r -= 1
        return True    


