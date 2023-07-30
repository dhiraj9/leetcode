class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        a, b = {}, {}
        for i in range(len(p)):
            a[p[i]] = 1 + a.get(p[i], 0)
            b[s[i]] = 1 + b.get(s[i], 0)
        result = [0] if a == b else []
        l = 0
        for r in range(len(p), len(s)):
            b[s[r]] = 1 + b.get(s[r], 0)
            b[s[l]] -= 1
            if b[s[l]] == 0:
                b.pop(s[l])
            l += 1
            if b == a:
                result.append(l)
        return result
