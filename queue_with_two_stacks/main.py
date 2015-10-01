
class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    print(self.items)
    l = len(self.items)
    return self.items[l - 1]

  def is_empty(self):
    if len(self.items):
      return False
    return True

class QueueNaive:
  def __init__(self):
    self.stack_one = Stack()
    self.stack_two = Stack()

  def enqueue(self, item):
    if self.stack_one.is_empty():
      self.stack_one.push(item)
    else:
      pop_item = self.stack_one.pop()

      while (pop_item):
        self.stack_two.push(pop_item)
        if self.stack_one.is_empty():
          pop_item = False
        else:
          pop_item = self.stack_one.pop()

      self.stack_one.push(item)

      pop_item = self.stack_two.pop()

      while (pop_item):
        self.stack_one.push(pop_item)
        if self.stack_two.is_empty():
          pop_item = False
        else:
          pop_item = self.stack_two.pop()

  def dequeue(self):
    return self.stack_one.pop()

  def peek(self):
    return self.stack_one.peek()

  def is_empty(self):
    return self.stack_one.is_empty()

qn = QueueNaive()
qn.enqueue(1)
qn.enqueue(2)
qn.enqueue(3)
qn.enqueue(4)

res = qn.dequeue()
print(res)
res = qn.dequeue()
print(res)
res = qn.dequeue()
print(res)
