# Given two integer arrays preorder and inorder where preorder is the preorder 
# traversal of a binary tree and inorder is the inorder traversal of the same tree,
#  construct and return the binary tree. 
# 
#  
#  Example 1: 
#  
#  
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  Example 2: 
# 
#  
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= preorder.length <= 3000 
#  inorder.length == preorder.length 
#  -3000 <= preorder[i], inorder[i] <= 3000 
#  preorder and inorder consist of unique values. 
#  Each value of inorder also appears in preorder. 
#  preorder is guaranteed to be the preorder traversal of the tree. 
#  inorder is guaranteed to be the inorder traversal of the tree. 
#  
# 
#  👍 14404 👎 453
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None

        root_value = preorder[0]

        inorder_root_index = inorder.index(root_value)
        left_inorder = inorder[0: inorder_root_index]
        right_inorder = inorder[inorder_root_index + 1: len(inorder)]

        left_preorder = []
        right_preorder = preorder[1: len(preorder)]
        if len(left_inorder) > 0:
            left_preorder = preorder[1: 1 + len(left_inorder)]
            right_preorder = preorder[1 + len(left_inorder): len(preorder)]

        root = TreeNode(val=root_value)
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root


# leetcode submit region end(Prohibit modification and deletion)
Solution().buildTree([3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])
