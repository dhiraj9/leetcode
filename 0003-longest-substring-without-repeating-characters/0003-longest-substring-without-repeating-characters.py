class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    left = 0
    a = set()
    result = 0
    for i in range(len(s)):
      while s[i] in a:
        a.remove(s[left])
        left += 1 
      a.add(s[i])
      result = max(result, i - left + 1)
    return result
      
