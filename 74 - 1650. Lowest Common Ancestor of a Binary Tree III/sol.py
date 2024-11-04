
'''
这个题目有个非常奇妙的解法
两个指针同时向上移动
当一个指针移动到root时候，它切换到另一个指针的开头
对另一个指针同理。
最后他们会在同一个地方相遇，相遇的地方就是他们的共同祖先。
'''


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Initialize two pointers at p and q
        pointer1, pointer2 = p, q
        
        # Traverse upwards until they meet
        while pointer1 != pointer2:
            # Move each pointer one step up. If a pointer reaches None, switch it to the other node's start
            pointer1 = pointer1.parent if pointer1 else q
            pointer2 = pointer2.parent if pointer2 else p
        
        # When they meet, that's the lowest common ancestor
        return pointer1



# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.parent = None
# """

# class Solution:
#     def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
#         ppath = set()
#         qpath = set()
#         while p or q:
            
#             ppath.add(p)
#             qpath.add(q)

#             inter = ppath & qpath
            
#             if inter:
#                 for i in inter:
#                     return i

#             if p:
#                 p = p.parent
#             if q:
#                 q = q.parent
#         return None
