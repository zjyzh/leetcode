'''
bfs 经典题目,需要注意一些细节
'''


from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def get_next_states(current):
            # Generate all possible states from the current state by turning each wheel by one step
            states = []
            for i in range(4):
                digit = int(current[i])
                for move in [-1, 1]:  # Move the digit down or up
                    new_digit = (digit + move) % 10
                    states.append(current[:i] + str(new_digit) + current[i+1:])
            return states
        
        dead_set = set(deadends)
        if '0000' in dead_set:
            return -1  # Starting point is a dead end
        
        visited = set(['0000'])
        queue = deque([('0000', 0)])  # (current state, number of moves)
        
        while queue:
            current, turns = queue.popleft()
            
            if current == target:
                return turns
            
            for next_state in get_next_states(current):
                if next_state not in visited and next_state not in dead_set:
                    visited.add(next_state)
                    queue.append((next_state, turns + 1))
        
        return -1  # If the queue is exhausted, the target is unreachable


# import queue


# class Solution:
#     def openLock(self, deadends: List[str], target: str) -> int:

#         def getnext(current):

#             res = []
#             for i in range(len(current)):
#                 dig = int(current[i])
#                 front = (dig -1) % 10
#                 nxt = (dig + 1) % 10
    
#                 res.append(current[0:i] + str(front) + current[i+1:])                
#                 res.append(current[0:i] + str(nxt) + current[i+1:])
                
#             return res
        
#         deadhash = set()
#         for i in deadends:
#             deadhash.add(i)
        
#         visited = set()
#         pq = queue.Queue()

#         pq.put('0000')
#         pq.put(1)

#         result = 1
#         while True:
#             temppq = queue.Queue()
#             while pq.qsize() > 0:
#                 cur = pq.get()
#                 if cur in deadhash:
#                     continue
#                 if cur == target:
#                     return 0
#                 if cur == 1:
#                     result += 1
#                     continue
#                 nextset = getnext(cur)
                
#                 # print(cur, nextset, result)
#                 for j in nextset:
#                     if not j in visited and not j in deadhash:
#                         visited.add(j)
#                         temppq.put(j)
#                         if j == target:
#                             return result
#                 # pq.put(1)
#             pq = temppq
#             if pq.qsize() == 0:
#                 break
#             pq.put(1)
            
        
#         return -1

        
            


        