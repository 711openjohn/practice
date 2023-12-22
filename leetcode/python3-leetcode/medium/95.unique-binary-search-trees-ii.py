#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (56.77%)
# Likes:    7370
# Dislikes: 493
# Total Accepted:    430.4K
# Total Submissions: 756.6K
# Testcase Example:  '3'
#
# Given an integer n, return all the structurally unique BST's (binary search
# trees), which has exactly n nodes of unique values from 1 to n. Return the
# answer in any order.
#
#
# Example 1:
#
#
# Input: n = 3
# Output:
# [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [[1]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 8
#
#
#

from functools import lru_cache
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(None)
        def dfs(l, r):
            if l > r:
                return [None]
            if l == r:
                return [TreeNode(l)]

            ans = []

            for root in range(l, r + 1):
                leftNodes = dfs(l, root - 1)
                rightNodes = dfs(root + 1, r)
                for ln in leftNodes:
                    for rn in rightNodes:
                        ans.append(TreeNode(val=root, left=ln, right=rn))
            return ans
        return dfs(1, n)

        # @lru_cache(None)
        # def dfs(left, right):
        #     if left > right:
        #         return [None]
        #     if left == right:
        #         return [TreeNode(left)]
        #     ans = []
        #     for root in range(left, right + 1):
        #         leftNodes = dfs(left, root - 1)
        #         rightNodes = dfs(root + 1, right)
        #         for leftNode in leftNodes:
        #             for rightNode in rightNodes:
        #                 rootNode = TreeNode(root, leftNode, rightNode)
        #                 ans.append(rootNode)
        #     return ans

        # return dfs(1, n)


# @lc code=end
