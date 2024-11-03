'''
依然思路很简单，将链表一分为二，然后把
第二个链表翻转
最后插入到第一个链表中

注意链表翻转的写法
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:


    def findmid(self, head):
        
        size = 0
        s = head
        while s:
            s = s.next
            size += 1
        
        mid = size // 2

        s = head
        for i in range(0,mid-1):
            s = s.next
        return s

    def reverse(self, node):

        prev = None
        cur = node

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            

        return prev
    def printnode(self, node):
        
        print('start')
        s = node
        while s:
            print(s.val)
            s = s.next
        print('end')

    def insert(self, node, nodenext):
        nnode = node.next
        node.next = nodenext
        nodenext.next = nnode

    def merge(self, l ,r ):

        while l:
            lnext = l.next
            rnext = r.next
            self.insert(l, r)
            if not lnext and rnext:
                self.insert(r, rnext)
                break
            l = lnext
            r = rnext
           


    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return
        midnode = self.findmid(head)
        nextlist = midnode.next
        midnode.next = None
        # print('nextlist')
        # self.printnode(nextlist)
        nextlist = self.reverse(nextlist)
        # print('head')
        # self.printnode(head)
        # print('nextlist')
        # self.printnode(nextlist)
        self.merge(head, nextlist)






        

        