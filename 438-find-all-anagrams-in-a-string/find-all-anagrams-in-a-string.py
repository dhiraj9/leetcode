class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a = len(p)
        b = collections.Counter(p)
        c = []
        for i in range(0, len(s) - a + 1):
            if collections.Counter(s[i: i + a]) == b:
                c.append(i)
        return c
                
