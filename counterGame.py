'''
(Hackerrank) -> (Bit Manipulation) -> (Counter Game):--->>>
	https://www.hackerrank.com/challenges/counter-game/problem --->> (LINK)
'''

Method -> 1:
	from collections import Counter
	# Complete the counterGame function below.
	def counterGame(n):
    	chance = 0
    	while n>1:
        	if Counter(str(bin(n))[2:])['1'] == 1: 
			'''
			instead of Counter(string(or)array literals) from collections module
			we can also use built-in dict() or HashMap in Java.
			'''
            	n = n//2
            	chance += 1
        	else:
            	actual = 0
            	number = 1
            	while number < n:
                	actual = number
                	number = number << 1
            	n = abs(n - actual)
            	chance += 1
    	if chance%2 != 0: return "Louise"
    	else: return "Richard"
