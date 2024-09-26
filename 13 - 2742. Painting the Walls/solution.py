from collections import defaultdict
import sys
class Solution:


    """
    dp[i][j] = the min cost if you complete the first i task,
    with time difference between paid worker and free worker

    j = time of paid worker - time of free worker

    for i in range(n):
        for j in range(-n, n):

            # if I choose to use the free worker
            dp[i+1][j - 1] = min(dp[i+1][j-1], dp[i][j]) 
            
            if I choose to use the paid worker
            dp[i+1][min(n, j + times[i+1])] = min(dp[i+1][min(n, j + times[i])], dp[i][j] + cost[i+1])

    return min( dp[n][j] for j >= 0 )

    everyone could use cost[i] to finish 1+time[i] since every paid worker 
    could call a free worker

    choose the minium cost to finish n tasks by choosing some of the worker

    dp[i][j]: the minium cost if you have considered the first i worker
    and completed j task

    j is posibile to larger than n


    for i in range(1, n+1):
        for j in range(n+1):
            dp[i][j] is known
            dp[i+1][min(j + 1+ time[i+1],n)] = min(dp[i+1][min(j + 1+ time[i+1],n)],dp[i][j] + cost[i+1]
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])

    return dp[n][n]

    """

    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(time)
        dp = [ defaultdict(lambda: sys.maxsize // 2 ) for i in range(n+1) ]
        cost.insert(0, 0)
        time.insert(0, 0)

        dp[0][0] = 0



        # for i in range(0, n):
        #     for j in range(-n, n+1):
        #         dp[i+1][j-1] = min(dp[i+1][j-1], dp[i][j])
        #         dp[i+1][min(n, j+time[i+1])] = min( dp[i+1][min(n, j+time[i+1])], 
        #                                             dp[i][j] + cost[i+1])

        # mincost = sys.maxsize // 2
        # # print(dp)
        # for i in range(0, n+1):
        #     mincost = min(mincost, dp[n][i])
        
        """
        down here is the code for the second method
        """


        for i in range(0, n):
            for j in range(n+1):
                # dp[i][j] is known
                dp[i+1][min(j + 1+ time[i+1],n)] = min(dp[i+1][min(j + 1+ time[i+1],n)],dp[i][j] + cost[i+1])
                dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        
        return dp[n][n]


        