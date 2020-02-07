'''
Problem Statement:>>> (https://leetcode.com/problems/n-ary-tree-preorder-traversal/) -> (link to the problem discription)
'''

Solution:>>>

Method - I: >>> (Depth first search using stack)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children   
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        if not root: return result
        if not root.children: return [root.val]      
		# here the variable will be an array or list if there is something(such as collection of nodes) present in it otherwise it will be a null value.
        stack = []
        stack.append(root)
        while stack:
            currentRoot = stack.pop()
            result.append(currentRoot.val)
            if currentRoot.children:
                for i in range(len(currentRoot.children)-1, -1, -1):
                    stack.append(currentRoot.children[i])
        return result
