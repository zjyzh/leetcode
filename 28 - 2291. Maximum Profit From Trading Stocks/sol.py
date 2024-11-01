import heapq
import sys
from collections import defaultdict

class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:


        '''
我们定义 dp[i][j] 表示前 i 支股票,预算为 j 时的最大收益。那么答案就是 f[n][budget]。

对于第 i 支股票,我们有两种选择:

-   不购买,那么 f[i][j] = f[i - 1][j]；
-   购买,那么 f[i][j] = f[i - 1][j - present[i]] + future[i] - present[i]。

最后返回 f[n][budget] 即可。

时间复杂度 $O(n times budget),空间复杂度 O(n times budget)。其中 n 为数组长度。

我们可以发现,对于每一行,我们只需要用到上一行的值,因此可以将空间复杂度优化到 O(budget)。
        '''
        n = len(present)
        dp = [[ 0 for i in range(budget +1)]  for j in range(n+1)]    
       
        for i in range(1,len(present)+1):
            for j in range(0, budget+1 ):
                
                dp[i][j] = dp[i-1][j]
                margin = future[i-1] - present[i-1]
                if j >= present[i-1] and margin >= 0:
                    # current budget is bigger than buying the stoct
                    dp[i][j] = max(dp[i-1][j-present[i-1]] + margin , dp[i-1][j] )
        
        return dp[n ][budget]







                

      