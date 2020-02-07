'''
Problem Statement:>>> (https://leetcode.com/problems/n-ary-tree-postorder-traversal/) -> (link to the description)
'''

'''
Solution:>>>

Method - I:>>> (Depth first search using Stack)
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        stack = []
        result = []
        stack.append(root)
        while stack:
            currentRoot = stack.pop()
            result += [currentRoot.val]
            for child in currentRoot.children:
                stack.append(child)
        return result[::-1]        # This thing basically reverse a list in python. Which is called as List Comprehension.
