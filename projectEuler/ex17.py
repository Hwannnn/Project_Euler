x = {'0' : '', '1':'one', '2' : 'two', '3' : 'three', '4' : 'four', '5' : 'five', '6' : 'six', '7' : 'seven', '8' : 'eight', '9' : 'nine', '10' : 'ten',
'11' : 'eleven', '12' : 'twelve', '13' : 'thirteen', '14' : 'fourteen', '15' : 'fifteen', '16' : 'sixteen', '17' : 'seventeen', '18' : 'eighteen', '19' : 'nineteen', '20' : 'twenty',
'30' : 'thirty', '40' : 'forty', '50' : 'fifty', '60' : 'sixty', '70' : 'seventy', '80' : 'eighty', '90' : 'ninety', '100' : 'hundred', '1000' : 'thousand'}

sum = 0

for i in range(1, 1001) :

	if 1 <= i <= 20	:
		sum += len(x[str(i)])
	elif 21 <= i <= 99 :
		a= len(x[str(i)[0:1]+'0'])
		b= len(x[str(i)[1:2]])
		sum += (a+b)
		
	elif 100 <= i <= 999 :
		c = len(x[str(i)[0:1]])+len(x['100'])
		
		if str(i)[1:2] == '0' :
			d = len(x[str(i)[2:3]])
			if str(i)[2:3] == '0' :
				sum += c
			else :
				sum += (c+3+d)
			
		elif str(i)[1:2] == '1' :
			e = len(x['1'+str(i)[2:3]])
			sum += (c+3+e)
		
		elif str(i)[1:2] >= '2' :
			g = len(x[str(i)[1:2]+'0'])
			h = len(x[str(i)[2:3]])
			sum += (c+3+g+h)
	else : 
		sum+=(len(x['1'])+len(x['1000']))
		
print sum