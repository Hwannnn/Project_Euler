def fibo() :
	a, b = 0, 1

	while 1 :
		a, b = b, a+b
		yield a

for i, n in enumerate(fibo()) :
	if len(str(n)) >= 1000 :
		print (i+1) ; break