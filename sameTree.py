'''
Problem Statement: (https://leetcode.com/problems/same-tree/) ---> (link to the problem description)
'''

# Solution:>>>

# Method - 1:>> --> (recursive method)

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if not p and not q: return True          
		# Both the nodes p and q reaches the end(null) if every value in their respective branches are equal
    
        if not p and q: return False
        # return False if one of the nodes is null.
		
        if p and not q: return False
		# Same as above
    
        if p.val != q.val:  return False
    	# return False if their respective values are not equal to eachother at their respective nodes
		
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
