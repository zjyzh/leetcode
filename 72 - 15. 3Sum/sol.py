from typing import List

'''
三个数相加问题
需要固定一个数，然后将剩下两个数通过双指针的方法找到
可以从0到n固定一个数i
然后剩下的数从 i+1 到 n 找到两个
注意就是如果有重复的数，跳过
还有一些细节更新，比如提前结束等等。
在双指针寻找的时候，一个数可能对应多个双指针：
比如 
-2, -1, 3
-2, 1, 1
这样双指针要找到所有的结果。
同时双指针也要去重

'''



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array
        res = []
        
        for i in range(len(nums)):
            # If the current number is greater than 0, break out of the loop
            if nums[i] > 0:
                break
            # Skip duplicate elements to avoid redundant triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two-pointer technique
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                
                if three_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # Move left and right pointers to the next different elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif three_sum < 0:
                    left += 1  # We need a larger sum
                else:
                    right -= 1  # We need a smaller sum
        
        return res

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:

#         nums = sorted(nums)

#         res = set()
#         # visited = [0 for i in range(len(nums))]
#         for i in range(len(nums)):
#             # if not visited[i] == 1:

#             target = nums[i]
#             tres = self.twoSum(nums, -target, i+1, len(nums) -1)
#             if tres:
#                 for j in tres:
#                     res.add((target, j[0], j[1] ))
#                 # visited[tres[0]] = 1
#                 # visited[tres[1]] = 1
#             # visited[i] = 1
#         return list(res)

#     def twoSum(self, nums, target, begin, end):

#         l = begin
#         r = end
#         resset = []
#         while l < r:
#             # if visited[nums[l]] == 1:
#             #     l += 1
#             #     continue
            
#             # if visited[nums[r]] == 1:
#             #     r -= 1
#             #     continue
#             if nums[l] + nums[r] == target:
#                 resset.append([nums[l] , nums[r]])
#             if nums[l] + nums[r] > target:
#                 r -= 1
#             else:
#                 l += 1
#         return resset



            

        