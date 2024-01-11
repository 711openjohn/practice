# Design a data structure that follows the constraints of a Least Recently Used 
# (LRU) cache. 
# 
#  Implement the LRUCache class: 
# 
#  
#  LRUCache(int capacity) Initialize the LRU cache with positive size capacity. 
# 
#  int get(int key) Return the value of the key if the key exists, otherwise 
# return -1. 
#  void put(int key, int value) Update the value of the key if the key exists. 
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds 
# the capacity from this operation, evict the least recently used key. 
#  
# 
#  The functions get and put must each run in O(1) average time complexity. 
# 
#  
#  Example 1: 
# 
#  
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= capacity <= 3000 
#  0 <= key <= 10⁴ 
#  0 <= value <= 10⁵ 
#  At most 2 * 10⁵ calls will be made to get and put. 
#  
# 
#  👍 19906 👎 925




# leetcode submit region begin(Prohibit modification and deletion)
class Node:
    def __init__(self, key=None, val=None):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

    def __str__(self):
        return f'({self.key}:{self.val})'

    def __repr__(self):
        return f'({self.key}:{self.val})'
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail

    def print(self):
        result = []
        current = self.head
        while current:
            result.append(current)
            current = current.next
        return str(result)

    def get(self, key: int) -> int:
        value_node = self.cache.get(key, None)
        if not value_node:
            return -1

        # pop value node
        self._remove_key(key)
        self._append_head(key, value_node.val)

        return value_node.val

    def put(self, key: int, value: int) -> None:
        self._remove_key(key)
        self._append_head(key, value)
        if len(self.cache.keys()) > self.capacity:
            if self.tail.prev.key != None:
                self._remove_key(self.tail.prev.key)
    def _append_head(self, key, val):
        value_node = Node(key=key, val=val)
        pre_head = self.head.next
        self.head.next = value_node
        value_node.prev = self.head
        value_node.next = pre_head
        pre_head.prev = value_node
        self.cache[key] = value_node

    def _remove_key(self, key):
        if not self.cache.get(key):
            return

        value_node = self.cache.get(key)
        self.cache.pop(key)

        p = value_node.prev
        n = value_node.next
        p.next = n
        n.prev = p
        value_node.prev = None
        value_node.next = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
