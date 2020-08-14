import re
fname = input('Enter file name: ')
fh = open(fname)
lst = list()
sum = 0
for line in fh:
	num = re.findall('[0-9]+', line)
	if len(num) == 1:
		num1 = int(num[0])
		lst.append(num1)
	if len(num) == 2:
		num2 = int(num[0])
		num3 = int(num[1])
		lst.append(num2)
		lst.append(num3)
	if len(num) == 3:
		num4 = int(num[0])
		num5 = int(num[1])
		num6 = int(num[2])
		lst.append(num4)
		lst.append(num5)
		lst.append(num6)

for number in lst:
	sum = sum + number
print (sum)
