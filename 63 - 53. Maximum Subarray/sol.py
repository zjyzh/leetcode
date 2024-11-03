'''
需要维护一个变量，就是local的最优解
每次遇到一个新的数，我们将它加入到local中
如果新的结果比local大，那么我们需要将这个数纳入到我们的子数组
如果新的结果比local小，那么我们需要将这个数放弃掉
然后重新开始构建子数组，local = nums[i]

最后将res记录下来

'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        local = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            local = max(nums[i]+ local, nums[i])
            res = max(res, local)
        return res