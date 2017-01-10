import math

def divisor(n) :
	sum = 1	
	for i in range(2, int(math.sqrt(n))+1) :
		if n%i == 0 and n/i == i :
			sum += i
		elif n%i == 0 :
			sum += (i+(n/i))
	return n, sum

#####################################################

number = (a for a in range(10001))
total = 0

for r_n, d_n in map(divisor, number) :
	if d_n > 10000 or r_n == d_n:
		pass
	elif divisor(d_n)[1] == r_n :
		total += r_n

print total
