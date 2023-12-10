import sys
input = sys.stdin.readline
from collections import Counter
n = 2
l= 4
r = 17
def solution(n, l, r):
	arr = '1'
	while True:
		if n == 0:
			break
		tmp = ''
		for i in arr:
			if i == '1':
				tmp+='11011'
			else:
				tmp+='00000'
		arr=tmp
		n-=1

	cnt = Counter(arr[l-1:r])
	print(cnt['1'])
	return cnt['1']


solution(n, l, r)
