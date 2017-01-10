
p = []


def hamsu(n) :
	
	for i in range(1, len(a)) :
		if n[i] == n[-i] :
			if i == len(a)-1 :
				p.append(z)
			else :
				continue
		else : 
			break


for x in range(1000, 100, -1) :
	for y in range(1000, 100, -1) :
		z = x*y
		a = " %d" %(z) 
		hamsu(a)


p.sort()
print p.pop(-1) 


