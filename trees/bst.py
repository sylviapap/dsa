# A node is BST IFF its value is strictly greater than every node to the left, less than or equal to every node to the right, and children nodes are either BST as well or None/null

class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

# Function that takes in a BST and target integer value and returns closest value
# O(log(n)) time average, O(1) space
def findClosest(tree, target):
  closest = tree.value
  currentNode = tree
  while currentNode is not None:
		if abs(target - closest) > abs(target - currentNode.value):
			closest = currentNode.value
		if target < currentNode.value:
			currentNode = currentNode.left
		elif target > currentNode.value:
			currentNode = currentNode.right
		else:
			break
  return closest