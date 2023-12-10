import sys
input = sys.stdin.readline


n = int(input())
m = int(input())

answer = []
for i in range(n,m+1):
	if i % i**0.5 == 0:
		answer.append(int(i))
if len(answer)>0:
	print(sum(answer))
	print(answer[0])
else:
	print(-1)

