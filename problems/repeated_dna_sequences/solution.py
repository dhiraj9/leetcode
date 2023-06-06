class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        a = set()
        b = set()
        for i in range(0, len(s)-9):
            if s[i:10+i] in a:
                b.add(s[i:10+i])
            a.add(s[i:10+i])
        c = list(b)
        # Your code will replace this placeholder return statement
        return c