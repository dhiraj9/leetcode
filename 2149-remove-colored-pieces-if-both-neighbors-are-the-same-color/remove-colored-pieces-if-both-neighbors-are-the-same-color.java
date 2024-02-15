class Solution {
    public boolean winnerOfGame(String colors) {
        boolean result = false;
        int a_count = countConsecutive(colors, 'A');
        int b_count = countConsecutive(colors, 'B');
        if (a_count > b_count) {
            result = true;
        }
        else {
            result = false;
        }
        return  result;
    }

    private int countConsecutive(String s, char ch) {
        int c = 0;
        int i = 1;

        while (i < s.length() - 1) {
            if (s.charAt(i) == ch && s.charAt(i - 1) == s.charAt(i) && s.charAt(i + 1) == s.charAt(i)) {
                c++;
            }
            i++;
        }
        return c;
    }
}