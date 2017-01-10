data = open('p22.txt')
data_1 = data.read().replace('"','').split(',')
data_1.sort()


data_2 = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,
'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}


def calculate(s) :
	d2_sum = 0

	for a in str :
		d2_sum += data_2[a]

	return d2_sum

total = 0
for str in data_1 :
	d2 = calculate(str)
	d1 = data_1.index(str) + 1
	total += (d1*d2)

print total
