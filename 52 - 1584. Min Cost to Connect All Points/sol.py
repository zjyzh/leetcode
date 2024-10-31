import heapq
from typing import List

'''
Prim’s Algorithm: 最小生成树

'''



class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)  # Number of points
        
        # Edge case: If there's only one point, no cost is needed to connect it
        if n == 1:
            return 0

        # Min-heap to store (cost, point) tuples where 'cost' is the distance to connect the point
        # Initialize with the first point (0 cost to connect itself)
        min_heap = [(0, 0)]  # (cost, point_index)
        
        total_cost = 0        # To store the total minimum cost to connect all points
        visited = set()       # Set to keep track of points already included in the MST
        edges_used = 0        # Counter for the number of edges used in the MST

        # While we haven't connected all points
        while edges_used < n:
            # Get the edge with the minimum cost to expand the MST
            cost, u = heapq.heappop(min_heap)
            
            # If this point is already in the MST, skip it
            if u in visited:
                continue
            
            # Add the cost of this edge to the total cost
            total_cost += cost
            # Mark this point as visited (added to the MST)
            visited.add(u)
            edges_used += 1

            # Explore the edges to all other unvisited points
            for v in range(n):
                if v not in visited:
                    # Calculate Manhattan distance between points[u] and points[v]
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    # Push this edge to the heap
                    heapq.heappush(min_heap, (dist, v))

        # After connecting all points, return the total minimum cost
        return total_cost


# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
#         fa = [i for i in range(len(points) +1)]
#         def find(i):
#             if fa[i] == i:
#                 return i
#             else:
#                 fa[i] = find(fa[i])
#                 return fa[i]
        
#         def union(i, j):
#             root_i = find(i)
#             root_j = find(j)
#             fa[root_i] = root_j
        
#         def dis(pi, pj):
#             return abs(pi[0]-pj[0]) + abs(pi[1] - pj[1])
        

#         def allconnect(n):
#             root = 1
#             for i in range(n):
#                 if find(i) != root:
#                     return False
#             return True


#         edges = []
#         graph = {}
#         for i in range(len(points)):
#             for j in range(i+1,len(points)):
#                 if i == j:
#                     continue
                
#                 edge = [i, j, dis(points[i], points[j])]
#                 edges.append(edge)
#                 if not i in graph:
#                     graph[i] = []
#                 graph[i].append([j, dis(points[i], points[j])])
        
#         edges = sorted(edges, key = lambda x:x[2])
        
#         nodeset = set()
#         res = 0
#         for i in edges:
#             start = i[0]
#             end = i[1]
#             dis = i[2]
#             # print('edge,',i)

#             if not find(start) == find(end):
#                 union(start, end)
#                 nodeset.add(start)
#                 nodeset.add(end)
#                 res += dis
#                 # print('nodeset',nodeset)
#                 # print('ers', res)
            
#             if len(nodeset) == len(points) and allconnect(len(points)):
#                 return res
#         return res
                


            