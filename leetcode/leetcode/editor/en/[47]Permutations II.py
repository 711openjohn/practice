# Given a collection of numbers, nums, that might contain duplicates, return 
# all possible unique permutations in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 8 
#  -10 <= nums[i] <= 10 
#  
# 
#  👍 8280 👎 137
from typing import List
# time: O(n! * n)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtracking(result, path, used: list):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                if not used[i - 1] and i > 0 and nums[i] == nums[i-1]:
                    continue

                used[i] = True
                path.append(nums[i])
                backtracking(result, path, used)
                used[i] = False
                path.pop()

        result = []
        nums.sort()
        used = [False] * len(nums)
        backtracking(result, [], used)
        return result


# leetcode submit region end(Prohibit modification and deletion)
Solution().permuteUnique([1,1,2])