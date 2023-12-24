#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (61.21%)
# Likes:    7255
# Dislikes: 156
# Total Accepted:    503.3K
# Total Submissions: 821.5K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given the head of a singly linked list where elements are sorted in ascending
# order, convert it to a height-balanced binary search tree.
#
#
# Example 1:
#
#
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the
# shown height balanced BST.
#
#
# Example 2:
#
#
# Input: head = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in head is in the range [0, 2 * 10^4].
# -10^5 <= Node.val <= 10^5
#
#
#


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def sortedListToBST(self, head):
        if not head:
            return None

        if not head.next:
            return TreeNode(val=head.val)

        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(slow.next.val)
        right = slow.next.next
        slow.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(right)
        return root

    # def sortedListToBST(self, head):
    #     """
    #     :type head: Optional[ListNode]
    #     :rtype: Optional[TreeNode]
    #     """
    #     if not head:
    #         return None

    #     if not head.next:
    #         return TreeNode(head.val)

    #     # Find the middle element of the linked list
    #     slow, fast = head, head.next.next
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next

    #     # Create a new TreeNode with the middle element as the root
    #     root = TreeNode(slow.next.val)

    #     # Recursively construct the left and right subtrees
    #     right_head = slow.next.next
    #     slow.next = None
    #     root.left = self.sortedListToBST(head)
    #     root.right = self.sortedListToBST(right_head)

    #     return root


# @lc code=end
