import datetime

def counting(one, two) :
	sub_date = (second_date - first_date).days

	for a in range(1, sub_date+1) :
		add = datetime.timedelta(days=a)
		count_date = first_date + add

		if (count_date.isoweekday() == 7) and  (count_date.day == 1) :
			sum += 1

##########################################################################

first_date = datetime.date(1901,1,1)
second_date = datetime.date(2000,12,31)
sum = 0

counting(first_date, second_date)

print sum