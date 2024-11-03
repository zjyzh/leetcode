'''
解题方法就是将数字全部存到set里面
然后遍历这个set的数字。
开始遍历的时候，如果当前数字为n
那么判断n-1是否在set里面
如果n-1不在set里面，那就代表当前数字是开头
那么通过循环判断以n开头的,n+1, n+2, n+3 ... 是否在set里面
通过这个方法，记录最长的连续数字
返回结果
'''




class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list to a set for O(1) membership checks
        num_set = set(nums)
        longest_sequence = 0

        for num in num_set:
            # Only check for the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_sequence = 1

                # Count the length of the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_sequence += 1

                # Update the longest sequence found
                longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence



# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:

#         hashmap = {}
#         for n in nums:
#             if not n in hashmap:
#                 hashmap[n] = 1
        
#         res = 0
#         for n in hashmap.keys():
#             if n in hashmap and not (n-1) in hashmap:
#                 cur = n
#                 l = 0
#                 while cur in hashmap:
#                     # hashmap[cur] += 1
#                     cur += 1
#                     l += 1
#                 res = max(res, l)
#         return res
                

                    
                    

        