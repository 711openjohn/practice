# Given an unsorted array of integers nums, return the length of the longest 
# consecutive elements sequence. 
# 
#  You must write an algorithm that runs in O(n) time. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
# Therefore its length is 4.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
# 
#  👍 19064 👎 898


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        exists = set(nums)
        max_seq = 1
        for num in exists:
            if (num - 1) not in exists:
                current = num
                local_seq = 1
                while (current + 1) in exists:
                    local_seq += 1
                    current += 1
                    max_seq = max(max_seq, local_seq)
        return max_seq
        
# leetcode submit region end(Prohibit modification and deletion)
