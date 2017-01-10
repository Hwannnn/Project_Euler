r = [] ; t = [] ; rt  = 1 ; tt = 1

def hamsu(n) :
	global rt ; global tt
	for a in range(0,2) : 
		for b in range(0,2) :
		
			if str(y)[b] != '0' :
				z2 = float(str(x)[a]) / float(str(y)[b])
				j = 1-a ; k = 1-b
				if (z1 == z2) and (str(x)[j] == str(y)[k]) :
					r.append(x); t.append(y) 
	
	if x == 98 and y == 99 :
		for a in range(0,len(r)) :
			rt*=r[a]
		for b in range(0,len(t)) :
			tt*=t[b]
		for c in range(rt, 2, -1) :
			if rt%c == 0 and tt%c == 0 :
				rt /= c ; tt /= c
				
for x in range(10,99) :
	for y in range (x+1, 100) :
		z1 = float(x) / y 
		
		if str(x)[1] == '0' and str(y)[1] == '0' :
			continue
		else : 
			hamsu(z1)

print r ; print t ; print rt ; print tt
