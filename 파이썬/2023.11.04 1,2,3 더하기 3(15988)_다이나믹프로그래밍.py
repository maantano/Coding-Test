import sys
input = sys.stdin.readline
n = int(input())

arr = [int(input()) for _ in range(n)]

dp = [0] * 1000001
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4

for j in range(4,1000001):
	dp[j] = (dp[j-3]+dp[j-2]+dp[j-1]) %  1000000009

for a in arr:
	print(dp[a])

# import sys


# t = int(sys.stdin.readline())
# n = [int(sys.stdin.readline()) for _ in range(t)]

# dp = [0] * 1000001

# dp[1] = 1
# dp[2] = 2
# dp[3] = 4

# for i in range(4, 1000001):
# 	dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

# [print(dp[j]) for j in n]

# import sys

# n = int(input())
# arr = [0 for j in range(1000001)]
# arr[0] = 1
# arr[1] = 1
# arr[2] = 2
# for i in range(3, 1000001):
#     arr[i] = arr[i - 1] % 1000000009 + arr[i - 2] % 1000000009 + arr[i - 3] % 1000000009
# for i in range(n):
#     a = int(input())
#     print(arr[a] % 1000000009)


# 	# print(dp[chk] % 1000000009)

# # import sys


# # t = int(sys.stdin.readline())
# # n = [int(sys.stdin.readline()) for _ in range(t)]

# # dp = [0] * 1000001

# # dp[1] = 1
# # dp[2] = 2
# # dp[3] = 4

# # for i in range(4, 1000001):
# #     dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

# # [print(dp[j]) for j in n]

# # # import sys

# # # n = int(input())
# # # arr = [0 for j in range(1000001)]
# # # arr[0] = 1
# # # arr[1] = 1
# # # arr[2] = 2
# # # for i in range(3, 1000001):
# # #     arr[i] = arr[i - 1] % 1000000009 + arr[i - 2] % 1000000009 + arr[i - 3] % 1000000009
# # # for i in range(n):
# # #     a = int(input())
# # #     print(arr[a] % 1000000009)

# # # n = int(input())
# # # dp = [0] * 12
# # # dp[0] = 0
# # # dp[1] = 1
# # # dp[2] = 2
# # # dp[3] = 4
# # # for i in range(n):
# # # 	chk = int(input())
# # # 	for j in range(4,chk+1):
# # # 		dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
# # # 	print(dp[chk])
