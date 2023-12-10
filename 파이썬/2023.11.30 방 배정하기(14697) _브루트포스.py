import sys
input = sys.stdin.readlin

a, b, c, n = map(int, input().split())
res = 0

for i in range(0, n+1, a):
	for j in range(0, n-i+1, b):
		for k in range(0, n-i-j+1, c):
			if i+j+k == n:
				res = 1
print(res)


a, b, c, n = map(int, input().split())
li = [a, b, c]
dp = [0]*(n+1)
dp[0] = 1
for i in range(1, n+1):
	for t in li:
		if i-t >= 0 and dp[i-t]:
			dp[i] = 1
print(dp[n])
