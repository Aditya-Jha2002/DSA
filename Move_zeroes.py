# Question - Move Zeroes [LeetCode]
# Link - https://leetcode.com/problems/move-zeroes/

# Date - 2 October, 2021


# _____________________________________________________________________________________

# Solution :-


# Approach 1 (Two Pointer Approach)
#   - Space : O(1)
#   - Time : O(n)


class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pointer = 0

        for moving_pointer in range(len(nums)):
            if nums[moving_pointer] != 0:
                nums[moving_pointer], nums[zero_pointer] = (
                    nums[zero_pointer],
                    nums[moving_pointer],
                )
                zero_pointer += 1
