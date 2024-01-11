# You are given two binary trees root1 and root2. 
# 
#  Imagine that when you put one of them to cover the other, some nodes of the 
# two trees are overlapped while the others are not. You need to merge the two 
# trees into a new binary tree. The merge rule is that if two nodes overlap, then sum 
# node values up as the new value of the merged node. Otherwise, the NOT null 
# node will be used as the node of the new tree. 
# 
#  Return the merged tree. 
# 
#  Note: The merging process must start from the root nodes of both trees. 
# 
#  
#  Example 1: 
#  
#  
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]
#  
# 
#  Example 2: 
# 
#  
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in both trees is in the range [0, 2000]. 
#  -10⁴ <= Node.val <= 10⁴ 
#  
# 
#  👍 8618 👎 290
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
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None

        left_value = 0
        left_root1 = None
        left_root2 = None
        right_root1 = None
        right_root2 = None

        if root1:
            left_value = root1.val
            left_root1 = root1.left
            right_root1 = root1.right
        right_value = 0
        if root2:
            right_value = root2.val
            left_root2 = root2.left
            right_root2 = root2.right

        root = TreeNode(val=left_value + right_value)
        root.left = self.mergeTrees(left_root1, left_root2)
        root.right = self.mergeTrees(right_root1, right_root2)
        return root

# leetcode submit region end(Prohibit modification and deletion)
