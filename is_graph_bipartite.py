class Solution:
    def isBipartite(self, graph):
        color = {}

        def dfs(node):
            for nei in graph[node]:
                if nei in color:
                    if color[nei] == color[node]:
                        return False
                else:
                    color[nei] = 1 - color[node]
                    if not dfs(nei):
                        return False
            return True

        for node in range(len(graph)):
            if node not in color:
                color[node] = 0
                if not dfs(node):
                    return False

        return True