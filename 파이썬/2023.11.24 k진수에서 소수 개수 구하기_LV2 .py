# n = 437674
# k = 3
n = 110011
k = 10

import string
tmp = string.digits + string.ascii_lowercase

def convert(num,base):
	q,r = divmod(num,base)
	if q == 0:
		return tmp[r]
	else:
		return convert(q,base)+tmp[r]

def conv(n, k):
	s = ''
	while n:
		s += str(n%k)
		n //= k
	return s[::-1]


def prime(x):
	if x == 1:
		return False
	for i in range(2,int(x**0.5)+1):
		if x % i == 0:
			return False
	return True


def solution(n, k):
	answer = 0
	chk = convert(n,k)
	for i in chk.split('0'):
		if len(i) <=0:
			continue
		if prime(int(i)):
			answer+=1
	return answer
solution(n, k)
