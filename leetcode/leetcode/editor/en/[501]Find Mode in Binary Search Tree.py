# Given the root of a binary search tree (BST) with duplicates, return all the 
# mode(s) (i.e., the most frequently occurred element) in it. 
# 
#  If the tree has more than one mode, return them in any order. 
# 
#  Assume a BST is defined as follows: 
# 
#  
#  The left subtree of a node contains only nodes with keys less than or equal 
# to the node's key. 
#  The right subtree of a node contains only nodes with keys greater than or 
# equal to the node's key. 
#  Both the left and right subtrees must also be binary search trees. 
#  
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,null,2,2]
# Output: [2]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [0]
# Output: [0]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁴]. 
#  -10⁵ <= Node.val <= 10⁵ 
#  
# 
#  
# Follow up: Could you do that without using any extra space? (Assume that the 
# implicit stack space incurred due to recursion does not count).
# 
#  👍 3800 👎 769
from collections import defaultdict
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def searchBST(self, cur, freq_map):
        if cur is None:
            return
        freq_map[cur.val] += 1  # 统计元素频率
        self.searchBST(cur.left, freq_map)
        self.searchBST(cur.right, freq_map)

    def findMode(self, root):
        freq_map = defaultdict(int)  # key:元素，value:出现频率
        result = []
        if root is None:
            return result
        self.searchBST(root, freq_map)
        max_freq = max(freq_map.values())
        for key, freq in freq_map.items():
            if freq == max_freq:
                result.append(key)
        return result
# leetcode submit region end(Prohibit modification and deletion)
