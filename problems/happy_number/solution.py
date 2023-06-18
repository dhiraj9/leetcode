class Solution:
    def isHappy(self, n: int) -> bool:
        # Write your code here
        a = set()
        while n not in a:
            a.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False
    
    def sumOfSquares(self, n: int) -> int:
        result = 0
        while n:
            digit = n % 10
            digit **= 2
            result += digit
            n = n // 10
        return result