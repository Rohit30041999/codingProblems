'''
Problem Statement:>>> () -> (link to the problem discription)
'''

'''
Solution:>>> 

Method - I:>>> (level order wise storing and retrieving)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        
        if not root: return 0
        
        universal = []
		
        # level order traversal for storing all the values in an array called universal
        queue = []
        queue = collections.deque(queue)
        queue.append(root)
        while queue:
            node = queue.popleft()
            universal.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        # converting universal array into a set to get rid of duplicate values.
        universal = list(set(universal))
        universal.sort()
        
        #returning the adjacent minimum difference value.
        return min([universal[i+1]-universal[i] for i in range(len(universal)-1)])
