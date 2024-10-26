from collections import defaultdict
import heapq



'''
很简单，只需要将它频率最高的task找出来，假设频率最高的task的频率为m
那么至少需要m组，但是最后一组可能填不满。
所以，(m-1) * n 是最开始的res的长度
然后检查最后一组，看看是否满人。
最后，如果所有的m组都满了，但是还剩下task，就需要把剩下的task加上去。
'''


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskset = defaultdict(int)
        heap = []
        for i in tasks:
           taskset[i] += 1
        n = n + 1
        resset = []
        for i in taskset.keys():
            valu = taskset[i]
            resset.append([i,valu])
            # update_dict_and_heap(taskset,heap, i, valu)
        resset = sorted(resset, key = lambda x:x[1], reverse = True)
        res = 0
        
        num = resset[0][1]
        res += (num -1) * n 
        
        for j in resset: # 检查最后一组的数量
            j[1] -= (num -1)
            if j[1] > 0:
                res += j[1]
        
        remain = len(tasks) - res # 检查剩余的数量
        if remain > 0:
            res += remain
        return res
            
        