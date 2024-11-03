'''
利用递归求解
dfs的函数返回一个数组，这个数组记录的是子节点距离当前节点的集合
分为两个数组，一个左边，一个右边的集合
[] []
然后遍历这两个集合，如果这两个集合的任意元素加起来小于dis，那么结果加一
最后再将这两个集合合并，返回到上一层继续判断
注意用到了一些剪枝手法，如果俩个集合元素相加小于dis才会返回给上层
这样能确保集合的数量较小

'''




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self.result = 0
        self.distance = distance
        
        def dfs(node):
            if not node:
                return []
            
            # Leaf node, return distance 1 (distance from itself)
            if not node.left and not node.right:
                return [1]
            
            # Recursively get distances from left and right subtrees
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            # Count good pairs between left and right distances
            for ld in left_distances:
                for rd in right_distances:
                    if ld + rd <= self.distance:
                        self.result += 1
            
            # Collect distances incremented by 1 for parent level
            new_distances = []
            for d in left_distances + right_distances:
                if d + 1 < self.distance:
                    new_distances.append(d + 1)
            
            return new_distances
        
        dfs(root)
        return self.result



# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:

#     def dfs(self, node, height):

#         if node and (node.left or node.right):
#             left_collect = self.dfs(node.left,  height+1)
#             right_collect = self.dfs(node.right,  height +1)

#             for i in left_collect:
#                 dis_i = i[1]
#                 for j in right_collect:
#                     dis_j = j[1]
#                     if ((dis_i - height) + (dis_j - height)) <= self.distance:
#                         self.res += 1
#             return left_collect + right_collect

#         else:
#             if node:
#                 return [(node, height)]
#         return []

#     def countPairs(self, root: Optional[TreeNode], distance: int) -> int:

#         self.res = 0
#         self.distance = distance
#         if root:
#             self.dfs(root, 0)
#         else:
#             return 0
        
#         return self.res

        