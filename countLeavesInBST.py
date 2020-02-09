'''
Problem Statement:>>> (https://practice.geeksforgeeks.org/problems/count-leaves-in-binary-tree/1) -> (link to the problem description)
'''

'''
Solution:>>>

Method - I: --> (level order traversal)
'''

def countLeaves(root):
    if not root: return 0
    countLeaves = 0
    queue = []
    queue = collections.deque(queue)
    queue.append(root)
    while queue:
        currentNode = queue.popleft()
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
        else:
            countLeaves += 1
    return countLeaves
