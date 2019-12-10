#LINKED LIST REVERSE USING STACK:>>
class Node():
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

def reverseList(head):
  if head is None: return head
  stack = []
  while head:
    stack.append(head)
    head = head.next
  head = stack.pop()
  current = head
  print(head.data)
  print(current.data)
  while stack:
    current.next = stack.pop()
    current = current.next
  current.next = None
  return head

def main():
  head = Node(3)
  head1 = Node(2, head)
  head2 = Node(1, head1)
  he = reverseList(head2)
  while he is not None:
    print(he.data, end = "->")
    he = he.next
  print('null')

main()
