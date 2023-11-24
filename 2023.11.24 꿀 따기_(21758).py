import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int,input().split()))
target = sum(m[:])
answer = 0
tmp = m[0]

for i in range(1,n):
	tmp += m[i]
	answer  = max(answer,target-m[0]+target-tmp-m[i])

m.reverse()
tmp = m[0]
for i in range(1,n):
	tmp += m[i]
	answer = max(answer,target-m[0]+target-tmp-m[i])


for i in range(1,n):
	answer = max(answer,target-m[0]-m[-1]+m[i])

print(answer)
