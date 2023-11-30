import sys
input = sys.stdin.readline

dp = [0] * 1001

dp[0] = 0
dp[1] = 1
dp[2] = 3
dp[3] = 6
for i in range(3,1001):
	dp[i]= i+dp[i-1]

def solution(target,dp):
	for j in range(1,1001):
		if dp[j] > target:
			break
		for k in range(1,1001):
			if dp[k] > target:
				break
			for m in range(1,1001):
				if dp[m] > target:
					break
				# 	return
				if dp[j]+dp[k]+dp[m] == target:
					return 1
	return 0
n = int(input())
arr = [int(input()) for _ in range(n)]
for target in arr:
	print(solution(target,dp))
