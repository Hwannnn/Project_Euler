from math import sqrt

def prime_search(n) :
	global sum, b

	if dict.get(n) == None :
		for b in range(2, int(sqrt(n)+1)) :
			if n%b == 0 :
				break
			elif b == int(sqrt(n)) :
				dict_2[n] = n ; circular_num(n)
	else :
		pass

def circular_num(n) :
	global sum, dummy
	str_n = str(n)

	if len(str_a) != dummy :
		dummy += 1
		circular_n = int(str_n[1:len(str_n)]+str_n[0])
		prime_search(circular_n)
	else :
		dict.update(dict_2)

#########################################################

num = 1000000
dict = {2:2, 3:3, 5:5}
dict_2 = {}
sum = 3

for a in range(6, num+1) :
	str_a = str(a)
	dummy = 1
	dict_2.clear()
	if (str_a.count('0') + str_a.count('2') + str_a.count('4') + str_a.count('5') + str_a.count('6') + str_a.count('8')) == 0 :
		prime_search(a)

print len(dict)

