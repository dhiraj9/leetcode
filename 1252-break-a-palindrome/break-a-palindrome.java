class Solution {
    public String breakPalindrome(String palindrome) {
        if (palindrome.length() == 1)
            return "";
        char[] ar = palindrome.toCharArray();
        for (int i = 0; i < ar.length / 2;i++)
            if (ar[i] != 'a') {
                ar[i] = 'a';
                return String.valueOf(ar);
            }
        ar[ar.length - 1] = 'b';
        return String.valueOf(ar);
    }
}