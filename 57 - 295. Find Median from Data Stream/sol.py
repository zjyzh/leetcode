import heapq

'''

非常优雅的解法
首先将来的元素全部放进最小堆里面
然后把最小堆里面的元素放进最大堆里面
如果最小堆的元素比最大堆要少，那么就把元素从最大堆移动到最小堆
始终保持最小堆的元素大于等于最大堆

取值时候，如果两个堆元素不相等，就把最小堆的元素给他
要不然就取两个堆的平均值
'''


class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        
    def addNum(self, num: int) -> None:

        heapq.heappush(self.minheap,num)
        minval = heapq.heappop(self.minheap)
        heapq.heappush(self.maxheap, -minval)
        if len(self.minheap) < len(self.maxheap):
            minval = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, - minval)

        
    def findMedian(self) -> float:

        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return (self.minheap[0] + (-self.maxheap[0])) /2
        