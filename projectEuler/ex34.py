from math import factorial

############################################

def tunnel(n) :
	n = str(n)
	count = n.count('9')

	if count >= 3 and len(n) == 7 :
		calculator(n)
	elif count >= 1 and len(n) == 6 :
		calculator(n)
	elif count == 0 and len(n) <= 6:
		calculator(n)

def calculator(n) :
	global sum

	for a in range(0, len(n)) :
		sum += factorial(int(n[a]))

###########################################

dict_factorial = {0:0}

for a in range(1, 10) :
	dict_factorial[a] = factorial(a)

###########################################

max_number = dict_factorial[9]*7

sum = 0
total = 0

for a in range(3, max_number+1) :
	tunnel(a)
	if a == sum :
		total += a ; sum = 0
	else :
		sum = 0

print total