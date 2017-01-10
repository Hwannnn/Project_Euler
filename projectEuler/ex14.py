def calculator(n) :

	global number

	if n == 1 :
		dict_1[a] = number

	elif dict_1.get(n) == None :
		if n%2 == 0 :
			n/=2 ; number += 1 ; calculator(n)
		else :
			n = 3*n+1 ; number += 1 ; calculator(n)

	else :
		number += dict_1[n] ; dict_1[a] = number

def max_number(n) :
	global x ; global max_count
	
	if dict_1[n] > max_count :
		x = n ; max_count = dict_1[n]

#####################################################################

dict_1 = {}
x = 0 ; max_count = 0
input = 1000000

for a in range(1, input+1) :
	number = 0
	calculator(a)
	max_number(a)

print x