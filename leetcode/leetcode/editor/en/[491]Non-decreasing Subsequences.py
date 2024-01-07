# Given an integer array nums, return all the different possible non-decreasing 
# subsequences of the given array with at least two elements. You may return the 
# answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 15 
#  -100 <= nums[i] <= 100 
#  
# 
#  👍 3561 👎 226
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtracking(result, path, start):
            if len(path) > 1:
                result.append(path[:])

            exists = set()
            for i in range(start, len(nums)):
                if nums[i] in exists or (path and nums[i] < path[-1]):
                    continue
                exists.add(nums[i])
                path.append(nums[i])
                backtracking(result, path, i + 1)
                path.pop()
        result = []
        backtracking(result, [], 0)
        return result
        # def backtracking(result, path, start):
        #     if len(path) > 1:
        #         result.append(path[:])
        #
        #     uset = set()  # 使用集合对本层元素进行去重
        #     for i in range(start, len(nums)):
        #         if (path and nums[i] < path[-1]) or nums[i] in uset:
        #             continue
        #
        #         uset.add(nums[i])  # 记录这个元素在本层用过了，本层后面不能再用了
        #         path.append(nums[i])
        #         backtracking(result, path, i + 1)
        #         path.pop()
# leetcode submit region end(Prohibit modification and deletion)
