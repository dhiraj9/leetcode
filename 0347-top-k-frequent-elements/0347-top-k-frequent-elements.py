class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i, j in Counter(nums).most_common(k):
            result.append(i)
        return result
            