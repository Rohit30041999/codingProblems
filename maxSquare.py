"""
Maximum length of a square of 1's in a matrix (Dynamic Programming):>>
example :
matrix :       1 1 0 0 1
               1 1 1 1 0
               0 1 1 1 1
               1 1 1 1 1
    if you can observe. The max square is ==>    1 1 1
                                                 1 1 1
                                                 1 1 1
    so return length of its side i.e., 3.
"""

def maxSquareLength(mat) :
  clone = mat.copy()
  maxLength = 0
  for i in range(len(mat)):
    for j in range(len(mat[0])):
      if i > 0 and  j > 0 and clone[i][j] != 0:
        minVal = min(clone[i][j-1], min(clone[i-1][j], clone[i-1][j-1]))
        clone[i][j] += minVal
        if maxLength < clone[i][j]:
          maxLength = clone[i][j]
      if (i == 0 and j > 0 and clone[i][j] == 1) or (i > 0 and j == 0 and clone[i][j] == 1):
        maxLength = clone[i][j]
  return maxLength

def main():
  matrix = []
  n, m = int(input().strip()), int(input().strip())
  for i in range(n) :
    temp = []
    for j in range(m) :
      temp.append(int(input().strip()))
    matrix.append(temp)
  print(maxSquareLength(matrix))

main()  
