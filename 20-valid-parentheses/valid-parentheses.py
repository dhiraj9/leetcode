class Solution:
    def isValid(self, s: str) -> bool:
        a = {')': '(', ']': '[', '}': '{'}
        b = []
        for i in s:
            if i in a.values():
                b.append(i)
            else:
                if b:
                    if b.pop() != a[i]:
                        return False
                else:
                    return False
        return not b

