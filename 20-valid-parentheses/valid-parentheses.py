class Solution:
    def isValid(self, s: str) -> bool:
        a = {')': '(', '}': '{', ']': '['}
        b = []
        for i in s:
            if i in a.values():
                b.append(i)
            else:
                if b:
                    if a[i] != b.pop():
                        return False
                else:
                    return False
        return len(b) == 0
