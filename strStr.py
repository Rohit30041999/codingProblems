#LEETCODE(Solution):>>>

#Implement strStr(parentString, childString):>>
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (len(haystack) == 0 and len(needle) == 0) or len(needle) == 0: return 0
        if len(needle) > len(haystack): return -1
        for i in range(len(haystack)-len(needle)+1):
            for j in range(i+1, i+len(needle)+1):
                if haystack[i:j] == needle: return i
        return -1

#TestingTheCode:>>
solution = Solution()
print(solution.strStr("hello", "ll"))    #output: 2(index of ll in hello)
print(solution.strStr("", "a"))    #output: -1
print(solution.strStr("", ""))    #output: 0
print(solution.strStr("h", ""))    #output: 0
