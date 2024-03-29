class Solution {
    public int countSubstrings(String s) {
        int n = s.length();
        boolean[][] dp = new boolean[n][n];
        int res = 0;
        for (int len = 1; len <= n; len++) {
            for (int i = 0, j = i + len - 1; j < n; i++, j++) {
                if (len == 1) {
                    dp[i][i] = true;
                    res++;
                } else if (len == 2) {
                    dp[i][i + 1] = s.charAt(i) == s.charAt(i + 1);
                    if (dp[i][i + 1]) res++;
                }
                else {
                    dp[i][j] = s.charAt(i) == s.charAt(j) && dp[i + 1][j - 1];
                    if (dp[i][j]) res++;
                }
            }
        }
        return res;
    }
}