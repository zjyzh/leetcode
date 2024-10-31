from typing import List

'''
用dfs + 路径的encode来识别每一次的岛屿
然后放进set里面
'''


class Solution:
    def dfs(self, grid, x, y, x0, y0, path, direction):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 1:
            return
        
        # Mark the cell as visited
        grid[x][y] = 2
        # Add the direction to the path
        path.append(direction)
        
        # Perform DFS in all four directions
        self.dfs(grid, x + 1, y, x0, y0, path, "D")  # down
        self.dfs(grid, x - 1, y, x0, y0, path, "U")  # up
        self.dfs(grid, x, y + 1, x0, y0, path, "R")  # right
        self.dfs(grid, x, y - 1, x0, y0, path, "L")  # left
        
        # Mark the return path for backtracking
        path.append("B")  # backtrack

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        unique_shapes = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    path = []
                    self.dfs(grid, i, j, i, j, path, "O")  # start with "O" for origin
                    unique_shapes.add("".join(path))
        
        return len(unique_shapes)




# directions = [-1, 0, 1, 0, -1]


# class Solution:

#     def dfs(self, grid, x0, y0, x, y, strset):
        
#         if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 2 or grid[x][y] == 0:
#             return False
        
#         grid[x][y] = 2
#         # print('x, y',x,y)
#         strset.append((x - x0, y-y0))
#         for i in range(4):
#             newx = x + directions[i]
#             newy = y + directions[i+1]
#             # print('newx,',newx, newy)
#             self.dfs(grid, x0, y0, newx, newy, strset)
        
#         return True



#     def numDistinctIslands(self, grid: List[List[int]]) -> int:

#         res = 0
#         resset = set()
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1:
#                     strset = []
#                     # print('have 1', i, j)
#                     if self.dfs(grid,i, j, i, j, strset):
#                         # print(strset)
#                         resset.add(frozenset(strset))
        
#         # print(resset)
#         return len(resset)


        


        
        