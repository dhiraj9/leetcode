import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        a = []
        for i in points:
            a.append(((i[0]**2 + i[1]**2), i))
        heapq.heapify(a)
        b = []
        while k:
            b.append(heapq.heappop(a)[1])
            k -= 1
        return b

