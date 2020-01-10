'''
Problem Statement: --> "https://leetcode.com/problems/reorder-list/" --> (link to the problem discription)
'''

# Solution:>>>

# Method - 1: ---> (deque method)
def reorderList(self, head: ListNode) -> None:
	"""
	Do not return anything, modify head in-place instead.
	"""
	if not head or not head.next:      # if the linked list is in the form 'None' or '1->None' there's no need to modify the head.
		return
        
	tempArr = []
	current = head
	while current:
		tempArr.append(current)
		current = current.next
            
	tempArr = collections.deque(tempArr)     #deque data structure from collections module
        
	step = 1
        
	newHead = tempArr.popleft()
	currentHead = newHead
        
	while tempArr:
		currentHead.next = tempArr.pop() if (step % 2) != 0 else tempArr.popleft()
		step += 1
		currentHead = currentHead.next
        
	currentHead.next = None
        
	head = newHead    #modifying head inplace instead of returning it.
