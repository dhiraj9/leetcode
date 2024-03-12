class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in dictionary.values():
                stack.append(i)
            else:
                if stack:
                    if stack.pop() != dictionary[i]:
                        return False
                else:
                    return False
        return len(stack) == 0

