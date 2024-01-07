# Given an integer array nums of unique elements, return all possible subsets (
# the power set). 
# 
#  The solution set must not contain duplicate subsets. Return the solution in 
# any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0]
# Output: [[],[0]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  All the numbers of nums are unique. 
#  
# 
#  👍 16341 👎 248
# 时间复杂度: O(n * 2^n)
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(result, path, start):
            result.append(path[:])  # 收集子集，要放在终止添加的上面，否则会漏掉自己

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(result, path, i + 1)
                path.pop()
        result = []
        backtracking(result, [],0)
        return result
# leetcode submit region end(Prohibit modification and deletion)
Solution().subsets([1,2,3])