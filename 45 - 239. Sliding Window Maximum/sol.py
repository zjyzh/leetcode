from collections import deque

'''
单调队列,使用双端队列

1. 如果队列为空,从右边插入
2. 如果当前元素大于队尾元素,将元素弹出,直到当前元素小于或者等于队尾元素
3. 删除时候,看看当前删除的元素是否等于队列左边元素,如果相等就将左边元素弹出


'''


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        dq = deque()

        for i in range(k):
            if len(dq) == 0:
                dq.append(nums[i])
            else:
                while len(dq) > 0 and dq[-1] < nums[i]:
                    dq.pop()
                
                dq.append(nums[i])
        
        res = []
        for i in range(k ,len(nums)):

            res.append(dq[0])

            if len(dq) == 0:
                dq.append(nums[i])
            else:
                while len(dq) > 0 and dq[-1] < nums[i]:
                    dq.pop()
                dq.append(nums[i])
            
            former = nums[i -k]
            if dq[0] == former:
                dq.popleft()
        res.append(dq[0])
        return res

                  


        # pq = []
        # maxset = {}

        # if k == 1:
        #     return nums
        
        # for i in range(k):
        #     heapinsert(pq, nums[i])
        #     if nums[i] in maxset:
        #         maxset[nums[i]] += 1
        #     else:
        #         maxset[nums[i]] = 1
        
        # res = []
        
        # print(pq)
        # first = - pq[0]
        # res.append(first)
        # # maxset[first] -= 1
        # # if maxset[first] == 0:
        # #     del maxset[first]

        

        # for i in range(k, len(nums)):

        #     heapinsert(pq, nums[i])
        #     if nums[i] in maxset:
        #         maxset[nums[i]] += 1
        #     else:
        #         maxset[nums[i]] = 1
            
        #     former = nums[i-k]
            
        #     maxset[former] -= 1
        #     if maxset[former] == 0:
        #         del maxset[former]

        #     # print(former, maxset)
        #     first = heappop(pq, maxset)
        #     res.append(first)
        # return res
            
            

            
            
        