# Question - Given an array which consists of only 0, 1 and 2. [LeetCode]
# Link - https://leetcode.com/problems/sort-colors/

# Date - 2 October, 2021


# _____________________________________________________________________________________

# Solution :-


# Approach 1 (Using Two pointer approach)
#   - Space : O(1)
#   - Time : O(n)


class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums) - 1
        pointer = 0
        while pointer <= end:
            if nums[pointer] == 2:
                nums[pointer], nums[end] = nums[end], nums[pointer]
                end -= 1
            elif nums[pointer] == 0:
                nums[pointer], nums[start] = nums[start], nums[pointer]
                pointer += 1
                start += 1
            else:
                pointer += 1

