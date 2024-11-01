"""
非常简单,双指针,移动的时候抛弃掉比较小的高度的一个指针
如果两个高度一样,那么随便抛弃一个
循环返回最大值
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        res = 0
        while left < right:
            if height[left] > height[right]:
                res = max(res, height[right]*(right - left))
                right -= 1
            else:
                res = max(res, height[left] * (right - left))
                left += 1

        return res


        # left = [ 0 for i in range(len(height) + 1)]
        # right = [0 for i in range(len(height) + 1)]
        # cur = height[0]
        # res =0
        # for i in range(len(height) -1, 0, -1):
        #     # left[i] = cur
        #     # cur = max(height[i], cur)
        #     for j in range(i):
        #         if height[j] >= height[i]:
        #             res = max(res, (i-j) * height[i])
        #             break
        
        # for i in range(0, len(height)-1):
        #     # left[i] = cur
        #     # cur = max(height[i], cur)
        #     for j in range(len(height)-1, i, -1):
        #         if height[j] >= height[i]:
        #             res = max(res, (j-i)* height[i])
        #             break
        # return res
        
        # cur = height[-1]
        # for j in range(len(height) -2, -1, -1):
        #     right[i] = cur
        #     cur = max(height[i], cur)
        

