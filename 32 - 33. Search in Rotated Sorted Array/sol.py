"""
参考这里，算法基于一个事实，数组从任意位置劈开后，至少有一半是有序的，什么意思呢？

比如 [ 4 5 6 7 1 2 3] ，从 7 劈开，左边是 [ 4 5 6 7] 右边是 [ 7 1 2 3]，左边是有序的。

基于这个事实。

我们可以先找到哪一段是有序的 (只要判断端点即可)，然后看 target 在不在这一段里，如果在，那么就把另一半丢弃。如果不在，那么就把这一段丢弃。

"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        if nums[left] == target:
            return left
        while left < right:

            mid = (left + right) // 2
            if nums[mid] == target :
                return mid
            
            if nums[left] == target:
                return left

            if nums[right] == target:
                return right
            
            if (right - left) == 1:
                return -1

            
            if nums[left] < nums[mid]:
                if nums[left] < target and target < nums[mid]:
                    right = mid -1
                    continue
                else:
                    left = mid + 1
            
                continue
            
            if nums[mid] < nums[right]:
                if nums[mid] < target and nums[right] > target:
                    left = mid + 1
                else:
                    right = mid -1
                continue
                
 
        return -1



                
        