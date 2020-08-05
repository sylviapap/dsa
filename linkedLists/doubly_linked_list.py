# Construct doubly linked list
# Methods: set head/tail, insert/remove nodes, search for node with given value
# Complexity:
  # O(1) time, O(1) space: set head/tail, insert before/after, remove
  # O(p) time, O(1) space: insert at pos where p = pos
  # O(n) time, O(1) space: remove with value, search
    # because traversing the list, others take node as param

class Node:
# value is int
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def setHead(self, node):
    if self.head is None:
      self.head = node
      self.tail = node
      return
    self.insertBefore(self.head, node)

  def setTail(self, node):
    if self.tail is None:
      self.setHead(node)
      return
    self.insertAfter(self.tail, node)

  def insertBefore(self, node, nodeToInsert):
    if nodeToInsert == self.head and nodeToInsert == self.tail:
      return
    self.remove(nodeToInsert)
    nodeToInsert.prev = node.prev
    nodeToInsert.next = node
    if node.prev is None:
      self.head = nodeToInsert
    else:
      node.prev.next = nodeToInsert
    node.prev = nodeToInsert

  def insertAfter(self, node, nodeToInsert):
    if nodeToInsert == self.head and nodeToInsert == self.tail:
      return
    self.remove(nodeToInsert)
    nodeToInsert.prev = node
    nodeToInsert.next = node.next
    if node.next is None:
      self.tail = nodeToInsert
    else:
      node.next.prev = nodeToInsert
    node.next = nodeToInsert

# pos is int
  def insertAtPosition(self, position, nodeToInsert):
    if position == 1:
      self.setHead(nodeToInsert)
      return
    node = self.head
    currentPosition = 1
    while node is not None and currentPosition != position:
      node = node.next
      currentPosition += 1
    if node is not None:
      self.insertBefore(node, nodeToInsert)
    else:
      self.setTail(nodeToInsert)

# value is int
  def removeNodesWithValue(self, value):
    node = self.head
    while node is not None:
      nodeToRemove = node
      node = node.next
      if nodeToRemove.value == value:
        self.remove(nodeToRemove)

  def remove(self, node):
    if node == self.head:
      self.head = self.head.next
    if node == self.tail:
      self.tail = self.tail.prev
    self.updatePointers(node)

# value is int, return bool
  def containsNodeWithValue(self, value):
    node = self.head
    while node is not None and node.value != value:
      node = node.next
    return node is not None

  def updatePointers(self, node):
    if node.prev is not None:
      node.prev.next = node.next
    if node.next is not None:
      node.next.prev = node.prev
    node.prev = None
    node.next = None