'''

首先用两个指针，left和right，代表列表的两端

然后维护两个变量：left_max 和right_max，分别代表当前列的左边
最大值和右边最大值

如果left小于等于right,那么把左边的指针向前移动，
同时计算当前左边指针能抓住的雨水，同时更新left_max

如果right_max < left_max，把右边指针向左移动，计算右边指针能抓住的雨水
同时更新right_max

不断移动直到两个相撞

'''


from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left = 0
        right = len(height) -1
        left_max = 0
        right_max = 0
        res = 0
        while left < right:

            if height[left] <= height[right]:
                if left_max <= height[left]:
                    left_max = height[left]
                else:
                    res +=  left_max - height[left]
                left += 1
            else:
                if right_max <= height[right]:
                    right_max = height[right]
                else:
                    res +=  right_max - height[right] 
                right -= 1
        return res
                    
            
        
        return res



'''
用两个数组：left 和 right，扫描两次
分别代表当前列的左边最大值和右边最大值
然后扫描height，看看当前height能承受多少的水
这样就是res
'''


# class Solution:
#     def trap(self, height: List[int]) -> int:
#         left = [0 for i in range(len(height))]
#         right = [0 for i in range(len(height))]

        
#         for i in range(1, len(height)):
#             left[i] = max(left[i-1], height[i-1])
        
#         for j in range(len(height) -2, 0, -1):
#             right[j] = max(right[j+1], height[j+1])
#         # print(left)
#         # print(right)
#         res = 0
#         for i in range(len(height)):
#             cur = min(left[i], right[i])
#             if height[i] < cur:

#                 res += (cur - height[i])
#         return res
        


class Solution:
    def trap(self, height: List[int]) -> int:

        '''
        left represent the left highest position
        right represent the right highest position
        so we can calculate the current position's water
        if the currentHigh < left or right
        then the current holding is min(left, right) - currentHigh
        else the current holding is 0
        '''
        left = [ 0 for i in range(len(height))]
        right = [ 0 for i in range(len(height))]

        leftmax = height[0]
        for i in range(1, len(height)):
            left[i] = leftmax
            leftmax = max(leftmax, height[i])

        rightmax = height[-1]
        for i in range(len(height) -1, 0, -1):
            right[i] = rightmax
            rightmax = max(rightmax,height[i])
        
        res = 0
        for i in range(1,len(height) -1):
            h = min(left[i], right[i])
            if h > height[i]:
                res += h - height[i]
        
        return res
        









