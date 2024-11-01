'''
直接贪心,双指针,将指针左右安放,然后merge
一个指针值较小的。优化就是直接把删除的元素跳过
就没有必要对原始的数组修改,记录修改的过程就行了。
'''


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = 0  # To count the number of merge operations

        while l < r:
            if nums[l] == nums[r]:
                # Move both pointers inward if values match
                l += 1
                r -= 1
            elif nums[l] < nums[r]:
                # Merge on the left side
                nums[l + 1] += nums[l]
                l += 1
                res += 1
            else:
                # Merge on the right side
                nums[r - 1] += nums[r]
                r -= 1
                res += 1

        return res
