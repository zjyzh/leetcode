
'''
依然采取类似的策略，看数列的哪一边是有序的，
然后通过判断最小值是否落在有序的一边来进行二分


'''


class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        if r == 0:
            return nums[0]

        while l <= r:

            mid = (l + r) //2

            if nums[l] <= nums[mid] : # 左边数列是有序的
                # 需要判断右边是不是也是有序的
                if nums[r] <= nums[mid]: 
                # 如果右边是无序的，那么结果一定落入到右边
                    l = mid + 1
                    continue
                else:
                # 如果右边是有序的，那么直接返回
                    return nums[l]
                    
            if nums[mid] <= nums[r]: # 右边序列是有序的
                # 这个时候需要判断左边的第一个是否比右边的最小值还小
                if (mid - 1) >= 0 and nums[mid -1] <= nums[mid]:
                    r = mid -1
                else:
                # 如果左边没有比最小值小，那么mid就是最小值
                    return nums[mid]
                    
        return nums[mid]