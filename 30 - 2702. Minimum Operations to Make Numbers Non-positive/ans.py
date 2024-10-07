"""
we define upper and lower for the operation
then we check for a mid, can we do it using mid operation?
if we can, just take the opper = mid - 1
else take lower = mid + 1

to find the fastest way to check for weather 
mid time we can change everything into 0
we just need to use every element to minus y * mid times
then we pick up the lagest element to minus (x-y) * mid times
if we can finish it using mid times, return True.

"""



class Solution:

    # check if we can do it using m step
    def can(self, nums, x, y, m):
        currentNum = [ (i - y*m) for i in nums]
        step = x - y
        
        for i in range(len(currentNum) -1, -1, -1):
            cur = currentNum[i]
            if cur > 0:
                if cur % step == 0:
                    m -= cur // step
                else:
                    m -= ((cur// step) +1)
            else:
                break
        if m < 0:
            return False
        else:
            return True


    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        nums = sorted(nums)
        i = len(nums) -1
        maxnum = nums[-1]
        res = 0

        upper = 0
        s = sum(nums)
        if s % x == 0:
            upper =  (s // x )
        else:
            upper =  (s // x  + 1)

        if len(nums) == 1:
            return upper


        left = 0
        right = upper
        res = 0
        # check every step to see we can do it or not
        while left <= right:
            mid = (left + right) // 2
            if self.can(nums, x, y, mid):
                right = mid - 1
                res = mid
            else:
                left = mid + 1
        return res




        # while maxnum > 0:
            
        #     print('maxnum before', maxnum)
        #     # res += 1
        #     times = 0
        #     print("op    ", res)
        #     if maxnum % x == 0:
        #         times = (maxnum // x )
        #     else:
        #         times = (nums[-1] // x  + 1)

        #     for j in range(len(nums) - 1):
        #         nums[j] -= y * times
        #     maxnum -= x*times
        #     res += times
        #     t = len(nums) -2
        #     swap = False
        #     print(t, maxnum, nums[t])
        #     while t >= 0 and maxnum < nums[t]:
        #         swap = True
        #         print('swap', t, t+1, nums[t],nums[t+1])
        #         nums[t+1] = nums[t]

        #         t -= 1
        #     if swap:
        #         t += 1
        #         nums[t] = maxnum
        #         print(t, nums[t])
        #     else:
        #         nums[-1] = maxnum
        #     maxnum = nums[-1]
        #     print('maxnum', maxnum)
        #     for s in nums:
        #         print(s, end='. ')
        #     print()
                
        # return res
            
        