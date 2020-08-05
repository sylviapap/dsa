# Create a singly linked list, append items and iterate through the list

class Node:
  def __init__(self, data=0, next=None):
    self.data = data
    self.next = next

class singly_linked_list:
  def __init__(self):
    self.tail = None
    self.head = None
    self.count = 0

  def iterate_item(self):
    current_item = self.tail
    while current_item:
      val = current_item.data
      current_item = current_item.next
      yield val

  def append_item(self, data):
    node = Node(data)
    if self.head:
      self.head.next = node
      self.head = node
    else:
      self.tail = node
      self.head = node
    self.count += 1

items = singly_linked_list()
items.append_item('A')
items.append_item(1)
items.append_item([1])

for val in items.iterate_item():
  print(val)