from numpy import *

matrix1 = array([1,2,5,10,20,50,100,200])

p200=0
count=0
for p100 in range(0,3):
	for p50 in range(0,5-p100*2):
		for p20 in range(0,11-(p100*5+p50*2)):
			for p10 in range(0,21-(p100*10+p50*5+p20*2)):
				for p5 in range(0,41-(p100*20+p50*10+p20*4+p10*2)):
					for p2 in range(0,101-(p100*50+p50*25+p20*10+p10*5+p5*2)):
						for p1 in range(0,201-(p100*100+p50*50+p20*20+p10*10+p5*5+p2*2)):
							matrix2 = array([p1,p2,p5,p10,p20,p50,p100,p200])
							total=sum(matrix1*matrix2)
							if(total==200):
								count +=1

print (count+1)