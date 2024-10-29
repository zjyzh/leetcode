import heapq
from collections import defaultdict

'''
思路不难，维护一个最大堆，每次从堆里面取出两个频率最大的字母，然后加到数列的末尾
同时更新最大堆。

注意python里面最大堆的写法以及正负号的取值

'''


def update_dict_and_heap(mydict, heap, key, new_value):
    mydict[key] = new_value
    heapq.heappush(heap, (-new_value, key))

def get_max_from_heap(heap, mydict):
    while heap:
        v, k = heapq.heappop(heap)
        if mydict[k] == -v:
            return(k,-v)
    return (-1, -1)


class Solution:
    def reorganizeString(self, s: str) -> str:
        
        mydict = {}
        maxheap = []
        for i in s:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1
        
        for k in mydict.keys():
            v = mydict[k]
            heapq.heappush(maxheap, ( -v, k ))

        res = ''

        # print(maxheap)
        max_key, max_value = get_max_from_heap(maxheap, mydict)
        if (max_value - 1) > (len(s) - max_value):
            return ''
        update_dict_and_heap(mydict, maxheap, max_key, max_value)
        # print(maxheap)
        while len(res) < len(s):
            k1, v1 = get_max_from_heap(maxheap, mydict)
            k2, v2 =  get_max_from_heap(maxheap, mydict)
            # print(k1, v1)
            # print(k2, v2)
            if v1 > 0:
                res += k1
            if v2 > 0:
                res += k2
            update_dict_and_heap(mydict, maxheap, k1, v1-1)
            update_dict_and_heap(mydict, maxheap, k2, v2-1)
        return res

        
        