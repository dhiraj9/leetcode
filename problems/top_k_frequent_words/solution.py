class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordmap = Counter(words)
        return sorted(wordmap, key=lambda x: (-wordmap[x], x))[:k]
