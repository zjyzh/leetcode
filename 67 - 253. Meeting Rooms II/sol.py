'''
按开始时间排序
用优先队列来存储结束时间
每次弹出最小结束时间
如果有冲突，那么将新的结束时间加进去
如果没有冲突，也要更新队列的第一个值，更新为min(cur_val, new_val)
然后继续循环
'''


import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals = sorted(intervals, key = lambda x:x[0])
        curstart = intervals[0][0]
        curend = intervals[0][1]
        pq = []
        heapq.heappush(pq, curend)
        res = 1
        for i in range(1, len(intervals)):
            cur = intervals[i]
            curend = pq[0]
            if curend > cur[0]:
                heapq.heappush(pq,cur[1])
                res += 1
                # curstart = min(curstart, cur[0])
            else:
                curend = max(curend, cur[1])
                heapq.heappop(pq)
                heapq.heappush(pq,curend)
        return res
        