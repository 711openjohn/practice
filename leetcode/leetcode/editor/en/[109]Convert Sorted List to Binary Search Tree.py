# Given the head of a singly linked list where elements are sorted in ascending 
# order, convert it to a height-balanced binary search tree. 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the 
# shown height balanced BST.
#  
# 
#  Example 2: 
# 
#  
# Input: head = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in head is in the range [0, 2 * 10⁴]. 
#  -10⁵ <= Node.val <= 10⁵ 
#  
# 
#  👍 7278 👎 157


# leetcode submit region begin(Prohibit modification and deletion)
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
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None
        if head.next is None:
            return TreeNode(val=head.val)

        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        root_pt = slow.next
        right_head = slow.next.next
        slow.next = None

        root = TreeNode(val=root_pt.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(right_head)
        return root



    # def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    #     if not head:
    #         return None
    #
    #     if not head.next:
    #         return TreeNode(val=head.val)
    #
    #     slow = head
    #     fast = head.next.next
    #
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #
    #     root = TreeNode(slow.next.val)
    #     right = slow.next.next
    #     slow.next = None
    #     root.left = self.sortedListToBST(head)
    #     root.right = self.sortedListToBST(right)
    #     return root
# leetcode submit region end(Prohibit modification and deletion)
