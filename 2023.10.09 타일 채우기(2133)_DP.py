# n = int(input())

# dp = [0] * (n+1)
# dp[0] = 0
# dp[1] = 1

# for i in range(1,n+1):
# 	dp[i] += dp[i-1] + dp[i-2] + 1

# print(dp[n])

n = int(input())

dp = [0]*(n+1)

if n % 2 != 0:
	print(0)
else:
	dp[2] = 3
	for i in range(4, n+1, 2):
		dp[i] = dp[i-2] * 3 + 2
		for j in range(2, i-2, 2):
			dp[i] += dp[j] * 2
	print(dp[n])

# n = int(input())

# # 앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
# d = [0] * 1001

# # 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
# d[1] = 1
# d[2] = 3
# for i in range(3, n + 1):
# 	d[i] = (d[i - 1] + (2 * d[i - 2]))% 796796

# # 계산된 결과 출력
# print(d[n])
