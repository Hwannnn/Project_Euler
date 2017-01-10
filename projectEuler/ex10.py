from math import sqrt

x = 5

for r in range(5, 2000001) :
	for i in range(2, int(sqrt(r)+1)) :
		if r%i == 0 :
			break
		if i == int(sqrt(r)) :
			x += r

print x