# given 2 non-empty arrays of integers, return true if 2nd is subsequence of first
# not necessarily adjacent
# but must be same order
# single number and the same 2 arrays are valid
# i.e. if arr1 = [1,2,3] both arr2 = [1] and arr2 = [1,2,3] are valid
# more examples
# arr1 = [1,2,3,4] arr2 = [1,3,4] or [2,4] valid

# O(n) time, O(1) space
# n is length of array

def isValidSubsequence1(array, sequence):
  position = 0
  for num in array:
    # need first part of conditional here or else list index out of range
    if position < len(sequence) and num == sequence[position]:
			position += 1
  return position == len(sequence)

# Maybe slightly cleaner code, using `break` out of loop

def isValidSubsequence(array, sequence):
  position = 0
  for num in array:
    if position == len(sequence):
      break
    if num == sequence[position]:
      position += 1
  return position == len(sequence)

# Using `while` instead of `for` loop

def isValidSubsequence(array, sequence):
  arrayPosition, sequencePosition = 0 , 0
  while arrayPosition < len(array) and sequencePosition < len(sequence):
		if array[arrayPosition] == sequence[sequencePosition]:
			sequencePosition += 1
		arrayPosition += 1
  return sequencePosition == len(sequence)