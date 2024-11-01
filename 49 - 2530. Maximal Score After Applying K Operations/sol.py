'''
不需要什么操作,直接用最大堆就行了。
'''


import heapq

def heappush(pq, key):
    heapq.heappush(pq,-key)

def heappop(pq):
    val = - heapq.heappop(pq)
    return val
    

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        pq = []
        for i in nums:
            heappush(pq, i)
        
        res = 0
        while len(pq) > 0 and k > 0:
            k -= 1
            top = heappop(pq)
            res += top
            
            if top % 3 == 0:
                top = top //3
            else:
                top = top //3 + 1
            heappush(pq, top)

        return res
            
