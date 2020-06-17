# problemStatement: (https://www.interviewbit.com/problems/swap-list-nodes-in-pairs/) <-- (link to the problem description)

# Solution: (Optimal) <-- (O(n))

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        cur = A
        while cur != None and cur.next != None:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        return A
