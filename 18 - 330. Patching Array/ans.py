class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i = 0
        canCover = 1
        res = 0

        # canCover means that the current number that we can cover
        while canCover <= n:

            # in here, if the nums[i] <= canCover, 
            # we will update the canCover
            if i < len(nums) and nums[i] <= canCover:
                canCover += nums[i]
                i += 1
                
            else:
                # else, we will double the canCover, since we added a new number
                # which is the current 'canCover' number
                # since we can cover from 1 to canCover
                # when we added the canCover, we now can double our coverage range
                # so this is the double time
                canCover += canCover 
                res += 1
        return res


