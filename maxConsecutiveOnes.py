'''
Problem Statement:>>> ---> (https://leetcode.com/problems/max-consecutive-ones/submissions/) --> (link to the problem discription)
'''

# Solution:>>>

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        counter = 0
        for number in nums:
            if number == 1:
                counter += number
            else:
                maxOnes = counter if maxOnes < counter else maxOnes
                counter = 0
        maxOnes = counter if maxOnes < counter else maxOnes
        return maxOnes
