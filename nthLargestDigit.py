'''
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
'''

def sT(m) :
  if m == 0: return 10
  if Sum(list(str(m))) >= 10: return m
  for i in range(1, 10):
    ch = check(m, i)
    if ch: return str(m) + str(i)

def check(m, i):
  if Sum(list(str(m)+str(i))) == 10: return True
  else: return False

def Sum(Il):
  Sum = 0
  for num in Il:
    Sum += int(num)
  return Sum

m = int(input())
print(sT(m))
