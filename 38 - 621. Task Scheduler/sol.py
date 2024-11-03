from typing import List

'''
很简单,只需要将它频率最高的task找出来,假设频率最高的task的频率为m
那么至少需要m组,但是最后一组可能填不满。
所以,(m-1) * n 是最开始的res的长度

其次，找到跟频率m一样的组，那么跟频率m一样的组那就是最后一组的个数
比如，频率为m的组有2个，那么最后一组就有两个
因此，res更新为 (m-1) * n + fre_counter

最后，将res和数组的size比较，返回较大的那个

'''



class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Frequency counting with a fixed array of size 26 (only uppercase letters A-Z)
        task_counts = [0] * 26
        for task in tasks:
            task_counts[ord(task) - ord('A')] += 1  # Calculate frequency by task letter

        # Step 2: Identify the maximum frequency and count of tasks with that maximum frequency
        max_freq = max(task_counts)
    
        # Step 3: Calculate the minimum required intervals
        # (max_freq - 1) * (n + 1): Accounts for the total blocks (rows of n+1 slots each) for max_freq - 1 occurrences
        # max_count: The last group of max_freq tasks may fit in the final row without needing additional idle time
        n = n + 1
        min_intervals = (max_freq - 1) * (n) 

        max_count = sum(1 for count in task_counts if count == max_freq)

        min_intervals += max_count

        # Step 4: Ensure that the result is at least the total number of tasks, to avoid overcounting idle times
        return max(min_intervals, len(tasks))

# from collections import defaultdict
# import heapq



