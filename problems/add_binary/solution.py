class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        carry = 0
        r = ""
        for i in range(max(len(a), len(b))):
            da = int(a[i]) if i < len(a) else 0
            db = int(b[i]) if i < len(b) else 0
            c = da + carry + db
            r = str(c%2) + r
            carry = c//2
        if carry:
            r = "1" + r
        return r