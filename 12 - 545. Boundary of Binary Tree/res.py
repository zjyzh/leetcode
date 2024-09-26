# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def isLeaf(self, node):

        if node.left == None and node.right == None:
            return True
        else:
            return False

    def buildLeft(self, node):

        if node == None:
            return
        
        if not self.isLeaf(node):
            self.leftSet.append(node.val)
            if not node.left == None:
                self.buildLeft(node.left)
            elif not node.right == None:
                self.buildLeft(node.right)
        
           
    def buildLeaf(self, root):
        if self.isLeaf(root):
            self.leafSet.append(root.val)
        else:
            if not root.left == None:
                self.buildLeaf(root.left)
            if not root.right == None: 
                self.buildLeaf(root.right)

    def buildRight(self, node):
        if node == None:
            return
        if not self.isLeaf(node):
            self.rightSet.append(node.val)
            if not node.right == None:
                self.buildRight(node.right)
            elif not node.left == None:
                self.buildRight(node.left)
        

    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        if root == None:
            return []
        self.rootSet = [root.val]

        self.leftSet = []
        self.rightSet = []
        self.leafSet = []
        self.buildLeft(root.left)
        self.buildRight(root.right)
        if not self.isLeaf(root):
            self.buildLeaf(root)

        self.rightSet.reverse()
        # print(self.rootSet , self.leftSet , self.leafSet , self.rightSet)

        return self.rootSet  + self.leftSet + self.leafSet + self.rightSet

        