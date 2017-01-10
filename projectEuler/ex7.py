from math import sqrt

x= 3 ; 	n = 3
dict = {1 : 2, 2 : 3}

while True :

	for a in range(2, (int(sqrt(x))+1)) :
		if x%a == 0 :
			break
		if a == int(sqrt(x)) :
			dict[n] = x ; n += 1

	if len(dict) == 10001 :
		break

	x += 1

print dict[10001]