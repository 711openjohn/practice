# Given the root of a binary tree, check whether it is a mirror of itself (i.e.,
#  symmetric around its center). 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 1000]. 
#  -100 <= Node.val <= 100 
#  
# 
#  
# Follow up: Could you solve it both recursively and iteratively?
# 
#  👍 14760 👎 360


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def compare(left, right):
            none_checker = {left, right}
            if len(none_checker) == 1:
                return True
            if len(none_checker) == 2 and None in none_checker:
                return False
            if left.val != right.val:
                return False

            outside = compare(left.left, right.right)
            inside = compare(left.right, right.left)
            return outside and inside
        if not root:
            return True

        return compare(root.left, root.right)
# leetcode submit region end(Prohibit modification and deletion)
