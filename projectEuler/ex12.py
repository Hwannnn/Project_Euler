from math import sqrt

def count_machine(n) :
	z = 0

	for a in range(1, (int(sqrt(n))+1)) :
		if n%a == 0 :
			z += 2
	if n/sqrt(n) == sqrt(n) :
		z -= 1
	return z

###################################################

count = 500
n = 1
number = 0

while True :

	number += n

	if count_machine(number) >= count :
		print number ; break
	else :
		n+=1