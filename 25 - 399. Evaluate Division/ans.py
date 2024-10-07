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

        