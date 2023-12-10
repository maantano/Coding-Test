import sys
input = sys.stdin.readline


n = int(input())
arr = []
chk = [[0]*101 for _ in range(101)]

for i in range(n):
	a,b = map(int,input().split())
	for i in range(a,a+10):
		for j in range(b,b+10):
			chk[i][j] = 1
answer = 0
for i in range(len(chk)):
	answer += sum(chk[i])
print(answer)
