import math
import decimal
decimal.getcontext().prec = 15

z=decimal.Decimal(5).sqrt()

list=[]
i=1

def fibo(n):
	n=n+1
	y=(1/z)*(((1+z)/2)**n)-(1/z)*(((1-z)/2)**n)
	k=math.floor(y)
	print (k)
	return k

while True:
	i=i+1
	digits = len(str(fibo(i)))
	if digits  >= 1000:
		list.append(i)
		break
	else:pass



print (list)