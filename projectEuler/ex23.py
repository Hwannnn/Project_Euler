from math import sqrt

def multi(n_1) :
	for r in list :
		z = n_1 + r
		if z > 28123 :
			break
		else :
			list_2.append(z)


def divisor(n) :
	sum = 1
	for i in range(2, int(sqrt(n))+1) :
		if n%i == 0 and n/i == i :
			sum += i
		elif n%i == 0 :
			sum += (i+(n/i))
	return sum, n

#############################################################3

list = [] ; list_2 = []
sum_1 = (dummy for dummy in range(28124))
number = (dummy for dummy in range(12, 28112))

for a, b in map(divisor, number) :
	if a > b :
		list.append(b); multi(b)



print sum(sum_1) - sum(set(list_2))