import heapq

'''
用二分,快速判断一个k能不能被限时吃掉

在这用了优先队列

'''

def insert_heap(heap, value):
    heappush(heap, -value)

def pop_heap(heap):
    return - heappop(heap)

class Solution:

    def canEat(self, piles, h, k):
        # length = len(piles)
        # times = h // length
        # remain = h % length
        # per = k * times
        heap = []
        for i in range(len(piles)):
            # piles[i] -= per
            insert_heap(heap, piles[i])
        # print('pile', piles)
        # print('heap', heap)
        # for j in range(len(piles))
        # piles = sorted(piles, reverse = True)
        remain = h
        while remain > 0:
            top = pop_heap(heap)
            if top % k == 0:
                consume = top // k 
            else:
                consume = top // k + 1
            if consume ==0:
                consume += 1
            if top < 0:
                return True
            # print(top, consume, remain)
            
            if remain >= consume:
                remain -= consume
            else:
                return False
            top -= consume * k
            insert_heap(heap, top)
            # remain -= 1
        final = pop_heap(heap)
        # print(final)
        if final > 0:
            return False
        else:
            return True
        # for i in range(remain):



    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        # if len(piles) == 1:
        #     l = 1

        

        new_pile = copy.deepcopy(piles)
        if not self.canEat(new_pile, h, r-1):
            return r
        new_pile = copy.deepcopy(piles)

        while l <= r :
            mid = (l + r) // 2
            # print(new_pile)
            result = self.canEat(new_pile, h, mid)
            # print( h, mid,  result)
            if result:
                res = mid
                r = mid -1
            else:
                l = mid + 1
            new_pile = copy.deepcopy(piles)
        return res