#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (47.40%)
# Likes:    18919
# Dislikes: 886
# Total Accepted:    1.5M
# Total Submissions: 3.1M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#
# Example 1:
#
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
#
#
# Example 2:
#
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
#
#


# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        nums.sort(key=lambda x: x)
        lookup = {nums[-1]: False}

        for i in range(0, len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                lookup[nums[i]] = True
            else:
                lookup[nums[i]] = False

        count = 1
        max_count = 1
        for key in sorted(lookup.keys()):
            if lookup[key]:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        return max_count

    # def longestConsecutive(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     # If list is empty
    #     if nums == []:
    #         return 0

    #     # Sort the list
    #     nums = sorted(nums)

    #     # Create Dictionary
    #     maps = {}
    #     for i in range(len(nums)):
    #         try:
    #             if nums[i] + 1 == nums[i + 1]:
    #                 maps[nums[i]] = 0
    #             else:
    #                 maps[nums[i]] = 1
    #         except:  # when (i+1) == len(nums)
    #             maps[nums[i]] = 1
    #             break

    #     # Set counter variable (count) and max varialble (maxi)
    #     count = 1
    #     maxi = 1

    #     # Sort the keys
    #     for i in sorted(maps.keys()):
    #         if maps[i] == 0:
    #             count += 1  # Count the number of 0's
    #         if maps[i] == 1:
    #             if maxi < count:  # Compare max count value
    #                 maxi = count
    #             count = 1  # Reset count value
    #             continue

    #     return maxi


# @lc code=end

Solution().longestConsecutive([0, 3, 7, 2, 5, 5, 8, 4, 6, 0, 1])
