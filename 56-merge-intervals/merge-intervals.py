class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        r = [intervals[0]]
        for s, e in intervals:
            l = r[-1][1]
            if s <= l:
                r[-1][1] = max(e, l)
            else:
                r.append([s, e])
        return r



