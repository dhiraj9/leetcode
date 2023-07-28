class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        si = 1
        a = ""
        b = 0
        i = 0
        if len(s) != 0:
            if s[0] == '+':
                si = 1
                i += 1
            elif s[0] == '-':
                si = -1
                i += 1
        # if not s[1].isdigit():
        #     return b
        while i < len(s):
        # for i in s[1:]:
            if s[i].isdigit():
                a += s[i]
                i += 1
            else:
                break
        if a:
            b = int(a)
        c = b * si
        if c < - (2 ** 31):
            c = - (2 ** 31)
        if c > (2 ** 31) - 1:
            c = (2 ** 31) - 1
        return c

