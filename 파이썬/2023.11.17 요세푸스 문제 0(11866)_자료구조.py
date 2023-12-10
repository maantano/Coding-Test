import sys
input = sys.stdin.readline

n,m = map(int,input().split())

q  = [i  for i in range(1,n+1)]

answer = []
num = 0

for i in range(n):
	num += m -1
	if num >=len(q):
		num = num % len(q)
	answer.append(str(q.pop(num)))

print('<',', '.join(answer)[:] ,'>',sep='')

