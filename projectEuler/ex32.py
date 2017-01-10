list = []
list_result = []

def hamsu(x, y, z) :
	global list, list_result
	sum = str(x) + str(y) + str(z)

	for a in range(0, len(sum)) :
		if sum[a] == '0' :
			break
		else :
			list.append(sum[a])

	if len(set(list)) == 9:
		list_result.append(z); list = []
	else :
		list = []


for a in range(1, 10) :
	for b in range(1000, 10000) :
		c = a * b
		if len(str(c)) == 4 :
			hamsu(a, b, c)
for a in range(10, 100) :
	for b in range(100, 1000) :
		c = a * b
		if len(str(c)) == 4 :
			hamsu(a, b, c)

print list_result
print sum(set(list_result))