# Given a binary search tree (BST), find the lowest common ancestor (LCA) node 
# of two given nodes in the BST. 
# 
#  According to the definition of LCA on Wikipedia: “The lowest common ancestor 
# is defined between two nodes p and q as the lowest node in T that has both p 
# and q as descendants (where we allow a node to be a descendant of itself).” 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
#  
# 
#  Example 2: 
#  
#  
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant 
# of itself according to the LCA definition.
#  
# 
#  Example 3: 
# 
#  
# Input: root = [2,1], p = 2, q = 1
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [2, 10⁵]. 
#  -10⁹ <= Node.val <= 10⁹ 
#  All Node.val are unique. 
#  p != q 
#  p and q will exist in the BST. 
#  
# 
#  👍 10656 👎 296


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def postorder(root, p, q):
            if root is None:
                return None

            if root.val > p.val and root.val > q.val:
                left = postorder(root.left, p, q)
                if left:
                    return left
            if root.val < p.val and root.val < q.val:
                right = postorder(root.right, p, q)
                if right:
                    return right
            return root

        return postorder(root, p, q)
    #
    # def traversal(self, cur, p, q):
    #     if cur is None:
    #         return cur
    #
    #     if cur.val > p.val and cur.val > q.val:  # 左
    #         left = self.traversal(cur.left, p, q)
    #         if left is not None:
    #             return left
    #
    #     if cur.val < p.val and cur.val < q.val:  # 右
    #         right = self.traversal(cur.right, p, q)
    #         if right is not None:
    #             return right
    #
    #     return cur

# leetcode submit region end(Prohibit modification and deletion)
