# Write a function to check that a binary tree is a valid binary search tree 

# NOTES
#
# depth-first search 
#    * generally requires less memory
#    * can be easily implemented recursively
#    * doesn't necessarily find the shortest path to a node
#
# breadth-first search 
#    * finds the shortest path to a target, but not (necessarily) quickly
#    * requires more memory

MAX = 99999
MIN = -99999

class BinaryTreeNode:
  def __init__(self, value, left=None, right=None):
      # if left and/or right aren't specified,
      # they get a default value of None
      self.value = value
      self.left  = left
      self.right = right

def bst_checker_naive(tree):
  def is_valid(value, left, right, predicates):
    for predicate in predicates:
      if not predicate(value):
        return False

    if right is None:
      right_result = True
    elif right.value < value:
      right_result = False
    else:
      right_result = is_valid(right.value, right.left, right.right, predicates + [lambda x: x > value])

    if left is None:
      left_result = True
    elif left.value > value:
      left_result = False
    else:
      left_result = is_valid(left.value, left.left, left.right, predicates + [lambda x: x < value])

    return left_result and right_result

  return is_valid(tree.value, tree.left, tree.right, [])

a = BinaryTreeNode(2,
      BinaryTreeNode(1),
      BinaryTreeNode(3))

b = BinaryTreeNode(50,
        BinaryTreeNode(30,
          BinaryTreeNode(20),
          BinaryTreeNode(40)),
        BinaryTreeNode(80,
          BinaryTreeNode(70),
          BinaryTreeNode(90)))

# much better:
# we don't need to keep track of all the ancestors, we really just need an upper bound and lower bound
#
# Complexity:
# O(n) time, O(n) additional space. additional space is O(logn) if our tree is balanced
def bst_checker(root, lower_bound=MIN, upper_bound=MAX):
  if not root:
    return True

  if (root.value > upper_bound or root.value < lower_bound):
    return False

  # set our bounds depending on if we're traversing left or right. for left, the child nodes cannot be greater
  # than the current node value, so we reset our upper bound. same/inverse for the right side... the right
  # nodes cannot be less than the root value, so we reset our lower_bound
  return bst_checker(root.left, lower_bound, root.value) and bst_checker(root.right, root.value, upper_bound)

print(bst_checker(b))
