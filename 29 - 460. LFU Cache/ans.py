"""
需要设计两个哈希表，一个k-node键值对，用来快速找到键值对
一个是frequency-linklist，用来快速确定某个frequency
对应的缓存

对于get操作，如果key在哈希表里面，那么我们需要更新
key的访问次数，同时需要将frequency - linklist中弹出
放入：（frequency+1） - linklist中
这个时候，如果frequency对应的linklist为空，那么需要删除
该frequency，并将min_frequency数字加一

如果key不在哈希表里面，直接返回

对于put操作，如果key在哈希表里面，我们需要更新key的值，
并更新访问次数。同事需要

做频率更新
···
需要将frequency - linklist中弹出
放入：（frequency+1） - linklist的链表头部
这个时候，如果frequency对应的linklist为空，那么需要删除
该frequency，并将min_frequency数字加一
···

如果key不在哈希表中，我们需要查看缓存的size

 1. 如果缓存size还有空余，那么我们直接将节点放入哈希表，
    同时更新frequency-list哈希表，注意新放入的元素
    一定在哈希表的表头，因为表头代表时间，表末尾代表
    访问时间最长（也就是最久没有访问的元素）会被优先淘汰
    对于新放入的元素，缓存设置为1，同时更新min_fre = 1
 2. 如果缓存size没有空余，那么从frequency为min_fre的
    缓存链表中，弹出末尾的元素，然后重复上面操作。


"""



class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.frequency = 0
        self.next = None
        self.prev = None

class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addfront(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            original_head = self.head
            self.head = node
            self.head.next = original_head
            original_head.prev = self.head
            self.head.prev = None

    # def pophead(self):
        
    
    def delete(self, node):

        
        pre = node.prev
        nex = node.next
        # print("dele", node.key, node.val, node.frequency)

        if node == self.tail and node == self.head:
            self.head = None
            self.tail = None
            return
        
        if node == self.tail:
            t = self.tail.prev
            self.tail = t
            if t != None:
                t.next = None
            node.prev = None
            return
        
        if node == self.head:
            t = self.head.next
            
            self.head = t
            if t != None:
                t.prev = None
            node.next = None
            return

        if pre == None and nex == None:
            self.head = None
            self.tail = None
            # print('none')
            return

        if not pre == None:
            pre.next = nex
            # print("pre", pre.key, pre.val)

        if not nex == None:
            nex.prev = pre
            
            # print("nex", nex.key, nex.val)
    
    def poptail(self):
        # print('poptail')
        # t = self.tail.prev
        res = self.tail
        self.delete(res)
        return res
        
        



class LFUCache:

    def __init__(self, capacity: int):
        self.kvhash = {}
        self.frequency_hash = {}
        self.cap = 0
        self.maxcap = capacity
        self.minFre = 1

    
    def changeFre(self,ele):
        '''
        在这个函数里面，我们进行了两个操作
        1. 我们需要将旧元素从缓存链表中弹出
        2. 我们需要将旧元素的访问频率更新，然后将它插入
            相邻的缓存链表，这里表示为frequency+1
        '''
        linklist = self.frequency_hash[ele.frequency]
        original_fre = ele.frequency
        ele.frequency += 1
        linklist.delete(ele)
        if linklist.head == None and linklist.tail == None:
            del self.frequency_hash[original_fre]
        if ele.frequency not in self.frequency_hash:
            self.frequency_hash[ele.frequency] = DoubleList()
        newlist = self.frequency_hash[ele.frequency]
        newlist.addfront(ele)
        


    def get(self, key: int) -> int:
        
        '''
        在get函数中，我们需要改变哈希表，同时更新缓存链表
        '''
        if key in self.kvhash and self.kvhash[key]:
            ele = self.kvhash[key]
            # print('get', ele.key, ele.val)
            self.changeFre(ele)
            if not self.minFre in self.frequency_hash:
                self.minFre += 1
            return self.kvhash[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # print('put', key)
        '''
        在put操作中，我们需要维护缓存size的大小
        如果put时候更新元素，那么同样需要改变缓存
        '''
        if key in self.kvhash:
            ele = self.kvhash[key]
            ele.val = value
            self.changeFre(ele)
            
            if not self.minFre in self.frequency_hash:
                self.minFre += 1
        else:
            '''
            如果put的时候插入元素，那么我们需要
            看缓存的size，如果缓存的size过大，弹出
            最小缓存对应的缓存链表的末尾，同时更新
            缓存链表，设置最小缓存为1
            '''
            self.cap += 1
            ele = Node(key, value)
            
            ele.frequency = 1

            if self.cap > self.maxcap:
                
                n = self.frequency_hash[self.minFre].poptail()
                if n != None:
                    del self.kvhash[n.key]
                self.cap -= 1
                
                
            if not 1 in self.frequency_hash:
                # print('not 1', self.frequency_hash)
                self.frequency_hash[1] = DoubleList()
                # self.frequency_hash[1].addfront(ele)
            self.frequency_hash[1].addfront(ele)
            self.kvhash[key] = ele
            # print('put', self.kvhash[key].key, self.kvhash[key].val)
            self.minFre = 1

                

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)