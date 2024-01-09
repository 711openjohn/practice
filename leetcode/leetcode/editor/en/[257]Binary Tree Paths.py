# Given the root of a binary tree, return all root-to-leaf paths in any order. 
# 
#  A leaf is a node with no children. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1]
# Output: ["1"]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 100]. 
#  -100 <= Node.val <= 100 
#  
# 
#  👍 6350 👎 275


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def backtracking(root, result, path):
            path.append(root.val)
            if root.left is None and root.right is None:
                result.append('->'.join(map(str, path)))
                return

            if root.left:
                backtracking(root.left, result, path)
                path.pop()

            if root.right:
                backtracking(root.right, result, path)
                path.pop()

        result = []
        path = []
        backtracking(root, result, path)
        return result
# leetcode submit region end(Prohibit modification and deletion)
