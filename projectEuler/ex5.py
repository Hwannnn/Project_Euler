i = 2520

list_1 = [7, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20]

while True :
	global r

	for r in list_1 :
		if i%r == 0 :
			continue
		else :
			break

	if r == 20 :
		break

	i+=1

print i
