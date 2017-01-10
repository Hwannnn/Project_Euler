dict = {}

for a in range(1, 996) :
	for b in range(1, 998) :
		c = 1000 - a - b
		if a**2 + b **2 == c**2 :
			dict[c] = a*b*c
print dict