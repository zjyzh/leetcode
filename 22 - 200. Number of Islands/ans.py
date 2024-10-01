direction = [1, 0, -1, 0, 1]

class Solution:

    def dfs(self, x, y):
        '''
        just do simple dfs, and we set it to '#' without recovering
        just return to True
        '''
        if x < 0 or x >= self.m:
            return False
        if y < 0 or y >= self.n:
            return False
        
        if self.grid[x][y] == '0'  or self.grid[x][y] == '#':
            return False

        t = self.grid[x][y]
        self.grid[x][y] = '#'
        for i in range(4):
            nextx = x + direction[i]
            nexty = y + direction[i+1]
            self.dfs(nextx, nexty)
            
        return True


    def numIslands(self, grid: List[List[str]]) -> int:

        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        res = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == '1' and self.dfs(i, j):
                    res += 1
        return res
                

        