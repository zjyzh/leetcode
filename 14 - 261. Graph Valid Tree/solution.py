class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        self.graph = [ set() for i in range(n)]

        for i in edges:
            innode = i[0]
            outnode = i[1]
            self.graph[innode].add(outnode)
            self.graph[outnode].add(innode)
        
        self.visited = [ 0 for i in range(n)]
        self.res = True
        self.dfs(0)
        for i in range(n):
            if self.visited[i] != 2:
                self.res = False
        return self.res

    def dfs(self, node):

        if self.visited[node] == 0:
            self.visited[node] = 1
            for child in self.graph[node]:
                self.dfs(child)
            self.visited[node] = 2
            
        elif self.visited[node] == 1:
            return
        elif self.visited[node] == 2:
            self.res = False 
            return

            













        
        
        