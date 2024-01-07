# Given an integer array nums that may contain duplicates, return all possible 
# subsets (the power set). 
# 
#  The solution set must not contain duplicate subsets. Return the solution in 
# any order. 
# 
#  
#  Example 1: 
#  Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#  
#  Example 2: 
#  Input: nums = [0]
# Output: [[],[0]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  
# 
#  👍 9323 👎 273
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtracking(result, path, start):
            result.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtracking(result, path, i + 1)
                path.pop()

        nums.sort()
        result = []
        backtracking(result, [], 0)
        return result

# leetcode submit region end(Prohibit modification and deletion)
Solution().subsetsWithDup([2,1,2])