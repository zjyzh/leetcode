class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        '''
        mat_sum is the sum from mat[0] to mat[i][j]
        here we add additional col to the mat_sum
        so that when we access mat[-1][-1] it's 0
        prettty nice design
        '''


        m = len(matrix)
        n = len(matrix[0])
        self.mat_sum = [ [0 for i in range(n+1)] for j in range(m+1)]

        self.mat_sum[0][0] = matrix[0][0]
        for i in range(1,m):
            self.mat_sum[i][0] = self.mat_sum[i-1][0] + matrix[i][0]
        
        for j in range(1,n):
            self.mat_sum[0][j] = self.mat_sum[0][j-1] + matrix[0][j]

        for i in range(1,m):
            for j in range(1,n):
                self.mat_sum[i][j] = self.mat_sum[i-1][j] + self.mat_sum[i][j-1] + matrix[i][j] - self.mat_sum[i-1][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        return self.mat_sum[row2][col2] - self.mat_sum[row2][col1-1] - self.mat_sum[row1-1][col2] + self.mat_sum[row1-1][col1-1] 
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)