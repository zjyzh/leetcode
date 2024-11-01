

'''
最小生成树,使用并查集
如果当前两个节点没有通过并查集连接到一起
那就要将当前节点加入到链接集合里面
最后通过检查集合是否是全联通图来返回结果
'''



class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        fa = [ i for i in range(n) ]
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

        sorted_connection = sorted( connections, key = lambda x:x[2] )
        
        res = 0

        visited = set()

        for i in sorted_connection:
            s = i[0]
            e = i[1]
            val = i[2]
            if not find(s-1) == find(e-1):
                union(s-1, e-1)
                res += val
                visited.add(s-1)
                visited.add(e-1)

        if len(visited) == n:
            temp = find(0)
            isbreak = True
            for i in visited:
                if not temp == find(i):
                    isbreak = False
            if isbreak:
                return res   
        
        
        return -1


         