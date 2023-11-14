import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
from collections import deque

n = int(input())
arr = list(map(int,input().split()))
visited = [0] * (n+1)

cnt = 1
def dfs(start):
	global cnt
	visited[start] = cnt

	for i in range(start,start+arr[start]+1):
		if not visited[i]:
			cnt+=1
			dfs(i)

dfs(0)

print(visited)


import sys

n = int(input())
jump = list(map(int, sys.stdin.readline().split()))
dp = [n + 1] * n
dp[0] = 0

for i in range(n):
	for j in range(1, jump[i] + 1):
		if i + j < n:
			dp[i + j] = min(dp[i] + 1, dp[i + j])

if dp[n - 1] == n + 1:
	print(-1)
else:
	print(dp[n - 1])


from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
	print(0)
	sys.exit()

arr = list(map(int,input().split()))
visited = [0]*n
q = deque([(0,arr[0])])

while q:
	pos,jump = q.popleft()
	for i in range(1,jump+1):
		if pos+i >= n or visited[pos+i]:
			continue
		visited[pos+i] = visited[pos]+1
		q.append((pos+i,arr[pos+i]))
print(visited[-1] if visited[-1] else -1)
