import math
import sys
input = sys.stdin.readline

# n = int(input())

# chk = [0,0]+[1]*(n+1)
# answer = []

# for i in range(2,n+1):
# 	if chk[i]:
# 		answer.append(i)
# 	for j in range(i*2,n+1,i):
# 		chk[j] = 0
# print(answer)


# ====================================================================================

m = 10
arr = [1 for _ in range(m+1)]
for i in range(2,int(math.sqrt(m))+1):
	if arr[i]:
		j = 2
		while i*j <= m:
			arr[i*j] = 0
			j+=1
for i in range(2,m+1):
	if arr[i]:
		print(i,end=' ')
