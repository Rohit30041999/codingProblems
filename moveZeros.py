'''
Problem Statement:>>> 'https://leetcode.com/problems/move-zeroes/' --> (link to the problem discription)
'''

# Solution:>>>
# Method - 1: --> (count method)
def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numbers = []
        for number in nums:
            if number != 0: numbers.append(number)
        numbers = numbers + [0] * nums.count(0)
        for index in range(len(nums)):
            nums[index] = numbers[index]
