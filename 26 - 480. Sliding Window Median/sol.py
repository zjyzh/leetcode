import heapq
from collections import defaultdict


'''
in this method, we use double prio queue
left que is the max heap to keep the left side
right que is the min heap to keep the min side
then we need to update the size of left and right
based on the delete element.

since delete the heap is time-consuming, we
need to use a dict to store the delete element
then we need to delete it when we want to create
a balance between left and right

'''


'''
the python method of maxheap
'''
def maxheappush(pq, k):
    heapq.heappush(pq, -k)

def maxheappop(pq):
    res = heapq.heappop(pq)
    return - res

def maxheapget(pq):
    if len(pq) > 0:
        return - pq[0]
    else:
        return None

class Solution:

    '''
    right num is always larger or equal than left num
    '''
    def getMid(self, k):
        if k % 2 == 1:
            return self.pq_right[0]
        else:
            r = self.pq_right[0]
            l = maxheapget(self.pq_left)
            return (l + r) / 2

    def remove(self, num):

        # removedict means that we need to remove the 
        # content in the future
        self.removedict[num] += 1

        if len(self.pq_left) > 0 and num <= maxheapget(self.pq_left):
            self.leftnum -= 1
            if maxheapget(self.pq_left) == num:
                self.popleft()
        else:
            self.rightnum -= 1
            if self.pq_right[0] == num:
                self.popright()
        
        self.balance()
         
        
    def insert(self, num):
       
        # for insert, we need to update the lefrnum and rightnum
        if len(self.pq_left) > 0 and num <= maxheapget(self.pq_left):
            self.leftnum += 1
            maxheappush(self.pq_left, num)
            
        else:
            self.rightnum += 1
            heapq.heappush(self.pq_right, num)

        self.balance()


    def popleft(self):
        while len(self.pq_left) > 0 and  self.removedict[maxheapget(self.pq_left)] > 0:
            l = maxheappop(self.pq_left)
            self.removedict[l] -= 1

    def popright(self):
        while len(self.pq_right) > 0 and self.removedict[self.pq_right[0]] > 0:
            r = heapq.heappop(self.pq_right)
            self.removedict[r] -= 1


    def balance(self):

        '''
        in the balance function
        what we need to do is to keep the 
        left and right num balance
        if they have greate diff
        we need to update then
        noticed that we also need to delete the one 
        with the useless dict
        '''
        self.popleft()
        self.popright()
        
        while self.rightnum - self.leftnum > 1:
            r = heapq.heappop( self.pq_right)
            maxheappush(self.pq_left, r)
            
            self.rightnum -= 1
            self.leftnum += 1
            self.popright()
        
        while self.rightnum - self.leftnum < 0:
            l = maxheappop( self.pq_left)
            heapq.heappush(self.pq_right, l)
            self.rightnum += 1
            self.leftnum -= 1
            self.popleft()

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        self.klist = [ nums[i] for i in range(k)]
        self.klist = sorted(self.klist)
        res = []
        right = k //2
        left = right - 1
        self.pq_left = []
        self.pq_right = []
        for i in self.klist[right:]:
            heapq.heappush(self.pq_right,i)

        for i in self.klist[0:left+1]:
            maxheappush(self.pq_left,i)
        
        self.leftnum = len(self.pq_left)
        self.rightnum = len(self.pq_right)

        self.removedict = defaultdict(int)
        
        res.append(self.getMid(k))
        if k == 1:
            return nums
        
        for i in range(len(nums) - k):
            start = i
            end = start + k
            self.remove(nums[start])
            self.insert(nums[end])
            res.append(self.getMid(k))
        return res

            

        