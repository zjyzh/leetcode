import heapq
import math

# class MaxHeap:
#     def __init__(self):
#         self.heap = []

#     def push(self, item):
#         heapq.heappush(self.heap, -item)
    
#     def pop(self):
#         return - heapq.heappop(self.heap)

#     def peek(self):
#         return -self.heap[0] if self.heap else None
    
#     def size(self):
#         return len(self.heap)


# solution :
# left and right half and half
# both pointer from right to left
# if they are greater, just res += 2, move the pointer
# if they are not, just move the pointer


class Solution(object):
    def minLengthAfterRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = len(nums) 
        # maxheap_left = MaxHeap()
        # maxheap_right = MaxHeap()
        mid = 0
        rightmid = 0
        res = 0
        if len(nums) % 2 == 1:
            mid = (right - left) // 2 - 1
            rightmid = mid + 2
            res = 1
        else:
            mid = (right - left) // 2 -1
            rightmid = mid + 1
            res = 0

        # mid = (right - left) // 2) - 1

        # left = nums[:mid+1]
        # right = nums[rightmid:]
        i = mid
        j = len(nums) -1
        # for i in nums[:mid+1]:
        #     maxheap_left.push(i)
        
        # for j in nums[rightmid:]:
        #     maxheap_right.push(j)
        
        while(i >= 0 and j>=rightmid):
            if nums[i] < nums[j]:
                i -= 1
                j -= 1
            else:
                i -= 1
                j -= 1
                res += 2
        
        return  res
         