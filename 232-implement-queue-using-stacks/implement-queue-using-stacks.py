class MyQueue:

    def __init__(self):
        self.a, self.b = [], []

    def push(self, x: int) -> None:
        while self.a:
            self.b.append(self.a.pop())
        self.a.append(x)
        while self.b:
            self.a.append(self.b.pop())

    def pop(self) -> int:
        return self.a.pop()

    def peek(self) -> int:
        return self.a[-1]

    def empty(self) -> bool:
        return len(self.a) == 0

