
class ListItem:
  def __init__(self, value, next):
    self.value = value
    self.next = next


def reverse(head):

  current = head
  previous = None

  while (current is not None):
    next = current.next
    current.next = previous
    previous = current
    current = next

  return previous

head = ListItem(1, ListItem(2, ListItem(3, None)))

res = reverse(head)

print(res.value, res.next.value, res.next.next.value, res.next.next.next)
