'''
解法就是,将新的节点link到原来节点的后面,
第一遍循环:创建新节点,link到原来节点的后面
第二遍循环:更新新节点的random
第三遍循环:将新节点和旧节点分离
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':


        t = head

        while t:
            tnode = Node(t.val)
            t_next = t.next
            t.next = tnode
            tnode.next = t_next
            t = t_next
        
        t = head

        while t:
            newnode = t.next
            if t.random:
                rannode = t.random.next
            else:
                rannode = None
            newnode.random = rannode
            t = t.next.next
        
        t = head

        prenode = None
        res = None

        while t :

            tnext = t.next.next
            nexnode = t.next
            t.next = tnext
            if prenode:
                prenode.next = nexnode
            else:
                res = nexnode
            prenode = nexnode
            t = tnext
        return res
                

            

        




        # linkMap = {}
        # linkArray = []
        # t = head
        # prev = None
        # i = 0
        # res = None
        # while  t:
        #     linkMap[t] = i
        #     tnode = Node(t.val)
        #     # tnode.val = t.val
        #     tnode.next = None
        #     tnode.random = None
        #     if prev:
        #         prev.next = tnode
        #     else:
        #         res = tnode
            
        #     prev = tnode
        #     linkArray.append(tnode)
        #     t = t.next
        #     i += 1
        # t = head
        # i = 0
        # while t:
            
        #     if t.random:
        #         idx = linkMap[t.random]
        #     else:
        #         idx = None
        #     # print(i, idx)
        #     curNode = linkArray[i]
        #     if idx != None:
        #         curNode.random = linkArray[idx]
        #     t = t.next
        #     i += 1
            
            
        return res
        