class Solution:
    def romanToInt(self, s: str) -> int:
        a = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        for i in range(len(s)):
            if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:
                result -= a[s[i]]
            else:
                result += a[s[i]]
        return result