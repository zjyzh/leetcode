class Solution:
    def maxProduct(self, s: str) -> int:
        if len(s) == 2 :
            return 1

        n = len(s)
        res = 0 
        for i in range(1<<n):
            '''
            use bit map for choosing the all possible subset
            it should be in time complixity of 2^n
            '''
            subset = [s[j] for j in range(n) if i & (1 << j)]
            remaining = [s[j] for j in range(n) if not (i & (1 << j))]
            substr = ''.join(subset)
            remainstr = ''.join(remaining)
            res = max(self.getMax(substr) * self.getMax(remainstr), res)

        return res

    def getMax(self, string):

        if len(string) == 0:
            return 0
        
        n = len(string)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = 1
        
        '''
        the define of dp[i][j] is the maxinum length of 
        the palindromic sub string between str[i] and str[j]
        '''

        # first loop was for the length
        for length in range(2,n+1):
            t = n - length + 1
            # print(t)
            # second loop was for the j
            # we start from the biggest j,then we move it to the next
            # here we didn't limit it to i < j since if i > j it will
            # reach 0, which means nothing in here
            for i in range(t):
                j = i + length -1
                if string[i] == string[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][n-1]


            
            
        return res

        

        