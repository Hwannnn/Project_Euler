
def fun(n) :
	global sum

	n_1 = str(n)
	n_2 = n_1[::-1]

	if n_1 == n_2 :
		sum += n

sum = 0

for a in range(10, 1000000) :
	bn_1 = bin(a)[2:]
	bn_2 = bn_1[::-1]

	if bn_1 == bn_2 :
		fun(a)

print sum