
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def calculate_sum(height: int, length: int) -> int:
            """
            Helper function to calculate the sum of the first 'length' elements of 
            a sequence decreasing from 'height'. If length > height, add 1s for the extra elements.
            """
            if length <= height:
                # Sum of the first 'length' elements of a decreasing sequence from 'height'
                return (height * (height + 1) // 2) - ((height - length) * (height - length + 1) // 2)
            else:
                # If 'length' exceeds 'height', add 1s for the remaining elements
                return (height * (height + 1) // 2) + (length - height)

        def can_construct(mid: int) -> bool:
            """
            Check if it's possible to construct the array with nums[index] = mid,
            while keeping the total sum <= maxSum.
            """
            left_sum = calculate_sum(mid - 1, index)  # Sum of elements to the left of 'index'
            right_sum = calculate_sum(mid - 1, n - index - 1)  # Sum of elements to the right of 'index'
            
            # Total sum including the peak element 'mid'
            total_sum = left_sum + right_sum + mid
            return total_sum <= maxSum

        # Binary search for the maximum possible value at nums[index]
        left, right, result = 1, maxSum, 0
        while left <= right:
            mid = (left + right) // 2
            if can_construct(mid):
                result = mid  # Update the result and try for a higher value
                left = mid + 1
            else:
                right = mid - 1

        return result

# class Solution:
#     def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
#         def fix(maxsum, n, idx, num):

#             if num ==0 or num == 1 and n <= maxsum:
#                 return True

#             lnum = num -1
#             lminnum = (lnum - idx) + 1
#             lsum = 0
            
#             if lminnum > 0:
#                 lsum = (lminnum + lnum) * idx // 2
#             else:
#                 lsum += (1 + lnum) * lnum //2
#                 lsum += (idx - lnum)
            
#             if idx == 0:
#                 lsum = 0

#             rnum = num -1
#             rdis = n - idx -1
#             rminnum = (rnum - rdis) + 1
#             rsum = 0
#             if rminnum > 0:
#                 rsum = (rminnum + rnum) * rdis //2
#             else:
#                 rsum += (1+rnum) * rnum //2
#                 rsum += (rdis - rnum)
            
#             if idx == n-1:
#                 rsum = 0
            

#             if (lsum + rsum + num) <= maxsum:
#                 return True
#             else:
#                 return False

            
#         l = 0
#         r = maxSum
#         res = 0
#         while l <= r:
#             mid = (l+r) //2
#             # print('l,r',l, r, mid)
#             if fix(maxSum, n , index, mid):
#                 res = mid
#                 l = mid +1
#             else:
#                 r = mid -1
#             # print('l,r',l, r, mid)
#         return res



        

        