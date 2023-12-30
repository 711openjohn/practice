# Given an integer array nums, return the length of the longest strictly 
# increasing subsequence. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the 
# length is 4.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2500 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
#  Follow up: Can you come up with an algorithm that runs in O(n log(n)) time 
# complexity? 
# 
#  👍 19330 👎 366
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums))
        result = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i])
        return result
        # dp = [1] * (len(nums) + 1)
        # result = 1
        # for i in range(1, len(nums)):
        #     for j in range(0, i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        #     result = max(result, dp[i])
        # return result
# leetcode submit region end(Prohibit modification and deletion)
