class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split(' ')
        output = []
        for i in a:
            b = list(i)
            b.reverse()
            d = "".join(b)
            output.append(d)
        return " ".join(output)



