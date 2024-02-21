class Solution {
    Set<String> dict;
    HashMap<String, Boolean> cache = new HashMap<>();
    public boolean wordBreak(String s, List<String> wordDict) {
        dict = new HashSet<>(wordDict);
        return helper(s);
    }
    private boolean helper(String s) {
        if (s == null || s.length() == 0) return true;
        if (cache.containsKey(s)) return cache.get(s);
        int n = s.length();
        for (int i = 1; i <= n; i++) {
            String left = s.substring(0, i);
            String right = s.substring(i, n);
            if (dict.contains(left) && helper(right)) {
                cache.put(s, true);
                return true;
            }
        }
        cache.put(s, false);
        return false;
    }
}