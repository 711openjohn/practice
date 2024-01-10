# Given an array nums of n integers, return an array of all the unique 
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that: 
# 
#  
#  0 <= a, b, c, d < n 
#  a, b, c, and d are distinct. 
#  nums[a] + nums[b] + nums[c] + nums[d] == target 
#  
# 
#  You may return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 200 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  
# 
#  👍 10852 👎 1314
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l = j + 1
                r = len(nums) - 1

                while l < r:
                    local_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if local_sum > target:
                        r = r - 1
                    elif local_sum < target:
                        l = l + 1
                    else:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[r] == nums[r - 1]:
                            r = r - 1
                        while l < r and nums[l] == nums[l + 1]:
                            l = l + 1
                        r = r - 1
                        l = l + 1
        return result
# leetcode submit region end(Prohibit modification and deletion)

Solution().fourSum([1,-2,-5,-4,-3,3,3,5], -11)
# Solution().fourSum([1,0,-1,0,-2,2], 0)