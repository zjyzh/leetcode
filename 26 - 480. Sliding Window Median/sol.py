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


import heapq
from collections import defaultdict
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # Max-heap for the left side (invert values to use Python's min-heap as max-heap)
        left_heap = []
        # Min-heap for the right side
        right_heap = []
        # Dictionary to keep track of elements marked for deletion
        delayed_removals = defaultdict(int)
        
        # Helper function to balance the heaps
        def balance_heaps():
            # Ensure left_heap has at most the same number of elements as right_heap
            while len(left_heap) > len(right_heap):
                heapq.heappush(right_heap, -heapq.heappop(left_heap))
            while len(right_heap) > len(left_heap) + 1:
                heapq.heappush(left_heap, -heapq.heappop(right_heap))
            
            # Remove elements marked for deletion from the top of each heap
            while left_heap and delayed_removals[-left_heap[0]] > 0:
                delayed_removals[-heapq.heappop(left_heap)] -= 1
            while right_heap and delayed_removals[right_heap[0]] > 0:
                delayed_removals[heapq.heappop(right_heap)] -= 1

        # Helper function to get the current median
        def get_median():
            if k % 2 == 1:
                # If k is odd, the median is the root of right_heap
                return float(right_heap[0])
            else:
                # If k is even, the median is the average of the roots of both heaps
                return (right_heap[0] - left_heap[0]) / 2.0

        # Initialize the heaps with the first 'k' elements
        for i in range(k):
            if not right_heap or nums[i] >= right_heap[0]:
                heapq.heappush(right_heap, nums[i])
            else:
                heapq.heappush(left_heap, -nums[i])
            balance_heaps()

        # Store the first median
        result = [get_median()]

        # Process the rest of the elements
        for i in range(k, len(nums)):
            # Outgoing element (leaves the sliding window)
            outgoing = nums[i - k]
            # Incoming element (enters the sliding window)
            incoming = nums[i]
            
            # Mark the outgoing element for deletion
            delayed_removals[outgoing] += 1
            
            # Remove the outgoing element from its respective heap
            if outgoing >= right_heap[0]:
                right_heap_size = len(right_heap)
                if right_heap_size > 0 and outgoing == right_heap[0]:
                    heapq.heappop(right_heap)
                else:
                    delayed_removals[outgoing] += 1
                balance_heaps()
            else:
                left_heap



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

            

        