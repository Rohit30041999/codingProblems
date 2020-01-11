'''
Problem Statement:>>> --> 'https://leetcode.com/problems/sort-colors/' --> (link to the problem discription)
'''

# Solution:>>>

# Method 1: ---> (collections.Counter method)

def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = collections.Counter(nums)
        i = 0
        for key in sorted(count.keys()):
            j = 0
            while j < count[key]:
                nums[i] = key
                j += 1
                i += 1
