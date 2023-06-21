def transform(s,k):
    return s[:k][::-1]+s[k:]

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return ''.join(transform(s[i:i+2*k], k) for i in range(0,len(s), 2*k))
