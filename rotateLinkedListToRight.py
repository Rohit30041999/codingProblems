# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        o = []
        if k == 0: return head
        while head:
            o.append(head.val)
            head = head.next
        if o == []: return head
        k %= len(o)
        o = o[-k:] + o[:-k]
        head1 = ListNode(o[0])
        res = head1
        for i in range(1, len(o)):
            node = ListNode(o[i])
            head1.next = node
            head1 = head1.next
        return res
