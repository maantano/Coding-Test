n = int(input())
arr = [0]+list(map(int,input().split(' ')))+[0]

dp = [[0] * (n+1)+[0] for _ in range(n+1)]
# dp = [0] * (n+1)


# for i in range(1,n+1):
# 	dp[i][1] = arr[i]
# 	for j in range(2,n+2):
# 		dp[i][j] += dp[i][j-1] + arr[j+1]

# print(dp)
# print(max(dp))


for i in range(1,n):
	arr[i] = max(arr[i],arr[i-1]+arr[i])
print(max(arr))
