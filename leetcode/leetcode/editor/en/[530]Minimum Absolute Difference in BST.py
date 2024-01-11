# Given the root of a Binary Search Tree (BST), return the minimum absolute 
# difference between the values of any two different nodes in the tree. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [4,2,6,1,3]
# Output: 1
#  
# 
#  Example 2: 
#  
#  
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [2, 10⁴]. 
#  0 <= Node.val <= 10⁵ 
#  
# 
#  
#  Note: This question is the same as 783: https://leetcode.com/problems/
# minimum-distance-between-bst-nodes/ 
# 
#  👍 4224 👎 212
from typing import Optional


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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(root, result):
            if root is None:
                return
            inorder(root.left, result)
            result.append(root.val)
            inorder(root.right, result)

        result = []
        inorder(root, result)

        min_diff = float('inf')
        for i in range(1, len(result)):
            min_diff = min(min_diff, result[i] - result[i - 1])
        return min_diff

# leetcode submit region end(Prohibit modification and deletion)
