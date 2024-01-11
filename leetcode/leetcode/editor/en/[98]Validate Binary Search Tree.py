# Given the root of a binary tree, determine if it is a valid binary search 
# tree (BST). 
# 
#  A valid BST is defined as follows: 
# 
#  
#  The left subtree of a node contains only nodes with keys less than the 
# node's key. 
#  The right subtree of a node contains only nodes with keys greater than the 
# node's key. 
#  Both the left and right subtrees must also be binary search trees. 
#  
# 
#  
#  Example 1: 
#  
#  
# Input: root = [2,1,3]
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁴]. 
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
# 
#  👍 16270 👎 1327


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        current_max = float('-inf')
        def validate(root):
            if root is None:
                return True
            left = validate(root.left)
            nonlocal current_max
            if root.val > current_max:
                current_max = root.val
            else:
                return False
            right = validate(root.right)

            return left and right
        return validate(root)
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     current_max = float('-inf')
    #     def validate(root):
    #         if root is None:
    #             return True
    #         nonlocal current_max
    #         left = validate(root.left)
    #         if root.val > current_max:
    #             current_max = root.val
    #         else:
    #             return False
    #         right = validate(root.right)
    #         return left and right
    #
    #     return validate(root)

# leetcode submit region end(Prohibit modification and deletion)
