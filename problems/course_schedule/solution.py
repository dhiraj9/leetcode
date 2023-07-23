class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        a = {i: [] for i in range(numCourses)}
        for b, c in prerequisites:
            a[b].append(c)
        v = set()
        def d(cr):
            if cr in v:
                return False
            if a[cr] == []:
                return True
            v.add(cr)
            for j in a[cr]:
                if not d(j):
                    return False
            v.remove(cr)
            a[cr] = []
            return True
        for k in range(numCourses):
            if not d(k):
                return False
        return True