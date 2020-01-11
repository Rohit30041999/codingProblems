'''
Problem Statement:>>> --> 'https://leetcode.com/problems/sort-list/' --> (link to the problem discription)
'''

#Solution:>>>

def sortList(self, head: ListNode) -> ListNode:
	if not head or not head.next: return head
	numbers = []
   	current = head
   	while current:
    		numbers.append(current.val)
        	current = current.next
    	numbers.sort()
    	current = head
    	for num in numbers:
    		current.val = num
        	current = current.next
    	return head
