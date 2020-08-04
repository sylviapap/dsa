# Binary Search
# Takes a sorted array of integers and target integer
# Use standard Binary Search Algorithm to return index of target in array, or -1 if not found
# Binary Search uses a midpoint/pivot

# O(log(n)) time, O(1) space
def binarySearch(array, target):
  left = 0
  right = len(array) - 1
  while left <= right:
		pivot = (left + right) // 2
		if array[pivot] == target:
			return pivot
		if target < array[pivot]:
			right = pivot - 1
		else:
			left = pivot + 1
  return -1

# Example
# array = [0,1,21,33,45,45,50,60,70,71,73], target = [33]
# len(array) = 11, right = 10, pivot = array[5] = 45
# target < 45, so right = 9, pivot = array[4] = 45
# repeat again, get pivot = array[3] = 33 == target
# return 3

# Note
# This is the "iterative" solution, which gives O(1) space
# Using while loop
# Another option is also O(log(n)) time, but also O(log(n)) space, not using iterative