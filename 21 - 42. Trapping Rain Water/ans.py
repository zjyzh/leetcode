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
        









