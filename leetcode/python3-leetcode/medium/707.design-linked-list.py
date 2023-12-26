#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#
# https://leetcode.com/problems/design-linked-list/description/
#
# algorithms
# Medium (27.98%)
# Likes:    2500
# Dislikes: 1561
# Total Accepted:    298.7K
# Total Submissions: 1.1M
# Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\n' +
# '[[],[1],[3],[1,2],[1],[1],[1]]'
#
# Design your implementation of the linked list. You can choose to use a singly
# or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val
# is the value of the current node, and next is a pointer/reference to the next
# node.
# If you want to use the doubly linked list, you will need one more attribute
# prev to indicate the previous node in the linked list. Assume all nodes in
# the linked list are 0-indexed.
#
# Implement the MyLinkedList class:
#
#
# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the index^th node in the linked list. If
# the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of
# the linked list. After the insertion, the new node will be the first node of
# the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the
# linked list.
# void addAtIndex(int index, int val) Add a node of value val before the
# index^th node in the linked list. If index equals the length of the linked
# list, the node will be appended to the end of the linked list. If index is
# greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the index^th node in the linked list, if
# the index is valid.
#
#
#
# Example 1:
#
#
# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get",
# "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]
#
# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
#
#
#
# Constraints:
#
#
# 0 <= index, val <= 1000
# Please do not use the built-in LinkedList library.
# At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and
# deleteAtIndex.
#
#
#


# @lc code=start
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.vh = ListNode()

    def p(self):
        c = self.vh
        result = []
        while c.next:
            result.append(c.next.val)
            c = c.next
        return result

    def get(self, index: int) -> int:
        if index > self.size:
            return -1

        i = 0
        cur = self.vh.next
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        node = ListNode(val=val)
        tail = self.vh.next
        self.vh.next = node
        node.next = tail
        self.size += 1

    def addAtTail(self, val: int) -> None:
        self.size += 1
        prev = self.vh
        cur = self.vh.next
        while cur:
            prev = cur
            cur = cur.next
        prev.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        self.size += 1
        prev = self.vh
        cur = self.vh.next

        i = 0
        while cur:
            if i == index:
                break
            prev = cur
            cur = cur.next
            i += 1

        prev.next = ListNode(val=val)
        prev.next.next = cur

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1


# class MyLinkedList:
#     def __init__(self):
#         self.dummy_head = ListNode()
#         self.size = 0

#     def get(self, index: int) -> int:
#         if index < 0 or index >= self.size:
#             return -1

#         current = self.dummy_head.next
#         for i in range(index):
#             current = current.next

#         return current.val

#     def addAtHead(self, val: int) -> None:
#         self.dummy_head.next = ListNode(val, self.dummy_head.next)
#         self.size += 1

#     def addAtTail(self, val: int) -> None:
#         current = self.dummy_head
#         while current.next:
#             current = current.next
#         current.next = ListNode(val)
#         self.size += 1

#     def addAtIndex(self, index: int, val: int) -> None:
#         if index < 0 or index > self.size:
#             return

#         current = self.dummy_head
#         for i in range(index):
#             current = current.next
#         current.next = ListNode(val, current.next)
#         self.size += 1

#     def deleteAtIndex(self, index: int) -> None:
#         if index < 0 or index >= self.size:
#             return

#         current = self.dummy_head
#         for i in range(index):
#             current = current.next
#         current.next = current.next.next
#         self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end


# [null,null,null,null,null,null,null,8,null,6,7,null]
