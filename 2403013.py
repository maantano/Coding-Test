
# 1, 2, 3 더하기 3
# https://www.acmicpc.net/problem/15988


# t = int(input())
# dp = [0]*1000001
# dp[1] = 1
# dp[2] = 2
# dp[3] = 4
# for i in range(4,1000001):
# 	dp[i] = (dp[i-1]+dp[i-2]+dp[i-3])%1000000009


# for i in range(t):
# 	chk = int(input())
# 	print(dp[chk])

# 극장 좌석
# https://www.acmicpc.net/problem/2302


# import sys
# input = sys.stdin.readline
# n = int(input())
# m = int(input())
# arr = [int(input()) for _ in range(m)]

# dp = [0]* (n+1)
# dp[0] = 1
# dp[1] = 1
# dp[2] = 2

# for i in range(3,n+1):
# 	dp[i] = dp[i-1]+dp[i-2]

# answer = 1
# if m > 0:
# 	pre = 0
# 	for j in range(m):
# 		answer *= dp[arr[j] - 1 - pre]
# 		pre = arr[j]
# 	answer *= dp[n-pre]
# else:
# 	answer = dp[n]
# print(answer)


# N = int(input())
# M = int(input())

# default = list(int(input()) for _ in range(M))

# dp = [[0]*2 for _ in range(N+1)]

# dp[1][0] = 1
# dp[1][1] = 0


# for d in default:
# 	dp[d][1] = -1

# for i in range(2, N+1):
# 	if dp[i][1] == -1:
# 		if dp[i-1][1] != -1:
# 			dp[i][0] = dp[i-1][0] + dp[i-1][1]
# 			dp[i][1] = -1
# 		else:
# 			dp[i][0] = dp[i - 1][0]
# 			dp[i][1] = -1
# 	else:
# 		if dp[i-1][1] != -1:
# 			dp[i][0] = dp[i-1][0] + dp[i-1][1]
# 			dp[i][1] = dp[i-1][0]
# 		else:
# 			dp[i][0] = dp[i-1][0]
# 			dp[i][1] = 0

# if dp[N][1] == -1:
# 	print(dp[N][0])
# else:
# 	print(dp[N][0]+dp[N][1])

# 암호코드
# https://www.acmicpc.net/problem/2011

# n = list(map(int, input()))
# l = len(n)

# if n[0] == 0:
# 	print(0)
# 	exit()
# else:
# 	n = [0] + n

# 	dp = [0] * (l+1)
# 	dp[0] = 1
# 	dp[1] = 1

# 	for i in range(2, l+1):
# 		if n[i] > 0:
# 			dp[i] += dp[i-1]
# 		if 10<= (n[i-1]*10 + n[i]) <= 26:
# 			dp[i] += dp[i-2]

# 	print(dp[l] % 1000000)

# 연속합 2
# https://www.acmicpc.net/problem/13398

# n = int(input())
# arr =list(map(int,input().split()))
# dp = [[0]*n for _ in range(2)]
# dp[0][0] = arr[0]
# ans = arr[0]

# for i in range(1,n):
# 	dp[0][i] = max(dp[0][i-1] + arr[i],arr[i])
# 	dp[1][i] = max(dp[1][i-1]+arr[i],dp[0][i-1])
# 	ans = max(ans,dp[0][i],dp[1][i])
# print(ans)

# 팰린드롬 만들기
# https://www.acmicpc.net/problem/1213


# chk = input().rstrip()
# if len(chk) == 0:
# 	print("I'm Sorry Hansoo")
# 	exit()
# d = {}
# for i in chk:
# 	if i in d:
# 		d[i] += 1
# 	else:
# 		d[i] = 1

# arr1 = []
# arr2 = []
# tmp = []
# for k,v in d.items():
# 	arr1.append(k*(v//2))
# 	arr2.append(k*(v//2))

# 	if v % 2 == 1:
# 		tmp.append(k)
# chk = True
# if len(tmp) >1:
# 	chk = False

# arr1.sort()
# tmp += reversed(sorted(arr2))
# arr1 += tmp
# if not chk:
# 	print("I'm Sorry Hansoo")
# else:
# 	print(''.join(arr1))


# 카드 합체 놀이
# https://www.acmicpc.net/problem/15903

# n,m = map(int,input().split())
# arr = list(map(int,input().split()))
# dp = [0]*(n+1)
# while m>0:
# 	arr.sort()
# 	tmp = arr[0]+ arr[1]
# 	arr[0] = arr[1]=tmp
# 	m-=1
# print(sum(arr))

# import heapq

# n,m = map(int,input().split())
# arr = list(map(int,input().split()))
# heapq.heapify(arr)

# for i in range(m):
# 	a = heapq.heappop(arr)
# 	b = heapq.heappop(arr)
# 	heapq.heappush(arr,a+b)
# 	heapq.heappush(arr,a+b)
# print(sum(arr))


# 주식
# https://www.acmicpc.net/problem/11501

# t = int(input())
# for _ in range(t):
# 	n = int(input())
# 	p = list(map(int,input().split()))

# 	m = 0
# 	mp = 0

# 	for i in range(len(p)-1,-1,-1):
# 		if p[i] > mp:
# 			mp = p[i]
# 		else:
# 			m += mp - p[i]
# 	print(m)
# # ans = 0
# n = int(input())
# arr = list(map(int,input().split()))
# dp1  = [[0] for _ in range(n)]
# dp1[0][0] = -arr[0]
# cnt = 1
# ans = -int(1e9)
# for i in range(1,n):
# 	if dp1[i-1][0] < 0:
# 		ans = max(cnt*(arr[i] - dp1[i-1][0]),0)

# 	else:
# 		ans = max(cnt*(dp1[i-1][0]-arr[i]) ,0)
# 	dp1[i][0] = dp1[i-1][0] - arr[i]
# 	cnt+=1
# print(dp1)
# print(ans)

# 1학년
# https://acmicpc.net/problem/5557

# n = int(input())
# arr = list(map(int,input().split()))
# dp = [[0]*21 for _ in range(n)]

# dp[0][arr[0]] = 1

# for i in range(1,n-1):
# 	for j in range(21):
# 		if 0<= j+arr[i] <= 20:
# 			dp[i][j+arr[i]] += dp[i-1][j]
# 		if 0<= j-arr[i] <= 20:
# 			dp[i][j-arr[i]] += dp[i-1][j]
# print(dp[n-2][arr[-1]])


# 기타리스트
# https://www.acmicpc.net/problem/1495

# n,s,m = map(int,input().split())
# arr = list(map(int,input().split()))
# dp = [[0]*(m+1) for _ in range(n+1)]
# dp[0][s] = 1

# for i in range(n):
# 	for j in range(m+1):
# 		if dp[i][j]:
# 			if 0<=arr[i]+j <=m:
# 				dp[i+1][j+arr[i]] = 1
# 			if 0<= j-arr[i]<=m:
# 				dp[i+1][j-arr[i]] = 1
# ans = -1
# for i in range(m,-1,-1):
# 	if dp[n][i]==1:
# 		ans = i
# 		break
# print(ans)

# 퇴사 2
# https://www.acmicpc.net/problem/15486


# n = int(input())
# arr = [list(map(int,input().split())) for _ in range(n)]
# dp = [[0]*(n) for _ in range(n)]

# for i in range(n):
# 	dp[i][i] = arr[i][1]
# 	for j in range(i + arr[i][0],n):
# 		if arr[j][0]+j+1 > n:
# 			dp[i][i] = 0
# 			continue
# 		dp[i][j] = max(dp[i][j],arr[j][1]+dp[i][arr[j][1]])
# print(dp)


# n = int(input())
# dp = [0] * (n+1)

# for i in range(1,n+1):
# 	t,p = map(int,input().split())
# 	dp[i] = max(dp[i-1],dp[i])
# 	if i + t <= n+1:
# 		dp[i+t-1] = max(dp[i-1]+p,dp[i+t-1])
# print(dp[-1])

# import sys
# input = sys.stdin.readline
# n = int(input())
# dp  = [0] * (n+1)

# for i in range(1,n+1):
# 	t,p = map(int,input().split())
# 	dp[i] = max(dp[i-1],dp[i])
# 	if i+t-1 <= n:
# 		dp[i+t-1] = max(dp[i+t-1],dp[i-1]+p)
# print(dp[-1])


# 떡 먹는 호랑이
# https://www.acmicpc.net/problem/2502
# import sys
# input = sys.stdin.readline
# d,k = map(int,input().split())
# dp = [0]*(d)
# dp[0],dp[1] = 1,1
# while True:
# 	for i in range(2,d):
# 		dp[i] = dp[i-1]+dp[i-2]
# 	if dp[d-1] == k:
# 		print(dp[0],dp[1],sep='\n')
# 		break
# 	elif dp[-1] > k:
# 		dp[0] +=1
# 		dp[1] = dp[0]
# 	else:
# 		dp[1] += 1





# import sys
# input = sys.stdin.readline
# d,k = map(int,input().split())
# dp = [0] * d
# dp[0],dp[1] = 1,1

# while True:
# 	for i in range(2,d):
# 		dp[i] = dp[i-1]+dp[i-2]
# 	if dp[d-1] == k:
# 		print(dp[0],dp[1],sep='\n')
# 		break
# 	elif dp[-1] > k:
# 		dp[0]+=1
# 		dp[1] = dp[0]
# 	else:
# 		dp[1] +=1

# 자두나무
# https://www.acmicpc.net/problem/2240


