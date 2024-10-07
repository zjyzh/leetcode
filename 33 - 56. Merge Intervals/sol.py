class Solution:

    '''
    只需要对开始时间排序，然后维护两个变量
    start 和 end 记录当前的区间，如果当前区间
    跟后区间有交集，那么就扩展当前区间
    如果没有交集，将当前区间放入result，然后
    更新当前区间
    '''

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_interval = sorted(intervals, key = lambda x:x[0])
        res  = []
        # i = len(intervals)-1

        start = sorted_interval[0][0]
        end = sorted_interval[0][1]

        for i in range(1, len(sorted_interval)):
            cur = sorted_interval[i]
            cur_start = cur[0]
            cur_end = cur[1]
            if cur_start <= end:
                if cur_end > end:
                    end = cur_end
            else:
                res.append([start,end])
                start = cur_start
                end = cur_end
        
        res.append([start,end])

        return res
                

        