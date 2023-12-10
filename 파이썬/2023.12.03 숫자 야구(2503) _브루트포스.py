import sys
input = sys.stdin.readline


n = int(input())
answer = []
d = {}
from itertools import permutations
data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(permutations(data,3))

for i in range(n):
	tmp,s,b = map(int,input().split())
	tmp = list(str(tmp))
	rmCnt = 0
	for i in range(len(num)):
		strike = ball = 0
		i -= rmCnt
		for j in range(3):
			if num[i][j] == tmp[j]:
				strike +=1
			elif tmp[j] in num[i]:
				ball += 1
		if strike != s or ball != b:
			num.remove(num[i])
			rmCnt+=1
print(len(num))

