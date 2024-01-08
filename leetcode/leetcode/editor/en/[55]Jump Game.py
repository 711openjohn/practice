# You are given an integer array nums. You are initially positioned at the 
# array's first index, and each element in the array represents your maximum jump 
# length at that position. 
# 
#  Return true if you can reach the last index, or false otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum 
# jump length is 0, which makes it impossible to reach the last index.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  0 <= nums[i] <= 10⁵ 
#  
# 
#  👍 18500 👎 1111
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = nums[0]
        for i in range(1, len(nums)):
            if i > cover:
                return False
            cover = max(cover, nums[i] + i)
            if cover >= len(nums):
                return True
        if cover >= len(nums) - 1:
            return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().canJump([3,2,1,0,4]))