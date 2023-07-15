class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        connected = 0
        def dfs(i):
            visited.add(i)
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    dfs(j)
        for i in range(n):
            if i not in visited:
                dfs(i)
                connected += 1
        return connected
