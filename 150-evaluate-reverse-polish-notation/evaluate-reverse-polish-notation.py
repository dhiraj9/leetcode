class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a = []
        for token in tokens:
            if token == '+':
                a.append(a.pop() + a.pop())
            elif token == '-':
                b = a.pop()
                c = a.pop()
                a.append(c - b)
            elif token == '*':
                a.append(a.pop() * a.pop())
            elif token == '/':
                b = a.pop()
                c = a.pop()
                a.append(int(c / b))
            else:
                a.append(int(token))
        return a[0]
