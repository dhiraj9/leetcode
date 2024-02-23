class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[] ahead = new int[2];
        int[] cur = new int[2];
        int profit = 0;
        for (int ind = n - 1; ind > -1; ind--) {
            for (int buy = 0; buy < 2; buy++) {
                if (buy == 1) profit = Math.max(prices[ind] + ahead[0], ahead[1]);
                if (buy == 0) profit = Math.max(-prices[ind] + ahead[1], ahead[0]);
                cur[buy] = profit;
            }
            ahead = cur;
        }
        return cur[0];
    }
}