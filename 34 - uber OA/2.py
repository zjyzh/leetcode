"""

给一个list query, 和一个int diff。query中有两种元素
“+x” 往当前nums中添加一个int x
“-x“ 去掉nums中所有数字 x
定义 一个triple (x,y,z), y-x=z-y=diff
输出每个query过后nums中元素可以组成的triple个数,相同的数字可以多次使用(比如nums=[1,2,3,1] diff=1 输出就是2)
query = ['+1', '+2', '+3', '+1', '-1'] diff=1
output=[ 0, 0, 1, 2, 0]


"""





class Solution:

  def distance(self, x, y):
    return min(abs(x[0] - y[0]), abs(x[1] - y[1]))

  
  def minCostToConnectServers(self, x: List[int], y: List[int]) -> int:
    n = len(x)
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

    edges = []

    for i in range(n-1):
      for j in range(i+1, n ):
        l = [ x[i], y[i] ]
        r = [ x[j], y[j] ]
        dis = self.distance(l,r)
        
        edges.append( [i, j, dis])

    edges = sorted( edges, key = lambda x : x[2] )
    # print(edges)

    res = 0
    for edge in (edges):
      start = edge[0]
      end  = edge[1]
      dis = edge[2]
      if find(start) != find(end):
        union(start, end)
        res += dis

    return res
        
        
    





