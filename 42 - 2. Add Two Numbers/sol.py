'''
直接相加就行了,构建下个数组
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        t1 = l1
        t2 = l2

        cur_val = 0
        pre_val = 0

        res = ListNode()

        res_ptr = res

        i = 1
        while True:
            curres = 0
            if t1 :
                curres += t1.val
            #     print('t1', t1.val)
            # print('i', i)
            i+= 1
            if t2 :
                curres += t2.val
                # print('t2', t2.val)

            curres += pre_val
            # print( curres, pre_val)
            if curres >= 10:
                pre_val = curres // 10
                curres = curres % 10
            else:
                pre_val = 0
            # print( curres, pre_val)
            res_ptr.val = curres
            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next

            if not t1 and not t2 and pre_val == 0:
                res_ptr.next = None
                break

            if not res_ptr.next:
                res_ptr.next = ListNode()
            res_ptr = res_ptr.next
            

            
                

        return res
            

        