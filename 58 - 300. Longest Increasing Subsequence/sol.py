'''
第一种方法是用dp,利用dp数组为0...n-1
dp[n] 代表长度为n的子数列的最长子数组的长度
当我们遇到当前元素nums[i]时候
我们需要进行二重循环,遍历dp[0] -> dp[i-1]
计算当前dp[i]

dp[i] 的值是j in dp[0] to dp[i-1]中,如果我们遇到
nums[j] < nums[i] 时候,那么我们的dp[i] = dp[j] + 1
如果我们遇到nums[j] >= nums[i] 时候,dp[i] 值不变
我们只有遇到dp数组里面的元素比当前元素小的时候,才会更新dp数组
因此,dp[i] = max(dp[i], dp[j] + 1)

'''

'''
很显然,第一种方法的时间复杂度是n^2,想要降低时间复杂度,那么我们需要采用另一个数组tris

tris的构造方法是,从0-k的元素中,最长的子数列的长度。

当我们遇到当前元素,nums[i]时候,可以分下面情况:
1. 假设nums[i] > tris[-1],那么直接把nums[i]加入到tris里面,这是唯一的让tris变长的方法
2. 如果nums[i] < tris[-1],我们需要把nums[i]插入到tris里面
    用二分法,找到一个比nums[i]大的最小元素,把这个元素替换成nums[i]

通过这样,我们可以不断用更小的值来更新tris,返回值是tris的长度

'''



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tris = []
        for i in range(len(nums)):
            self.fitTris(tris, nums[i])
        return len(tris)
            
    def fitTris(self, tris, cur):

        if len(tris) == 0:
            tris.append(cur)
        elif tris[-1] < cur:
            tris.append(cur)
        else:
            l = 0
            r = len(tris) -1
            res = 0
            while l <= r:
                mid = (l + r) // 2
                if tris[mid] > cur:
                    res = mid
                    r = mid -1
                elif tris[mid] == cur:
                    return
                else:
                    l = mid + 1
            tris[res] = cur
        
            
            
        

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     dp = [ 1 for i in range(len(nums)) ]
    #     res = 0
    #     for i in range(len(nums)):
    #         for j in range(0, i):
    #             if nums[j] < nums[i]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #         res = max(res, dp[i])
    #         # print(dp)
    #     return res
                
        
                
        
        