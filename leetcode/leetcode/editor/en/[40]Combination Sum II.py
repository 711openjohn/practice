# Given a collection of candidate numbers (candidates) and a target number (
# target), find all unique combinations in candidates where the candidate numbers sum 
# to target. 
# 
#  Each number in candidates may only be used once in the combination. 
# 
#  Note: The solution set must not contain duplicate combinations. 
# 
#  
#  Example 1: 
# 
#  
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#  
# 
#  Example 2: 
# 
#  
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= candidates.length <= 100 
#  1 <= candidates[i] <= 50 
#  1 <= target <= 30 
#  
# 
#  👍 10001 👎 265
from typing import List
# time: O(n * 2^n)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(result, path, current, start):
            if current > target:
                return
            if current == target:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                current += candidates[i]
                path.append(candidates[i])
                backtracking(result, path, current, i + 1)
                path.pop()
                current -= candidates[i]
        result = []
        candidates.sort()
        backtracking(result, [], 0, 0)
        return result
# leetcode submit region end(Prohibit modification and deletion)
Solution().combinationSum2([10,1,2,7,6,1,5], 8)