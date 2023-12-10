import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
	n = int(input())
	arr = list(map(int,input().split()))
	dp=[0]*(n+1)
	for i in range(n):
		dp[i] = max(arr[i],arr[i]+dp[i-1])
	print(max(dp[:n]))


