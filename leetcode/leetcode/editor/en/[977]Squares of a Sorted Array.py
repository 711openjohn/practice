# Given an integer array nums sorted in non-decreasing order, return an array 
# of the squares of each number sorted in non-decreasing order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums is sorted in non-decreasing order. 
#  
# 
#  
# Follow up: Squaring each element and sorting the new array is very trivial, 
# could you find an 
# O(n) solution using a different approach?
# 
#  👍 8585 👎 213
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        l = 0
        r = len(nums) - 1
        index = len(nums) - 1
        result = [0] * len(nums)
        while index >= 0:
            l_sq = nums[l] * nums[l]
            r_sq = nums[r] * nums[r]
            if r_sq > l_sq:
                result[index] = r_sq
                r -= 1
            else:
                result[index] = l_sq
                l += 1
            index -= 1
        return result
# leetcode submit region end(Prohibit modification and deletion)
Solution().sortedSquares([-3, 1,2])