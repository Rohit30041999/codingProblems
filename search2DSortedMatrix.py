'''
Problem Statement:>> --> (https://leetcode.com/problems/search-a-2d-matrix-ii/) --> (link to the problem discription)
'''

# Solution:>>>

# Method - 1:>>> --> (binary search method)

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if search(row, 0, len(row)-1, target) > -1: return True
        return False

def search(L, l, h, t):
    if l > h:
        return -1
    mid = (l + h)//2
    if L[mid] == t:
        return mid
    elif L[mid] > t:
        return search(L, l, mid-1, t)
    elif L[mid] < t:
        return search(L, mid+1, h, t)
