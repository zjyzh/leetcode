


'''
基于模式的邻接表：

为了找出相邻的单词（即只差一个字母的单词），我们可以将单词变换为通用模式。例如，对于单词 "hot"，我们可以生成三个模式："*ot"、"h*t" 和 "ho*".
我们遍历 wordList 中的每个单词，将每个单词的每一个位置依次替换为 *，生成相应的模式。然后将这些模式存储在一个字典 all_combo_dict 中，模式作为键，匹配该模式的单词列表作为值。
这样做的好处是，我们可以通过模式快速找到“相邻”的单词。例如，对于 "hot" 和 "dot"，它们共享模式 "*ot"，因此是相邻的。
示例：

python
Copy code
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
all_combo_dict = {
    "*ot": ["hot", "dot", "lot"],
    "h*t": ["hot"],
    "ho*": ["hot"],
    "d*t": ["dot"],
    "*og": ["dog", "log", "cog"],
    "d*g": ["dog"],
    "l*t": ["lot"],
    "lo*": ["lot", "log"],
    "c*g": ["cog"],
    "co*": ["cog"]
}
广度优先搜索 (BFS)：

初始化一个队列 queue，将起始单词 beginWord 和初始层级（层级为 1，表示路径长度）放入队列中。同时，用 visited 集合来记录已经访问过的单词，防止重复访问。
每次从队列中取出一个单词 current_word，对于该单词生成所有可能的模式，然后通过这些模式找到所有的邻居单词。
如果某个邻居单词就是 endWord，那么我们找到了最短路径，直接返回当前层级加 1。
如果邻居单词不是 endWord，并且该单词还没有被访问过，就将其加入 queue 并标记为已访问。
为了避免重复检查，我们在访问过一个模式后，就将其清空，防止后续再次访问相同模式的单词。

'''

from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0
        
        adj_graph = defaultdict(list)
        n = len(beginWord)

        for w in wordList:
            for i in range(len(w)):
                pattern = w[0:i] + "*" + w[i+1:]
                adj_graph[pattern].append(w)

        q = deque()
        q.append([1, beginWord])
        visited = set()

        while len(q) > 0:

            top = q.popleft()
            level = top[0]
            word = top[1]
            if word in visited:
                continue
            visited.add(word)

            if word == endWord:
                return level


            for i in range(len(word)):
                pattern = word[0:i] + "*" + word[i+1:]

                if pattern in adj_graph:
                    for w in adj_graph[pattern]:
                        if w not in visited:
                            q.append([level +1, w])
        return 0

       




# from collections import deque


# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

#         def isneibour(l,r):
#             dif = 0
#             for i in range(len(l)):
#                 if not l[i] == r[i]:
#                     dif += 1
#             return dif == 1
#         n = len(wordList)
#         graph = [[0 for j in range(n+1)] for i in range(n + 1)]
#         for i in range(n):
            
#             for j in range(n):
#                 if not i == j:
#                     if isneibour(wordList[i], wordList[j]):
#                         graph[i][j] = 1
#                         graph[j][i] = 1

#         begin_idx = n
#         if not beginWord in wordList:
#             for i in range(n):
#                 if isneibour(beginWord, wordList[i]):
#                     graph[i][n] = 1
#                     graph[n][i] = 1
#         else:
#             begin_idx = wordList.index(beginWord)
        
#         que = deque()
#         visited = set()
#         # visited.add(begin_idx)
#         self.res = 0
#         que.append([begin_idx, 0])

#         def bfs( end, graph, visited, q):
            
#             cur = q.popleft()
#             curnode = cur[0]
#             curlevel = cur[1]
#             # print(cur)
#             if curnode != begin_idx and end == wordList[curnode]:
#                 self.res = curlevel 
#                 return 
            
#             visited.add(curnode)
#             for i in range(len(graph)):
#                 if curnode != i and graph[curnode][i] == 1 and i not in visited:
#                     q.append((i, curlevel + 1))
            
#             if len(q) > 0:
#                 bfs(end, graph, visited, q)
#             return 

#         bfs(endWord, graph, visited, que)
#         if self.res == 0:
#             return 0
#         return self.res + 1
            
            







        
                    
        
        