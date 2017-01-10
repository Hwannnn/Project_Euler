import pyprimes

def add_test(prime_num) :
	str_prime_num = str(prime_num)

	for i in range(1, len(str_prime_num)) :
		right = pyprimes.is_prime(int(str_prime_num[0:i]))
		left = pyprimes.is_prime(int(str_prime_num[i:len(str_prime_num)]))
		if right and left:
			continue
		else :
			return

	list.append(prime_num)

############################################################################

list = []
p = pyprimes.primes()

for prime_num in p :
	if len(list) == 11 :
		break
	if prime_num > 10 : 	
		add_test(prime_num)

print list
print sum(list)