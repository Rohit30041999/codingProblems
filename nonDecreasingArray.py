'''
Problem Statement:>>> 'https://leetcode.com/problems/non-decreasing-array/' --> (link to the problem discription)
'''

# Solution:>>>
# Method - 1: --> (counter method)

def checkPossibility(self, nums: List[int]) -> bool:
       	if not nums or len(nums) == 1: return True
        counter = 0
        maxElement = -pow(2, 31)
        for index in range(0, len(nums)-1):
            if nums[index] > nums[index + 1]:
                if counter != 1:
                    if nums[index+1] <= maxElement:
                        nums[index+1] = nums[index] + 1
                        counter += 1
                    else:
                        nums[index] = nums[index+1] - 1
                        counter += 1
                else: return False
            elif maxElement < nums[index]:
                maxElement = nums[index]
        return True
