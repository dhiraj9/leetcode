class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pairs = 0
        duration_dict = defaultdict(int)
        for song_length in time:
            if not song_length % 60:
                pairs += duration_dict[0]
            else:
                pairs += duration_dict[60 - (song_length % 60)]
            duration_dict[song_length % 60] += 1
        return pairs

