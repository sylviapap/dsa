# simplest solution and cases
# O(n) time, O(1) space

def isPalindrome(string):
  left = 0
  right = len(string) - 1
  while left < right:
		if string[left] != string[right]:
			return False
		left += 1
		right -= 1
  return True

# checking input for alphanumeric
# i.e. so "A man, a plan, a canal: Panama" returns True even with the ":"

def isPalindrome(string):
  left = 0
  right = len(string)-1
  while left < right:
    while left < right and not string[left].isalnum():
      left += 1
    while left < right and not string[right].isalnum():
      right -= 1
    if string[left].lower() != string[right].lower():
      return False
    left += 1
    right -= 1
  return True