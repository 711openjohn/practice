#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#
# https://leetcode.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Medium (52.31%)
# Likes:    7607
# Dislikes: 244
# Total Accepted:    427.7K
# Total Submissions: 816.7K
# Testcase Example:  '[1,3,null,null,2]'
#
# You are given the root of a binary search tree (BST), where the values of
# exactly two nodes of the tree were swapped by mistake. Recover the tree
# without changing its structure.
#
#
# Example 1:
#
#
# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]
# Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3
# makes the BST valid.
#
#
# Example 2:
#
#
# Input: root = [3,1,4,null,null,2]
# Output: [2,1,4,null,null,3]
# Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2
# and 3 makes the BST valid.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [2, 1000].
# -2^31 <= Node.val <= 2^31 - 1
#
#
#
# Follow up: A solution using O(n) space is pretty straight-forward. Could you
# devise a constant O(1) space solution?
#

from typing import Optional
from ds_builder import tree_builder


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.val}"

    def __str__(self) -> str:
        return f"{self.val}"


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        start = None
        prev = None
        end = None

        def inorder(root):
            if not root:
                return None
            nonlocal start, prev, end
            inorder(root.left)
            if prev and prev.val > root.val:
                if not start:
                    start = prev
                end = root
            prev = root
            inorder(root.right)

        inorder(root)
        if start:
            start.val, end.val = end.val, start.val

    # def recoverTree(self, root: TreeNode) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     start = None
    #     prev = None
    #     last = None

    #     def dfs(root):
    #         nonlocal start, prev, last
    #         if not root:
    #             return
    #         dfs(root.left)
    #         if prev and prev.val > root.val:
    #             if not start:
    #                 start = prev
    #             last = root
    #         prev = root
    #         dfs(root.right)

    #     dfs(root)
    #     if start and last:
    #         start.val, last.val = last.val, start.val

    # start = None
    # prev = None
    # last = None

    # def dfs(root):
    #     nonlocal start, prev, last
    #     if not root:
    #         return
    #     dfs(root.left)

    #     if prev and prev.val > root.val:
    #         if not start:
    #             start = prev
    #         last = root
    #     prev = root
    #     dfs(root.right)

    # dfs(root)
    # if start and last:
    #     start.val, last.val = last.val, start.val


# @lc code=end

Solution().recoverTree(tree_builder([3, 1, 4, None, None, 2]))

# In the brute force approach,
# the space complexity is O(n) we have to do better,
# If you think in the problem only two nodes are swapped,
# what we can do we can traverse the tree in an In-Order fashion and
# create one previous node and set the value to null after
# that we will traverse the tree and compare the current node value with
# the previous node value if the previous node is not null
# and previous node value is greater than the current node value
# than we can push back the previous and current node in our vector of pairs,
# because this is the node which is swapped.

# We have all such pairs in our array.
# The array size will be 1 or 2 not more than 2 because only two nodes are swapped.
# if the array size is 1 that means only two adjacent nodes are swapped else the array size will be 2.

# So we have to accordingly swap the numbers to get back to the original tree.
