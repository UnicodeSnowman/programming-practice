# Hooray! It's opposite day. Linked lists go the opposite way today.
# Write a function for reversing a linked list ↴ . Do it in-place ↴ .
# 
# Your function will have one input: the head of the list.
# 
# Your function should return the new head of the list.

class ListItem:
  def __init__(self, value, next):
    self.value = value
    self.next = next


def reverse(head):

  current = head
  previous = None
  next = None

  while (current is not None):
    next = current.next
    current.next = previous

    # previous (eventually) becomes our new head.
    previous = current
    current = next

  return previous

head = ListItem(1, ListItem(2, ListItem(3, None)))

res = reverse(head)

print(res.value, res.next.value, res.next.next.value, res.next.next.next)
