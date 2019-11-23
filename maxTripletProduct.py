'''
MAX TRIPLET PRODUCT (GREEDY APPROACH) :>>
max triplet product in an array or list:>>
example: [-10, -10, 5, 2] ===>> return 500((-10)*(-10)*5)
Note: You may assume that the size of the list or array is atleast 3.
'''

def maxProduct(l):
  n = []
  p = [] 
  if len(l) == 3:
    return(l[0] * l[1] * l[2])
  for i in range(len(l)):
    if l[i] < 0: n.append(l[i])
    if l[i] > 0: p.append(l[i])
  if len(n) <= 1 and len(p) >= 3:
    p.sort()
    return(p[len(p)-1] * p[len(p)-2] * p[len(p)-3])
  if len(n) == 1 and len(p) < 3:
    return(n[0] * p[0] * p[1])
  if len(n) > 1:
    if len(p) > 2:
      n.sort()
      nh = n[0] * n[1]
      p.sort()
      ph = p[len(p)-1] * p[len(p)-2] * p[len(p)-3]
      for i in p:
        if ph < (nh * i):
          ph = (nh * i)
      return(ph)
    elif len(p) == 2:
      n.sort()
      nh = n[0] * n[1]
      ph = 0
      for i in p:
        if ph < (nh * i):
          ph = (nh * i)
      return(ph)

l = list(map(int, input().strip().split()))
print(maxProduct(l))
