class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c=0
        a=len(s)
        b=len(t)
        for i in s:
            if i not in t:
                return False
            if s.count(i)==t.count(i):
                c+=1
            if c==max(a,b):
                return True
        