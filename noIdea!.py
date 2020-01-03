'''
(Hackerrank) --> (python) --> (sets) --> (NoIdea!): -->
https://www.hackerrank.com/challenges/no-idea/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen --->> (link)
'''

from bisect import bisect_left, bisect_right

def getHappiness(N, A, B):
    happy = 0
    sad = 0
    N = [int(N[index]) for index in range(len(N))]
    A = [int(A[index]) for index in range(len(A))]
    A.sort()
	'''
	.sort() takes O(nlogn) time complexity in python.
	'''
    B = [int(B[index]) for index in range(len(B))]
    B.sort()
    for number in N:
        if bisect_left(A, number) != len(A) and A[bisect_left(A, number)] == number:
		'''
		bisect_left and bisect_right from bisect module takes O(logn) time complexity to search a particular number in python.
		'''
            happy += 1
        if bisect_left(B, number) != len(B) and B[bisect_left(B, number)] == number: 
            sad += 1
    '''
	*) above for loop takes O(nlogn) time complexity O(n) ==> for passing N array and 
	O(logn) ==> for searching the number using bisect(binary search).
	*) therefore, total time complexity = O(nlogn + nlogn + nlogn) => O(3nlogn) => O(nlogn)
	'''
    return happy - sad


def main():
    input1 = input().strip().split()
    n = int(input1[0])
    m = int(input1[1])
    nArr = input().strip().split()
    mA = input().strip().split()
    mB = input().strip().split()
    print(getHappiness(nArr, mA, mB))

main()
