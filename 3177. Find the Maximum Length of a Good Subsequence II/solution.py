from collections import defaultdict

# dp[i][t] = the longest subsequence we can get from [0:i]
#  where we can have t 
# times that seq[i] != seq[i+1]
# need to use two array to store the mid value
# max_value[t] = max(dp[j][t-1] + 1) for i in 0 to i-1
# max_all[t][idx] = max(dp[j][t] with idx == one nums)
# 

class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        max_value = [0 for i in range(k+1)]
        max_all = [  defaultdict(int) for i in range(k+1) ]


        # for i in range(1,len(nums)+1):
        dp = [ [0 for i in range(k+1)] for j in range(len(nums)+1)  ]
        # for i in range(k+1):
        #     dp[1][k] = 0
        # dp[1][0]
        ret = 1
        for i in range(len(nums)):
            for t in range(k+1):
                ans = 1
               
                # dp[i][t] = max(dp[j][t] + 1 if nums[j] == nums[i], res) 
                # in here, j is the number from 0 to i-1
                # else max(res, dp[i][t] = dp[j][t-1] + 1)
                # this is the most intuitive solution
                # but it will exceed the time limit
                # in here, we need to store the intermediate result
                # max_value[t] = max(dp[j][t-1] + 1) for j in 0 to i-1
                # max_all[t][idx] = max(dp[j][t] with idx == one nums)
                # 
                # for j in range(i):
                #     if nums[i] == nums[j]:
                #         ans = max(ans, dp[j][t] + 1)
                #     else:
                #         s = t-1
                #         if s < 0:
                #             continue
                #         ans = max(ans,dp[j][t-1] + 1)
                # dp[i][t] = ans
                # ret = max(ret, ans)

                ans = max(max_all[t][nums[i]] +1, ans)
                if t >= 1:
                    ans = max(max_value[t-1] + 1,ans)
                dp[i][t] = ans
                ret = max(ret, ans)
            
            for t in range(k+1):
                max_value[t] = max(max_value[t], dp[i][t])
                max_all[t][nums[i]] = max(max_all[t][nums[i]], dp[i][t])

        return ret