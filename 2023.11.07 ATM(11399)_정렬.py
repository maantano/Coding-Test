import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
tmp = 0
answer = []
for i in arr:
	tmp +=i
	answer.append(tmp)
print(sum(answer))


