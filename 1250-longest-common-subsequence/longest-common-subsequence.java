class Solution {
    private int f(int i, int j, String text1, String text2, int[][] dp) {
        if (i == 0 || j == 0) return 0;
        if (dp[i][j] != -1) return dp[i][j];
        if (text1.charAt(i - 1) == text2.charAt(j - 1)) return dp[i][j] = 1 + f(i - 1, j - 1, text1, text2, dp);
        return dp[i][j] = Math.max(f(i - 1, j, text1, text2, dp), f(i, j - 1, text1, text2, dp));
    }
    public int longestCommonSubsequence(String text1, String text2) {
        int n = text1.length();
        int m = text2.length();
        int[][] dp = new int[n + 1][m + 1];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) dp[i][j] = -1;
        }
        return f(n, m, text1, text2, dp);
    }
}