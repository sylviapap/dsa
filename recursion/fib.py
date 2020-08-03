# classic fibonacci
# 0, 1, 1, 2, 3, 5
# f(n) = f(n-1) + f(n-2)

# O(2^n) time, O(n) space
def fib(n):
  if n <= 2:
    return n - 1
  else: # when we get to this point, n must = 3, so fib(n-1)=fib(3-1)=fib(2)=2-1=1
    return fib(n-1) + fib(n-2) # and fib(n-2)=fib(1)=0, so fib(3) = 1

# using memoization
# O(n) time and space
def fib(n):
  memo = {1: 0, 2:1}
  if n in memo:
		return memo[n]
  else:
		memo[n] = fib(n-1) + fib(n-2)
		return memo[n]

# iterative
# O(n) time, but O(1) space
def fib(n):
  base = [0,1]
  counter = 3
  while counter <= n:
		nextFib = base[0] + base[1]
		base[0] = base[1]
		base[1] = nextFib
		counter += 1
  return base[1] if n>1 else base[0]