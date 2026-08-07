class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = set()

        def dfs(city):
            visited.add(city)

            for nei in range(n):
                if isConnected[city][nei] == 1 and nei not in visited:
                    dfs(nei)

        provinces = 0

        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)

        return provinces