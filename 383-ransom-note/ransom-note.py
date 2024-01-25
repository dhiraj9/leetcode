class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote)
        b = Counter(magazine)
        for i, j in a.items():
            if j > b[i]:
                return False
        return True
