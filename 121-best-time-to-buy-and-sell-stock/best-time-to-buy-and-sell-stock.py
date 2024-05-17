class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = 0
        l = 0
        for r in range(1, len(prices)):
            b = prices[r] - prices[l]
            if b > a:
                a = b
            if prices[r] < prices[l]:
                l = r
        return a

