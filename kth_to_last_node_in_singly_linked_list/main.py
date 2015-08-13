# https://www.interviewcake.com/question/kth-to-last-node-in-singly-linked-list
#
# You have a linked list and want to find the kth to last node.
# Write a function kth_to_last_node() that takes an integer k and the head_node 
# of a singly linked list, and returns the kth to last node in the list.

class Node:
  def __init__(self, value, next):
    self.value = value
    self.next = next

a = Node("Angel Food",
    Node("Bundt",
    Node("Cheese",
    Node("Devil's Food",
    Node("Eccles", None)))))

# O(n), worst case 2n
def kth_to_last_node(i, list):

  # could also implement this non-recursively, i.e.
  # while(node.next):
  #   node = node.next
  #   length += 1
  # 
  # ... etc.
  def iter(node, length):
    if node.next:
      return iter(node.next, length + 1)
    else:
      return length

  def get_at_i(node, i, counter):
    if counter is i:
      return node
    else:
      return get_at_i(node.next, i, counter + 1)

  list_length = iter(list, 0) + 1
  val = get_at_i(list, list_length - i, 0)

  return val.value

def kth_to_last_node_n_time(i, list):
  return "Test"

res = kth_to_last_node(2, a)
print(res)
