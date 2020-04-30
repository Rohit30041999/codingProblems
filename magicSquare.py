/*
Problem Statement :-  (https://www.hackerrank.com/challenges/magic-square-forming/problem) --> (link to the problem description)
*/

Solution: (Method - Backtracking)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.

def isMagicSquare(I):
    return (sum([I[0], I[1], I[2]]) == sum([I[3], I[4], I[5]]) == sum([I[6], I[7], I[8]]) == sum([I[0], I[4], I[8]]) == sum([I[2], I[4], I[6]]) == sum([I[0], I[3], I[6]]) == sum([I[1], I[4], I[7]]) == sum([I[2], I[5], I[8]]) == 15)

def calculateCost(s, I):
    cost, k = 0, 0
    for i in range(len(s)):
        for j in range(len(s[i])):
            cost += abs(s[i][j] - I[k])
            k += 1 
    return cost


def getMinValue(a, v, c, n, I, s, costs):
    
    if c == n:
        if isMagicSquare(I):
            costs.append(calculateCost(s, I))
            return
        else:
            return
    
    for i in range(0, n):
        if not v[i]:
            v[i] = True
            I[c] = a[i]
            getMinValue(a, v, c+1, n, I, s, costs)
            v[i] = False
    

def formingMagicSquare(s):
    arrayOfNumbers = [1,2,3,4,5,6,7,8,9]
    visited = [False]*9
    costs = []
    getMinValue(arrayOfNumbers, visited, 0, len(arrayOfNumbers), [0]*9, s, costs)
    return min(costs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
