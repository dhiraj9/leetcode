class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a, b = {}, {}
        for i in ransomNote:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
        for i in magazine:
            if i not in b:
                b[i] = 1
            else:
                b[i] += 1
        for i in a:
            if i not in b:
                return False
            if b[i] < a[i]:
                return False
        return True

