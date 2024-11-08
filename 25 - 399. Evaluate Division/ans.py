import queue

"""
we could use bfs or union find to solve this problem

basic structure of union find

fa = [ i for i in range(n)]

def find(i):
    if fa[i] == i:
        return i
    else:
        fa[i] = find(fa[i])
        return fa[i]

def union(i, j):
    root_i = find(i)
    root_j = find(j)
    fa[root_i] = fa[root_j]


"""

"""

underlying solution using bfs

"""




from typing import List, Dict
from collections import defaultdict

class Solution:
    def __init__(self):
        self.graph = defaultdict(dict)
    
    def add_edge(self, u: str, v: str, value: float):
        # Add edges in both directions with appropriate weights
        self.graph[u][v] = value
        self.graph[v][u] = 1 / value

    def dfs(self, start: str, end: str, visited: set) -> float:
        # If start node equals end, return 1.0 as the division of any variable by itself is 1
        if start == end:
            return 1.0
        visited.add(start)
        
        # Visit all neighbors of the start node
        for neighbor, value in self.graph[start].items():
            if neighbor in visited:
                continue
            result = self.dfs(neighbor, end, visited)
            if result != -1.0:  # valid path found
                return value * result
        
        return -1.0  # No valid path

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build graph
        for (u, v), value in zip(equations, values):
            self.add_edge(u, v, value)
        
        results = []
        for start, end in queries:
            if start not in self.graph or end not in self.graph:
                results.append(-1.0)  # If start or end node is not in the graph, return -1.0
            else:
                results.append(self.dfs(start, end, set()))  # Perform DFS with a fresh visited set
        
        return results




class Solution:

    def bfs(self, start, end):

        self.q.put((start, 1))
        while self.q.qsize() > 0:
            head,val = self.q.get()
            if head in self.visited and self.visited[head] == 0:
                self.visited[head] = 1
                
                for node, value in self.equ_tree[head]:
                    if node == end:
                        return val * value
                    if node == head:
                        continue
                    self.q.put((node, val*value))
                    # update node ,new_value as val * value as the path value
                
        return -1
            
    def ini_visit(self):
        for k in self.visited.keys():
            self.visited[k] =  0


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.equ_tree = {}
        self.visited = {}
        for i in range(len(equations)):
            edge = equations[i]
            left = edge[0]
            right = edge[1]
            lvalue = values[i]
            rvalue = 1/values[i]

            if not left in self.visited:
                self.visited[left] = 0
            
            if not right in self.visited:
                self.visited[right] = 0

            if left in self.equ_tree:
                self.equ_tree[left].add((right,lvalue))
            else:
                self.equ_tree[left] = set([(right,lvalue)])
            
            if right in self.equ_tree:
                self.equ_tree[right].add((left,rvalue))
            else:
                self.equ_tree[right] = set([(left,rvalue)])
     

        res = []
        self.q = queue.Queue()
        for i in queries:
            start = i[0]
            end = i[1]
            res.append(self.bfs(start, end))
            # the key is to ini every queue and visited array for every bfs operation
            self.ini_visit()
            self.q = queue.Queue()

        return res

        