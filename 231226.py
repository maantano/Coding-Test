# #9095 1,2,3 더하기

# n = int(input())
# arr = [int(input()) for _ in range(n)]
# dp = [0] * (12)

# dp[1] = 1
# dp[2] = 2
# dp[3] = 4
# for chk in arr:
# 	for i in range(4,chk+1):
# 		dp[i] = dp[i-1]+ dp[i-2] + dp[i-3]
# for i in arr:
# 	print(dp[i])


#11726 2*n 타일링
n = int(input())
cache = [0]*1001
cache[1]=1
cache[2]=2
for i in range(3,1001):
	cache[i] = (cache[i-1]+cache[i-2])%10007

print(cache[n])
