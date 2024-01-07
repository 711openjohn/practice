# Given an array nums of distinct integers, return all the possible 
# permutations. You can return the answer in any order. 
# 
#  
#  Example 1: 
#  Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
#  Example 2: 
#  Input: nums = [0,1]
# Output: [[0,1],[1,0]]
#  
#  Example 3: 
#  Input: nums = [1]
# Output: [[1]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  All the integers of nums are unique. 
#  
# 
#  👍 18414 👎 298
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(result, path, used: set):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if i in used:
                    continue
                used.add(i)
                path.append(nums[i])
                backtracking(result, path, used)
                path.pop()
                used.remove(i)

        result = []
        backtracking(result, [], set())
        return result


# leetcode submit region end(Prohibit modification and deletion)
Solution().permute([1, 2, 3])
