'''
Problem Statement:>>> --> (https://leetcode.com/problems/longest-common-prefix/submissions/) --> (link to the problem discription)
'''

# Solution:>>>

# Method - 1:>> --> (Brute force method(Accepted))

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        res = ""
        first = strs[0]
        allEqual = 0
        for c in first:
            for i in range(1, len(strs)):
                if allEqual >= len(strs[i]) or c != strs[i][allEqual]:
                    return res
            res += c
            allEqual += 1
        return res
