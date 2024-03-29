class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote)
        b = Counter(magazine)
        for i, j in a.items():
            if b[i] < j: return False
        return True

