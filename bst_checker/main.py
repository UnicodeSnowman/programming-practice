# Write a function to check that a binary tree is a valid binary search tree 

class BinaryTreeNode:
  def __init__(self, value, left=None, right=None):
      # if left and/or right aren't specified,
      # they get a default value of None
      self.value = value
      self.left  = left
      self.right = right

def bst_checker(tree):

  def is_valid(value, left, right, ancestors):
    if not left:
      return True

    ancestors[value] = True

    return (
        is_valid(left.value, left.left, left.right, ancestors) and
        is_valid(right.value, right.left, right.right, ancestors))

  return is_valid(tree.value, tree.left, tree.right, { 50: True })

a = BinaryTreeNode(2,
      BinaryTreeNode(1),
      BinaryTreeNode(3))

b = BinaryTreeNode(50,
        BinaryTreeNode(30,
          BinaryTreeNode(20),
          BinaryTreeNode(60)),
        BinaryTreeNode(80,
          BinaryTreeNode(70),
          BinaryTreeNode(90)))

print(bst_checker(b))
