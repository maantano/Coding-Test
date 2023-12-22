
# // 1476 날짜 계산
# e,s,m = map(int,input().split(' '))

# chkE = 1
# chkS = 1
# chkM = 1
# answer = 1

# while True:
# 	if chkE == e and chkS == s and chkM == m:
# 		print(answer)
# 		break
# 	chkE = (answer % 15) + 1
# 	chkS = (answer % 28) + 1
# 	chkM = (answer % 19) + 1
# 	answer+=1


#1436 영화감독 숌
# n = int(input())
# nth = 666
# count = 0

# while True:
# 	if '666' in str(nth):
# 		count+=1
# 	if count == n:
# 		print(nth)
# 		break
# 	nth+=1



# 14501 퇴사
# Suc
# n = int(input())
# arr = [list(map(int,input().split())) for _ in range(n)]
# dp = [0] * (n+1)

# for i in range(n-1,-1,-1):
# 	if i + arr[i][0] > n:
# 		dp[i] = dp[i+1]
# 	else:
# 		dp[i] = max(dp[i+1],arr[i][1]+dp[i+arr[i][0]])
# print(dp[0])



#  Fale
# n = int(input())
# arr = [list(map(int,input().split(' '))) for _ in range(n)]
# answer = []
# for i in range(n):
# 	idx = i
# 	tmp = 0
# 	while(True):
# 		if idx >= n:
# 			answer.append(tmp)
# 			break
# 		start,cost = arr[idx]
# 		if (idx+ start > n):
# 			answer.append(tmp)
# 			break
# 		tmp += cost
# 		idx += start
# print(answer)
# print(max(answer))



# 14889 스타트와 링크


# n = int(input())
# arr = [list(map(int,input().split(' '))) for _ in range(n)]
# print(arr)
N = 6
board = [[0, 1, 2, 3, 4, 5], [1, 0, 2, 3, 4, 5], [1, 2, 0, 3, 4, 5], [1, 2, 3, 0, 4, 5], [1, 2, 3, 4, 0, 5], [1, 2, 3, 4, 5, 0]]

# ✨ 입력
import sys
input = sys.stdin.readline
# N = int(input())
# board = [list(map(int,input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
INF = 2147000000
res = INF

# ✨ DFS
def DFS(L,idx):
	global res
	if L == N//2:
		A = 0
		B = 0
		for i in range(N):
			for j in range(N):
				if visited[i] and visited[j]:
					A += board[i][j]
				elif not visited[i] and not visited[j]:
					B +=board[i][j]
		res = min(res, abs(A-B))
		return
	for i in range(idx,N):
		if not visited[i]:
			visited[i] = True
			DFS(L+1,i+1)
			visited[i] = False

DFS(0,0)
print(res)

# start = []
# link = []
# for i in range(n):
# 	for j in range(0,n,+1):
# 		if arr[i][j] == 0:
# 			break
# 		start.append(arr[i][j]+arr[j][i])

# 	for k in range(n-1,-1,-1):
# 		if arr[i][k] == 0:
# 			break
# 		link.append(arr[i][k]+arr[k][i])
# print(start)
# print(link)





