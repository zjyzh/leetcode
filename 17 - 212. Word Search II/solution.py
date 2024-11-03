
'''
this is a dfs + Tire tree type of problem
first I need to use Tire Tree to arrange all of 
the node, then use the dfs to go through the 
tire tree every time
'''

class Tire:
    def __init__(self):
        self.word = None
        self.isFinal = False
        self.next = [ None for i in range(27)]
    
    def changeFinal(self, isFinal, word):
        if isFinal:
            self.isFinal = True
            self.word = word


direction = [-1, 0 , 1, 0, -1]

class Solution:
    def dfs(self, x, y, node):
        
        if node == None:
            return
        
        '''

        we can't do this judgement after the x and y biger and limit
        since it's possible that we reach the final out of the
        x,y limit, so we first do the isFinal judgement 
        then do the x,y limitation

        '''
        if node.isFinal:
            self.res.append(node.word)
            node.isFinal = False

        if x < 0 or x >= self.m:
            return False
        
        if y < 0 or y >= self.n:
            return False

        if self.board[x][y] == '#':
            return

        '''
        here, we only go to next node after we found that it's
        valid on the Tire tree

        '''
        char = self.board[x][y]
        idx = ord(char) - ord('a')
        nextNode = node.next[idx]
        

        if nextNode == None:
            return
        
        # key point of dfs, set the dummy node
        self.board[x][y] = '#'
     
        # go through the next child, then do the dfs
        for t in range(4):
            nextx = x + direction[t]
            nexty = y + direction[t+1]
            self.dfs(nextx, nexty, nextNode)

        # key point of dfs, recover the dummy node      
        self.board[x][y] = char
              


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        self.res = []

        root = Tire()
        temp = root

        # in this, we ini the Tire Tree, 
        # iterate every word to create the Tire Tree
        for w in words:
            for j in range(len(w)):
                i = w[j]
                num = ord(i) - ord('a')
                if temp.next[num] == None:
                    temp.next[num] = Tire()
                temp = temp.next[num]
        
            temp.changeFinal(True, w)
            temp = root

        # For every start point, we use the dfs to do the search
        for i in range(self.m):
            for j in range(self.n):
                self.dfs(i, j, root)
            
        return self.res
        







'''
依然是dfs + tire的解法，但是加入了剪枝算法
如果一个word已经被找到，就把它设置为False
如果已经word已经没有任何next节点，那么直接把这个当前的字符删掉。
这样能够提前结束很多的情况
'''


class Tire:

    def __init__(self):
        self.head = Node()

    def add(self, word):

        curnode = self.head
        for s in word:
            if not s in curnode.next:
                curnode.next[s] = Node()
            curnode = curnode.next[s]
        
        curnode.isfinish = True
        curnode.w = word
            


class Node:
    def __init__(self, char = ''):
        self.isfinish = False
        self.next = {}
        self.w = ''
            

directions = [-1, 0, 1, 0, -1]
'''
a b
a a
'''
class Solution:



    def dfs(self, board, i, j, cur_node):

        if cur_node.isfinish:
            # 避免重复添加word
            cur_node.isfinish = False
            self.res.add(cur_node.w)

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == '':
            return

        if board[i][j] in cur_node.next:
            c = board[i][j]
            nxd = cur_node.next[c]
            board[i][j] = ''

            for k in range(4):
                next_i = i + directions[k]
                next_j = j + directions[k + 1]
                self.dfs(board, next_i, next_j, cur_node.next[c])
            board[i][j] = c
            # 注意剪枝，能提升很多空间利用率
            if not nxd.next:
                del cur_node.next[c]
        return



    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        tire = Tire()
        for w in words:
            tire.add(w)
        self.res = set()
        # self.visited = [  ]
        for i in range(len(board)):
            for j in range(len(board[0])):
                # print('start')
                self.dfs(board, i, j, tire.head)
                # print('end')

        return list(self.res)
        


        

        
                    







        