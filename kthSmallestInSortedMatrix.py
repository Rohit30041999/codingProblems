'''
Problem Statement:>> --> 'https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/' --> (link to the problem discription)
'''

#Solution:>>>

#Method:>>> --> (direct access method after sotring)

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res.append(matrix[i][j])
        res.sort()
        return res[k-1]
