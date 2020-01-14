'''
Problem Statement:>>> --> (https://leetcode.com/problems/pascals-triangle-ii/submissions/)  --> (link to the problem discription)
'''

# Solution:>>>

# Method - 1:>> -> (direct method)

class Solution:
    def getRow(self, row: int) -> List[int]:
        res = []
        if row == 0: return [1]
        for _ in range(row):
            tempRes = []
            for i in range(len(res)-1):
                tempRes.append(res[i] + res[i+1])
            res = [1] + tempRes + [1]
        return res
