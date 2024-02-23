class Solution {
    private int getMaximumProfit(int[] prices, int ind, int buy, int[][] dp) {
        if (ind == prices.length) return 0;
        if (dp[ind][buy] != -1) return dp[ind][buy];
        int profit = 0;
        if (buy == 1) profit = Math.max(-prices[ind] + getMaximumProfit(prices, ind + 1, 0, dp), getMaximumProfit(prices, ind + 1, 1, dp));
        if (buy == 0) profit = Math.max(prices[ind] + getMaximumProfit(prices, ind + 1, 1, dp), getMaximumProfit(prices, ind + 1, 0, dp));
        dp[ind][buy] = profit;
        return profit;
    }
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] dp = new int[n][2];
        for (int i = 0; i < n; i++) dp[i][0] = dp[i][1] = -1;
        return getMaximumProfit(prices, 0, 1, dp);
    }
}



