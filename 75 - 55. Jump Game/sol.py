
from typing import List

'''
非常简单的贪心方法，维护一个能访问的最远距离的变量
每次更新这个变量
'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            # If we can't reach this position, break early
            if i > farthest:
                return False
            # Update the farthest point we can reach
            farthest = max(farthest, i + nums[i])
            # If we can reach or exceed the last index, return True
            if farthest >= len(nums) - 1:
                return True
        return False


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         farthest = nums[0]
#         for i in range(1,len(nums)):
#             if farthest >= i:
#                 farthest = max(nums[i]+i, farthest)

#         if farthest >= len(nums) -1:
#             return True
#         else:
#             return False
        