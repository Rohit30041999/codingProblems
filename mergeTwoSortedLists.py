# problemStatement: (https://www.interviewbit.com/problems/merge-two-sorted-lists/) <-- (link to problem description)

# Solution: (Optimal) -- (O(n))

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if A == None and B == None: return None
        if A == None: return B
        if B == None: return A
        dummy = ListNode(-1)
        dum = dummy
        if A.val <= B.val:
            dum.next = A
            dum = dum.next
            A = A.next
        else:
            dum.next = B
            dum = dum.next
            B = B.next
        while A!=None and B!=None:
            if A.val <= B.val:
                dum.next = A
                dum = dum.next
                A = A.next
            else:
                dum.next = B
                dum = dum.next
                B = B.next
        while A!=None:
            dum.next = A
            dum = dum.next
            A = A.next
        while B!=None:
            dum.next = B
            dum = dum.next
            B = B.next
        dum.next = None
        return dummy.next
