
# n=int(input())
# array=[0]*10000
# for i in range(n):
#   array[i]=int(input())

# d=[0]*10000
# d[0]=array[0]
# d[1]=array[0]+array[1]
# d[2]=max(array[2]+array[0], array[2]+array[1], d[1])
# for i in range(3,n):
#   d[i]=max(array[i]+d[i-2], array[i]+array[i-1]+d[i-3], d[i-1])

# print(max(d))

n=int(input())
array=[0]*10000
for i in range(n):
  array[i]=int(input())

d=[0]*10000
d[0]=array[0]
d[1]=array[0]+array[1]
d[2]=max(array[2]+array[0], array[2]+array[1], d[1])
for i in range(3,n):
  d[i]=max(array[i]+d[i-2], array[i]+array[i-1]+d[i-3], d[i-1])

print(max(d))


n = int(input())
arr = [0]*10000
for i in range(n):
	arr[i] = int(int(input()))
dp = [0] * 10000

dp[0] = arr[0]
dp[1] = arr[1]+arr[0]
dp[2] = max(arr[2]+arr[1],arr[2]+arr[0],dp[1])

for i in range(3,n):
	dp[i] = max(arr[i]+dp[i-2],arr[i]+arr[i-1]+dp[i-3],dp[i-1])
print(max(dp))








# n = int(input())
# arr = [0] * n

# for i in range(n):
# 	arr[i] = int(input())

# dp = [0] * n
# dp[0] = arr[0]

# dp[1] = arr[0]+arr[1]
# dp[2] = max(arr[2]+arr[1],arr[2]+arr[0],dp[1])

# for i in range(3,n):
# 	dp[i] = max(arr[i] + dp[i-2],arr[i]+arr[i-1]+dp[i-3],dp[i-1])
# print(max(dp))












# # [6, 10, 8, 10, 13, 1]
# # 10 + 10 + 13
# # 10 + 8 + 13 + 1

