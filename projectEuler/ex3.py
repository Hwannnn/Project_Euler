


x = 600851475143
y = []
i = 1

while True :

	if x == 1 :
		break

	elif x%i	== 0 :
		x/=i
		y.append(i)

	i+=1

z = y.pop(-1)

print z



