#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (41.88%)
# Likes:    19808
# Dislikes: 922
# Total Accepted:    1.5M
# Total Submissions: 3.6M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' + '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design a data structure that follows the constraints of a Least Recently Used
# (LRU) cache.
#
# Implement the LRUCache class:
#
#
# LRUCache(int capacity) Initialize the LRU cache with positive size
# capacity.
# int get(int key) Return the value of the key if the key exists, otherwise
# return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds
# the capacity from this operation, evict the least recently used key.
#
#
# The functions get and put must each run in O(1) average time complexity.
#
#
# Example 1:
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
# Constraints:
#
#
# 1 <= capacity <= 3000
# 0 <= key <= 10^4
# 0 <= value <= 10^5
# At most 2 * 10^5 calls will be made to get and put.
#
#
#

# @lc code=start

from collections import deque


import heapq
from time import time


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.data = dict()
        self.access = []

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.data:
            return -1
        (val, _) = self.data[key]
        d_at = time()
        self.data[key] = (val, d_at)

        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        d_at = time()
        if key in self.data:
            self.data[key] = (value, d_at)
            return

        if self.capacity == 0:
            self.remove_lru()

        self.data[key] = (value, d_at)
        heapq.heappush(
            self.access, (d_at, key)
        )  # Assuming "set"ting is also counted as "use"
        self.capacity -= 1

    def remove_lru(self):
        while True:
            (lru_at, key) = self.access[0]
            (_, d_at) = self.data[key]
            if d_at > lru_at:
                heapq.heappop(self.access)
                heapq.heappush(self.access, (d_at, key))
            else:
                heapq.heappop(self.access)
                del self.data[key]
                self.capacity += 1
                return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
