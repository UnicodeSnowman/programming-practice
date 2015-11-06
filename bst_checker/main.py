# Write a function to check that a binary tree is a valid binary search tree 

class BinaryTreeNode:
  def __init__(self, value, left=None, right=None):
      # if left and/or right aren't specified,
      # they get a default value of None
      self.value = value
      self.left  = left
      self.right = right

def bst_checker(tree):

  def is_valid_right(value, left, right, ancestors):
    # is greater than all ancestors
    for ancestor in ancestors:
      if value < ancestor:
        return False

    ancestors.append(value)

    if left is None:
      left_result = False
    else:
      left_result = is_valid_right(left.value, left.left, left.right, ancestors)

    if right is None:
      right_result = False
    else:
      right_result = is_valid_right(right.value, right.left, right.right, ancestors)

    return left_result and right_result

  def is_valid_left(value, left, right, ancestors):
    # is less than all ancestors
    for ancestor in ancestors:
      if value > ancestor:
        return False

    if left is None:
      left_result = True
    elif left.value > value:
      return False
    else:
      left_result = is_valid_left(left.value, left.left, left.right, ancestors + [value])

    if right is None:
      right_result = True
    elif right.value < value:
      return False
    else:
      right_result = is_valid_left(right.value, right.left, right.right, ancestors)

    return left_result and right_result

    return (
        is_valid_left(left.value, left.left, left.right, ancestors) and
        is_valid(right.value, right.left, right.right, ancestors))

  return (
    is_valid_left(tree.value, tree.left, None, []) and True)
    #is_valid_right(tree.value, None, tree.right, [tree.value]))

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
