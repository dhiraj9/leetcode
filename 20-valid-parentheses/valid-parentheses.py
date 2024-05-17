class Solution:
    def isValid(self, s: str) -> bool:
        a = {')': '(', '}': '{', ']': '['}
        b = []
        for i in s:
            if i in a:
                if len(b) == 0:
                    return False
                if a[i] != b.pop():
                    return False
            else:
                b.append(i)
        return len(b) == 0

