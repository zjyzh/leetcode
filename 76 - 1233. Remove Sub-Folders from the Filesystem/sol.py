from typing import List
"""
这个只需要排序，然后判断后面加入的跟前面的第一个前缀是否一样就行了
"""



class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Step 1: Sort folders lexicographically
        folder.sort()
        
        # Step 2: Initialize result list and add the first folder
        result = [folder[0]]
        
        # Step 3: Iterate through the sorted folders and add only non-subfolders
        for i in range(1, len(folder)):
            # Check if the current folder is not a subfolder of the last added folder
            if not folder[i].startswith(result[-1] + "/"):
                result.append(folder[i])
        
        return result




# class Tree:
#     def __init__(self):
#         self.folderhash = {}
    
#     def add(self, path):
#         folderlist = path.split('/')
        
#         begin = folderlist[1]
#         if not begin in self.folderhash:
#             self.folderhash[begin] = MyNode()
#         curNode = self.folderhash[begin]
#         curNode.val = begin
#         # print(folderlist)
#         for i in range(2, len(folderlist)):
#             # print(curNode)
#             nxtset = curNode.nextval
#             curfolder = folderlist[i]
#             if not curfolder in nxtset:
#                 nxtset[curfolder] = MyNode()
#             curNode = nxtset[curfolder]
#             curNode.val = curfolder

#         # print('end.',curNode.val)
#         curNode.isfinish = True
#         curNode.endval = path
    
#     def getAll(self):
#         res = []
#         for i in self.folderhash.values():
#             tres = self.getOneNode(i)
#             res += tres
#         return res

    
#     def getOneNode(self, node):
#         resset = []
#         # print(node.val)
#         if node.isfinish:
#             resset.append(node.endval)
#             return resset
#         else:
#             for i in node.nextval.values():
#                 tres =  self.getOneNode(i)
#                 resset += tres
#         return resset



        
                
                


             

# class MyNode:
#     def __init__(self):
#         self.val = ''
#         self.nextval = {}
#         self.isfinish = False
#         self.endval = ''


# class Solution:
#     def removeSubfolders(self, folder: List[str]) -> List[str]:

#         folder_hash = Tree()
#         for i in folder:
#             folder_hash.add(i)
#         return folder_hash.getAll()
        

        