# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
  n, m = (int(s) for s in input().split(' ')) # read a list of integers, 2 in this case
  print(f'Case #{i}: {n+m} {n*m}')