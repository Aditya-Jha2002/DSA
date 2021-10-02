# Question - Find the maximum and minimum element in an array [Geeks for Geeks]
# Link - https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/

# Date - 2 October, 2021


# Approach 1 (Looping through the array) - Space : O(n), Time : O(1)
class Solution:
    def maxMinArray(self, nums: list) -> tuple:
        max = nums[0]
        min = nums[0]
        if len(nums) == 1:
            return min, max
        for num in nums:
            if num > max:
                max = num
            if num < min:
                min = num
        return (max, min)
