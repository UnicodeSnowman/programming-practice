class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    l = len(self.items)
    if l:
      return self.items[l - 1]

  def is_empty(self):
    if len(self.items):
      return False
    return True

