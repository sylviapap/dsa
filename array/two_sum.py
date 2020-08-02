# given array of nums and target int, find pair of ints that add to target
# assume only one pair
# return empty array if none

### O(n) time & space solution

def twoNumberSum(array, target):
  # make hash table of each num and its complement
  # i.e. if target is 10 and num is 3, complement is 7, pairs = {3:7}
	pairs = {}
	for num in array:
		complement = target - num # when loop gets to '-1', c = 10 - (-1) = 11
		if complement in pairs: # checks if 11 is a key in hash
			print(pairs)
			return [complement, num] 
		else:
			pairs[num] = complement
	print(pairs)
	return []

# print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
# this creates the hash: {3: 7, 5: 5, -4: 14, 8: 2, 11: -1, 1: 9}
# and returns [11, -1]

# print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 15))
# creates: {3: 12, 5: 10, -4: 19, 8: 7, 11: 4, 1: 14, -1: 16, 6: 9}
# and returns [] because there are no matches