# problemStatement: (https://www.interviewbit.com/problems/reverse-link-list-ii/) <-- (link to the problem description)

# Solution: (using stack) <-- (O(n))

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        if A == None: return A
        dummy = ListNode(0)
        dummy.next = A
        prev = dummy
        count = 1
        while count < B and prev != None:
            prev = prev.next
            count += 1
        if prev == None: return A
        stack = []
        cur = prev.next
        while count <= C and cur != None:
            count += 1
            stack.append(cur)
            cur = cur.next
        while stack:
            prev.next = stack.pop()
            prev = prev.next
        prev.next = cur
        return dummy.next
