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

# Complexity
# Each enqueue is clearly O(1)O(1) time, and so is each dequeue when out_stack has items. Dequeue on an empty out_stack is order of the number of items in in_stack at that moment, which can vary significantly.
# 
# Notice that the more expensive a dequeue on an empty out_stack is (that is, the more items we have to move from in_stack to out_stack), the more O(1)O(1)-time dequeues off of a non-empty out_stack it wins us in the future. Once items are moved from in_stack to out_stack they just sit there, ready to be dequeued in O(1) time. An item never moves "backwards" in our data structure.
# 
# We might guess that this "averages out" so that in a set of mm enqueues and dequeues the total cost of all dequeues is actually just O(m)O(m). To check this rigorously, we can use the accounting method ↴ , counting the time cost per item instead of per enqueue or dequeue.
# 
# So let's look at the worst case for a single item, which is the case where it is enqueued and then later dequeued. In this case, the item enters in_stack (costing 1 push), then later moves to out_stack (costing 1 pop and 1 push), then later comes off out_stack to get returned (costing 1 pop).
# 
# Each of these 4 pushes and pops is O(1)O(1) time. So our total cost per item is O(1)O(1). Our mm enqueue and dequeue operations put mm or fewer items into the system, giving a total runtime of O(m)O(m)!
