# Given an integer n, return all the structurally unique BST's (binary search 
# trees), which has exactly n nodes of unique values from 1 to n. Return the answer 
# in any order. 
# 
#  
#  Example 1: 
#  
#  
# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]
# ]
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: [[1]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 8 
#  
# 
#  👍 7406 👎 499
from functools import lru_cache
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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(None)
        def gen(l, r):
            if l > r:
                return [None]
            if l == r:
                return [TreeNode(val=l)]
            result = []
            for root in range(l, r + 1):
                leftnodes = gen(l, root - 1)
                rightnodes = gen(root + 1, r)
                for ln in leftnodes:
                    for rn in rightnodes:
                        node = TreeNode(val=root)
                        node.left = ln
                        node.right = rn
                        result.append(node)
            return result
        return gen(1, n)
    # def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
    #     @lru_cache(None)
    #     def gen(l, r):
    #         if l > r:
    #             return [None]
    #         if l == r:
    #             return [TreeNode(val=l)]
    #
    #         result = []
    #         for root in range(l, r + 1):
    #             leftNodes = gen(l, root - 1)
    #             rightNodes = gen(root + 1, r)
    #             for ln in leftNodes:
    #                 for rn in rightNodes:
    #                     node = TreeNode(val=root)
    #                     node.left = ln
    #                     node.right = rn
    #                     result.append(node)
    #         return result
    #
    #     return gen(1, n)
        
# leetcode submit region end(Prohibit modification and deletion)
