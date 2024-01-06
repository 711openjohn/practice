# Given two integers n and k, return all possible combinations of k numbers 
# chosen from the range [1, n]. 
# 
#  You may return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to 
# be the same combination.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 20 
#  1 <= k <= n 
#  
# 
#  👍 7952 👎 208
from typing import List


# time: O(n * 2^n)
# space: O(n)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(n, k, s, path, result):
            if len(path) == k:
                result.append(path[:])
                return
            # n - (k - len(path)) + 2)
            for i in range(s, n + 1):
                path.append(i)
                backtracking(n, k, i + 1, path, result)
                path.pop()

        result = []
        backtracking(n, k, 1, [], result)
        return result
    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     def backtracking(n, k, startIndex, path, result):
    #         if len(path) == k:
    #             result.append(path[:])
    #             return
    #         for i in range(startIndex, n + 1):  # 需要优化的地方
    #             path.append(i)  # 处理节点
    #             backtracking(n, k, i + 1, path, result)
    #             path.pop()  # 回溯，撤销处理的节点
    #     result = []
    #     backtracking(n, k, 1, [], result)
    #     return result


# leetcode submit region end(Prohibit modification and deletion)
Solution().combine(4, 2)
