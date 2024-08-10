class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    dict = defaultdict(list)
    for i in strs:
        count = [0] * 26
        for j in i:
            count[ord(j) - ord('a')] += 1
        dict[tuple(count)].append(i)
    result = []
    for i in dict.values():
        result.append(i)
    return result
