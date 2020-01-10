'''
Problem Statement:>>>>
he Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < (2 power 31).

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''

#Solution:>>>

def hammingDistance(self, x: int, y: int) -> int:
        hammingDistance = 0
        x = list(bin(x)[2:])
        y = list(bin(y)[2:])
        if len(x) < len(y) or len(x) > len(y):
            i = 0
            ex = []
            gap = len(y) - len(x) if len(x) < len(y) else len(x) - len(y)
            while i < gap:
                ex.append('0')
                i += 1
            if len(x) < len(y): x = ex + x
            else: y = ex + y
        for index in range(len(x)):
            if x[index] != y[index]: hammingDistance += 1
        return hammingDistance
