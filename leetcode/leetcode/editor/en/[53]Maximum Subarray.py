# Given an integer array nums, find the subarray with the largest sum, and 
# return its sum. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
#  Follow up: If you have figured out the O(n) solution, try coding another 
# solution using the divide and conquer approach, which is more subtle. 
# 
#  👍 32860 👎 1374
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [i for i in nums]
        result = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            result = max(result, dp[i])
        return result
# leetcode submit region end(Prohibit modification and deletion)
Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])