# Given the head of a singly linked list, reverse the list, and return the 
# reversed list. 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#  
# 
#  Example 2: 
#  
#  
# Input: head = [1,2]
# Output: [2,1]
#  
# 
#  Example 3: 
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
#  The number of nodes in the list is the range [0, 5000]. 
#  -5000 <= Node.val <= 5000 
#  
# 
#  
#  Follow up: A linked list can be reversed either iteratively or recursively. 
# Could you implement both? 
# 
#  👍 20371 👎 383


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(head, prev):
            if not head:
                return prev
            new_head = head.next
            head.next = prev
            return rev(new_head, head)
        return rev(head, None)
# leetcode submit region end(Prohibit modification and deletion)
