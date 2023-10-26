import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int,input().split(' ')))

d = {}
m = int(input())
arr2 = list(map(int,input().split(' ')))

for i in arr:
	if i in d:
		d[i] +=1
	else:
		d[i] = 1
for j in arr2:
	if j in d:
		print(d[j], end =' ')
	else:
		print(0, end = ' ')
