# Question - Reverse the Array [Geeks for Geeks]
# Link - https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

# Date - 2 October, 2021


# Approach 1 (Brute Force Approach) - Space : O(n), Time : O(n)
class Solution:
    def reverseArray(self, nums: list) -> list:
        arr = []
        for i in reversed(range(len(nums))):
            arr.append(nums[i])
        return arr


# Approach 1 (Brute Force Approach) - Space : O(1), Time : O(n)
class Solution1:
    def reverseArray(self, nums: list) -> list:
        size = len(nums)
        for i in range((size//2) + 1):
            nums[i], nums[size-i-1] = nums[size-i-1], nums[i]
        return nums
