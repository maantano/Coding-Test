import sys
input = sys.stdin.readline

import string

tmp = string.digits+ string.ascii_lowercase

import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
	q, r = divmod(num, base)
	if q == 0 :
		return tmp[r]
	else :
		return convert(q, base) + tmp[r]




def convert_exceptAl(num,base):
	x,y = divmod(num,base)
	if x == 0:
		return tmp[y]
	else:

		if tmp[y].isalpha():
			return convert_exceptAl(x,base)
		else:
			return convert_exceptAl(x,base) + tmp[y]
# print(convert_exceptAl(1002,12))

for i in range(1000, 10000):

	#16진수
	num = i
	sixteen = 0
	while num != 0:
		sixteen += num % 16
		num //= 16

	#12진수
	num = i
	twelve = 0
	while num != 0:
		twelve += num % 12
		num //= 12

	#10진수
	num = i
	ten = 0
	while num != 0:
		ten += num % 10
		num //= 10

	if sixteen == twelve == ten:
		print(i)
