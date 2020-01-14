'''
Problem Statement:>>> --> (https://leetcode.com/problems/pascals-triangle/submissions/)  --> (link to the problem discription)
'''

# Solution:>>>

# Method - 1:>> -> (direct method)

class Solution:
    def generate(self, row: int) -> List[List[int]]:
        res = []
        if row <= 0: return res
        if row == 1: return [[1]]
        res.append([1])
        tempRes = []
        for _ in range(row-1):
            temporary = []
            for i in range(len(tempRes)-1):
                temporary.append(tempRes[i] + tempRes[i+1])
            tempRes = [1] + temporary + [1]
            res.append(tempRes)
        return res
