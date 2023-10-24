import sys
input = sys.stdin.readline
n = int(input())

def chk(arr):
	l = 0
	r = 0
	rg = arr.count(')')
	lg = arr.count('(')
	if lg != rg:
		return 'NO'
	for i in arr:
		if i == ')':
			l -= 1
			if l <0:
				return 'NO'
		else:
			l+=1
	return 'YES'

for i in range(n):
	arr = list(map(str,input().rstrip()))
	print(chk(arr))
