import sys
input = sys.stdin.readline

n = int(input())
a1 = sorted(list(map(int,input().split())))
a2 = sorted(list(map(int,input().split())),reverse=True)

answer = 0

for i in range(n):
	answer += (a1[i] * a2[i])
print(answer)

