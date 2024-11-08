import heapq
from typing import List

'''
Dijkstra 算法,用优先队列详解
'''



class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Create the adjacency list to store edges and probabilities
        graph = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        # Initialize the max-heap with the starting node (negative probability for max heap)
        max_heap = [(-1.0, start_node)]  # Store (-probability, node)
        distance = [0.0] * n  # Stores the maximum probability to reach each node
        distance[start_node] = 1.0  # Start with probability 1.0 at the starting node
        
        '''
        在这里,用优先队列来代替unvisited的边,一开始,unvisited只需要一个,因为
        我们是从起点开始
        然后,弹出概率最大的节点,该节点肯定unvisited。
        其次,遍历该节点的边,找出跟当前节点相连接的所有节点
        如果通过当前节点以及distance数组连接的节点比distance数组大
        那么就需要更新数组,同时将节点放入max_heap中
        只要更新max_heap,那么当前节点肯定没有被访问
        '''
        # Perform Dijkstra's algorithm
        while max_heap:
            curr_prob, node = heapq.heappop(max_heap)
            curr_prob = -curr_prob  # Convert back to positive
            
            # If we reach the end node, return the probability
            if node == end_node:
                return curr_prob
            
            # Explore the neighbors
            for neighbor, edge_prob in graph[node]:
                new_prob = curr_prob * edge_prob
                if new_prob > distance[neighbor]:
                    distance[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
        
        # If the end node is not reachable, return 0.0
        return 0.0
