"""

3. 往地面倒水,给一个2d矩阵代表地块的高度,和初始水接触地块的row col 坐标。每秒水会往相邻的(上下左右)不高于当前高度的地块流,并把地块打湿。输出一个2d矩阵代表每个地块被打湿的时间,干燥的地块用-1
height = [[10, 10, 10],
         [4,    5,   6],
        [3,    2,   1]]
startrow = 1, startcol = 1
output = [[-1, -1, -1],
            [1,   0, -1],
            [2,   1, 2]]
"""

direction = [1, 0, -1, 0, 1]


# def dfs( height, x, y, initialHeight):
    
#     if height[x][y] >










