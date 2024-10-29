'''
djskstra 算法，依然是用优先队列
这个是AI优化过的写法，基本框架依然是优先队列

'''


import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Step 1: Build the graph using defaultdict with lists for adjacency list
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Step 2: Initialize distances to infinity, and use a min-heap for Dijkstra's algorithm
        distance = [float('inf')] * (n + 1)
        distance[k] = 0  # Distance to the starting node is 0

        # Min-heap (priority queue) to store (current_distance, node)
        min_heap = [(0, k)]  # Start from the source node k with 0 distance

        # Step 3: Dijkstra's algorithm
        while min_heap:
            curr_dist, node = heapq.heappop(min_heap)

            # Skip if we've already found a better path to this node
            if curr_dist > distance[node]:
                continue

            # Relax edges
            for neighbor, weight in graph[node]:
                new_dist = curr_dist + weight
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(min_heap, (new_dist, neighbor))

        # Step 4: Find the maximum distance from the start node to any other node
        max_dist = max(distance[1:])  # Ignore the 0th index

        # If any node is unreachable, return -1
        return max_dist if max_dist < float('inf') else -1

