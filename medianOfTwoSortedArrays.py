'''
Problem Statement:>>> ---> (https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/) ---> (link to the problem discription)
'''

# Solution:>>>

# Method:>>> --> (sorting method (quite slow))

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums)%2 != 0:
            return nums[math.ceil((0+(len(nums)-1))/2)]
        else:
            return (nums[math.ceil((0+(len(nums)-1))/2)] + nums[math.ceil((0+(len(nums)-1))/2)-1])/2
