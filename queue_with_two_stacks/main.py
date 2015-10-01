from stack import Stack

# currently optimized for dequeue... i.e. store data in correct order,
# making for easy dequeue. we could also optimize this for enqueue
# which is (probably) smarter, but the general idea is here
class QueueNaive:
  def __init__(self):
    self.stack_one = Stack()
    self.stack_two = Stack()

  def __move_from(self, from_stack, to_stack):
      pop_item = from_stack.pop()
      while (pop_item):
        to_stack.push(pop_item)
        if from_stack.is_empty():
          pop_item = False
        else:
          pop_item = from_stack.pop()

  # here, one enqueue operation is O(m),
  # number of operations is m, so worst
  # case is O(m^2)
  def enqueue(self, item):
    if self.stack_one.is_empty():
      self.stack_one.push(item)
    else:
      # move everything off our main stack
      # to our utility stack
      self.__move_from(self.stack_one, self.stack_two)

      # put the new item on the main stack
      self.stack_one.push(item)

      # move everything back from our utility stack
      # to our main stack
      self.__move_from(self.stack_two, self.stack_one)

  def dequeue(self):
    return self.stack_one.pop()

  def peek(self):
    return self.stack_one.peek()

  def is_empty(self):
    return self.stack_one.is_empty()

### buuuuut apparently we can get O(m) runtime for m function calls... so back to the drawing board
# what if we don't flip items back after initial flip?
class QueueBaller:
  def __init__(self):
    self.reversed_stack = Stack()
    self.ordered_stack = Stack()

  def __move_from(self, from_stack, to_stack):
      pop_item = from_stack.pop()
      while (pop_item):
        to_stack.push(pop_item)
        if from_stack.is_empty():
          pop_item = False
        else:
          pop_item = from_stack.pop()

  def enqueue(self, item):
    self.reversed_stack.push(item)

  def dequeue(self):
    if self.ordered_stack.is_empty():
      self.__move_from(self.reversed_stack, self.ordered_stack)
      return self.ordered_stack.pop()
    else:
      return self.ordered_stack.pop()

  def peek(self):
    # I suppose we could check ordered_stack, but what if it's empty? do we run the move operation just for peek?
    print(self.reversed_stack.peek())
    print(self.ordered_stack.peek())
    #return self.stack_one.peek()

  def is_empty(self):
    return self.reversed_stack.is_empty() and self.ordered_stack.is_empty()

#qn = QueueNaive()
#qn.enqueue(1)
#qn.enqueue(2)
#qn.dequeue()
#qn.enqueue(3)
#qn.enqueue(4)

q = QueueBaller()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.enqueue(4)


