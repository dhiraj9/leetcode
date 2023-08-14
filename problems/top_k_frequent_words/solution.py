import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordmap = Counter(words)
        minheap = [(-freq, word) for word, freq in wordmap.items()]
        heapq.heapify(minheap)
        result = []
        while k>0:
            result.append(heappop(minheap)[1])
            k -= 1
        return result

