'''
核心在于构造一个prefix数组
prefixsum数组需要单调递增

如果输入是[1,4,1,5]

prefix = [1, 5, 6, 11]

然后随机从1 - sum(w)数组中随机生成一个数
如果随机值为 1,那么落入到第一个
如果随机值为2,那么落入到第二个
采用二分法找到upper bound
注意二分的函数跳出的条件一定要落入到当前区间。

'''


import random
class Solution:

    def __init__(self, w: List[int]):

        # print(w)
        self.allsum = sum(w)
        # print(self.allsum)
        # w = sorted(w)
        self.prefix = [ 0 for i in range(len(w))]

        self.prefix[0] = w[0]
        for i in range(1, len(w)):
            self.prefix[i] = self.prefix[i-1] + w[i]
        # print(self.prefix)
        
        

    def findupper(self, target, prefix):
        l = 0
        r = len(prefix) - 1
        # print(prefix)
        while l <= r:
            mid = (l + r) //2
            # print(l, r, mid)
            if prefix[mid] == target:
                # print( target, prefix[mid-1], prefix[mid], mid)
                return mid 
            elif prefix[mid] < target:
                l = mid + 1
            elif prefix[mid] > target and mid -1 >= 0 and prefix[mid -1] < target:          
                # print( target, prefix[mid-1], prefix[mid], mid)
                return mid
            else:
                r = mid -1
        # print( target, prefix[mid-1], prefix[mid], mid)
        return mid



    def pickIndex(self) -> int:
        random_number = random.randrange(1, self.allsum+1)
        return self.findupper(random_number, self.prefix)





        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()