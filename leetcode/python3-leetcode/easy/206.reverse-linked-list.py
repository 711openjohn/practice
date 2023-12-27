#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (75.13%)
# Likes:    20280
# Dislikes: 378
# Total Accepted:    3.6M
# Total Submissions: 4.8M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, reverse the list, and return the
# reversed list.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
#
# Example 2:
#
#
# Input: head = [1,2]
# Output: [2,1]
#
#
# Example 3:
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
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
#
#
#
# Follow up: A linked list can be reversed either iteratively or recursively.
# Could you implement both?
#
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
# Definition for singly-linked list.


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def rev(pre, head):
            if head is None:
                return pre
            n = head.next
            head.next = pre
            return rev(head, n)

        return rev(None, head)

    # def reverseList(self, head: ListNode) -> ListNode:
    #     def rev(prev, head):
    #         if not head:
    #             return prev
    #         cur = head.next
    #         head.next = prev
    #         prev = head
    #         return rev(head, cur)
    #     return rev(None, head)


# @lc code=end
