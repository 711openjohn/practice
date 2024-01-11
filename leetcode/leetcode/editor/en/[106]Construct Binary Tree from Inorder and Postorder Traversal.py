# Given two integer arrays inorder and postorder where inorder is the inorder 
# traversal of a binary tree and postorder is the postorder traversal of the same 
# tree, construct and return the binary tree. 
# 
#  
#  Example 1: 
#  
#  
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  Example 2: 
# 
#  
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= inorder.length <= 3000 
#  postorder.length == inorder.length 
#  -3000 <= inorder[i], postorder[i] <= 3000 
#  inorder and postorder consist of unique values. 
#  Each value of postorder also appears in inorder. 
#  inorder is guaranteed to be the inorder traversal of the tree. 
#  postorder is guaranteed to be the postorder traversal of the tree. 
#  
# 
#  👍 7767 👎 125
from typing import List


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
    # def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    def buildTree(self, inorder: List[int], postorder: List[int]):
        if len(postorder) == 0:
            return None

        root_value = postorder[-1]
        inorder_root_index = inorder.index(root_value)
        left_inorder = inorder[0: inorder_root_index]
        right_inorder = inorder[inorder_root_index + 1: len(inorder) + 1]

        left_postorder = []
        right_postorder = postorder[0: len(postorder) - 1]
        if left_inorder:
            left_postorder = postorder[0: len(left_inorder)]
            right_postorder = postorder[len(left_inorder) : len(postorder) - 1]

        root = TreeNode(val=root_value)
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root


# leetcode submit region end(Prohibit modification and deletion)
Solution().buildTree([9,3,15,20,7], postorder = [9,15,7,20,3])
