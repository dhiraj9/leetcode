class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        a = []
        for x, y in points:
            a.append([x**2 + y**2, [x, y]])
        heapq.heapify(a)
        b = []
        while k:
            b.append(heapq.heappop(a)[1])
            k -= 1
        return b
