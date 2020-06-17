# problemStatement: (https://www.interviewbit.com/problems/palindrome-list/) <-- (link to the problem description)

# Solution : (Most Optimal) (O(n)) <-- (linear runtime and constant space)

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

def reverse(node):
    if node == None: return node
    if node.next == None: return node
    t = node.next
    p = None
    while t!=None:
        node.next = p
        p = node
        node = t
        t = t.next
    node.next = p
    p = node
    node = t
    return p

class Solution:
	# @param A : head node of linked list
	# @return an integer
	def lPalin(self, A):
        if A == None: return 1
        if A.next == None: return 1
        slow, fast = A, A
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        reversedNode = reverse(slow.next)
        while reversedNode != None:
            if A.val != reversedNode.val: return 0
            A = A.next
            reversedNode = reversedNode.next
        return 1
