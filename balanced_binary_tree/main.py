# https://www.interviewcake.com/question/balanced-binary-tree
# Write a function to see if a binary tree ↴ is "superbalanced" (a new tree property we just made up).
# A tree is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one.

class BinaryTreeNode:
  def __init__(self, value, left=None, right=None):
      # if left and/or right aren't specified,
      # they get a default value of None
      self.value = value
      self.left  = left
      self.right = right

def is_balanced(tree):
  results = []

  def check(n, t1, t2):
    if t1 and not t2:
      # have reached a node with only a Left
      results.append(n)
      return check(n + 1, t1.left, t1.right) + n
    elif t2 and not t1:
      # have reached a node with only a Right
      results.append(n)
      return n + check(n + 1, t2.left, t2.right)
    elif not t1 and not t2:
      # we have a reached a leaf node
      results.append(n)
      return n
    else:
      return check(n + 1, t1.left, t1.right) + check(n + 1, t2.left, t2.right)

  check(0, tree.left, tree.right)

  return abs(max(results) - min(results)) <= 1

one = BinaryTreeNode(2,
    BinaryTreeNode(1,
      BinaryTreeNode(1),
      BinaryTreeNode(1)),
    BinaryTreeNode(1,
      BinaryTreeNode(1),
      BinaryTreeNode(1)))

two = BinaryTreeNode(2,
    BinaryTreeNode(1,
      BinaryTreeNode(1),
      BinaryTreeNode(1)),
    BinaryTreeNode(1,
      BinaryTreeNode(1),
      BinaryTreeNode(1, BinaryTreeNode(2), BinaryTreeNode(2))))

tree = BinaryTreeNode(2, one, two)
res = is_balanced(tree)
print(res)

# improvements / alternates:
# * short circuit if we end up with a depth difference of more than 1 / minimize the result array for constant space
# * could also implement this as a stack... pop nodes on, then popping off when a leaf is reached

