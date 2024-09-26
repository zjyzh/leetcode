# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):


    # remember just how to reverse single
    def reverseSingle(self, head):

        prev = None
        curr = head
        tail = head
        # need to remember the order of how to reverse the node 
        # 1. record the next node
        # 2. change the curr.next to prev
        # 3. change the prev to current
        # 4. change the current = curr.next
        while curr:
            # next_node = curr.next
            # curr.next = prev
            # prev = curr
            # curr = next_node
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
            # if not curr:
            #     tail = 
        # self.output(prev)
        return (prev,tail)

    def output(self, node):
        t = node
        while t:
            print( t.val)  # Correct syntax for Python 3
            t = t.next
        print()  # To print a new line after the loop
            

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        t = k
        temp = head
        size = 0
        while temp:
            size += 1
            temp = temp.next
        
        if size < k :
            return self.reverse(head)
        
        times = size // k
        
        res = head

        prevhead = None
        temp = head
        curhead = head

        # self.output(head)

        for i in range(times):
            t = k - 1

            while t > 0:
                temp = temp.next
                t -= 1
            
            # if not temp:
            nexthead = temp.next
            temp.next = None
            (newhead, newtail) = self.reverseSingle(curhead)
            # self.output(newhead)
            
            if prevhead:
                prevhead.next = newhead
            if i == 0:
                res = newhead
            
            prevhead = newtail
            temp = nexthead
            curhead = nexthead
        prevhead.next = curhead



        return res
            


            

        
        
        