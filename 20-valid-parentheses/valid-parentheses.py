class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            if i in mapping.values():
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    if mapping[i] != stack.pop():
                        return False

        return len(stack) == 0

        