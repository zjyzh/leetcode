'''
关键在init linklist的步骤
需要在初始化的时候初始化两个占位符
head和tail都是占位符，head和tail指针都不会指向真正的节点
因此，头节点是head.next
末尾节点是tail.prev
通过这样的设计，能够大大提升节点增加删除时候的便利性
不需要移动头尾指针
'''

# Usage:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)




class LinkList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    
    def append(self, node):

        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        
    
    def pophead(self):

        n = self.head.next
        self.head.next = n.next
        n.next.prev = self.head
        return n


    def print(self):
        cur = self.head
        while cur:
            print(cur.key, cur.val)
            cur = cur.next
        return

            

    def delete(self, target):

        prev = target.prev
        nxt = target.next
        prev.next = nxt
        nxt.prev = prev

    




class Node:

    def __init__(self):
        self.val = 0
        self.next = None
        self.prev = None
        self.key = 0




class LRUCache:

    def __init__(self, capacity: int):
        self.max_cap = capacity
        self.hash = {}
        self.linklist = LinkList()
        self.cur_cap = 0
        

    def get(self, key: int) -> int:

        if key in self.hash:

            node = self.hash[key]
            self.linklist.delete(node)
            self.linklist.append(node)
            return node.val

        else:
            return -1


        

    def put(self, key: int, value: int) -> None:
        # print(key, value)
        # self.linklist.print()
        if key in self.hash:
            n = self.hash[key]
            n.val = value
            
            self.linklist.delete(n)
            self.linklist.append(n)

            # self.linklist.print()
        else:
            self.hash[key] = Node()
            self.hash[key].val = value
            self.hash[key].key = key
            if self.cur_cap == self.max_cap:
                node = self.linklist.pophead()
                self.linklist.append(self.hash[key])
                del self.hash[node.key]
            else:
                self.linklist.append(self.hash[key])
                self.cur_cap += 1
            # self.linklist.print()
        


        


# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)