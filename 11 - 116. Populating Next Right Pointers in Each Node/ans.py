"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import queue
import math

class Solution:

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # bfs method
        """
        in here, I use the bfs method,
        first I need to have a queue, to bfs the whole tree
        then I need to record the former node and the node number 
        if the nodenumber indicate that this node is end:
        
        if math.log2(i+1).is_integer()
        the relationship between the node number and high is :

        Number = 2^h -1
        h = 1, number = 1
        h = 2, number = 3
        h = 3, number = 7 = 2^3 - 1
        .........


        then it's next will be None, prevhead = none
        else just set the prevhead = currenthead

        """
        q = queue.Queue()
        temp = root
        q.put(root)
        res = []
        res.append(root)
        i = 1
        prevhead = None
        while q.qsize() > 0:
            head = q.get()
          
            if head == None:
                return head
            left = head.left
            right = head.right

            if prevhead != None:
                prevhead.next = head

            if math.log2(i+1).is_integer():
                head.next = None
                prevhead = None
            else:
                prevhead = head
            
            i += 1
            
            if  left == None or  right == None:
                continue

            q.put(left)
            q.put(right)

        return root
            
        # return root
        