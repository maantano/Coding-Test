





# https://www.acmicpc.net/problem/13305
# https://www.acmicpc.net/problem/2531
# https://www.acmicpc.net/problem/1715
# https://www.acmicpc.net/problem/3273
# https://www.acmicpc.net/problem/5397
#  https://www.acmicpc.net/problem/1158
# https://www.acmicpc.net/problem/10808
# https://www.acmicpc.net/problem/10807
# https://www.acmicpc.net/problem/13300
# https://www.acmicpc.net/problem/11328


# https://www.acmicpc.net/problem/10815
# https://www.acmicpc.net/problem/1920
# https://www.acmicpc.net/problem/10816


# https://www.acmicpc.net/problem/1697
# https://www.acmicpc.net/problem/2606
# https://www.acmicpc.net/problem/2667
# https://www.acmicpc.net/problem/11441
# https://www.acmicpc.net/problem/21921
# https://www.acmicpc.net/problem/16139



# 탑
# https://www.acmicpc.net/problem/2493


# from collections import deque

# n = int(input())
# arr = list(map(int,input().split()))
# ans = []
# visited = [0]*n
# for i in range(n-1,-1,-1):
# 	cnt = 0
# 	q = deque([(i)])
# 	while q:
# 		chk = q.popleft()
# 		while chk > 0:
# 			chk-=1
# 			if arr[chk] > arr[i]:
# 				cnt+=1
# 				q.append(chk)
# 				visited[chk] = 1
# 				break
# 		break
# 	ans.append(chk)
# print(*[i + 1 if i else 0 for i in ans][::-1])


# n = int(input())
# arr = list(map(int,input().split()))
# stack = []
# ans = [0] * n

# for i in range(n):
# 	while stack:
# 		if arr[stack[-1][0]] > arr[i]:
# 			ans[i]  = stack[-1][0] + 1
# 			break
# 		else:
# 			stack.pop()
# 	stack.append([i,arr[i]])
# print(*ans)






# 유기농 배추
# https://www.acmicpc.net/problem/1012

# from collections import deque

# t = int(input())

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y,visited,arr):
# 	q=deque([(x,y)])
# 	visited[x][y] = 1

# 	while q:
# 		x,y = q.popleft()

# 		for i in range(4):
# 			nx = dx[i] + x
# 			ny = dy[i] + y

# 			if 0<= nx < n and 0<=ny < m:
# 				if not visited[nx][ny] and arr[nx][ny]:
# 					q.append((nx,ny))
# 					visited[nx][ny] = 1

# 	return True

# for i in range(t):
# 	n,m,k = list(map(int,input().split()))
# 	arr = [[0]*m for _ in range(n)]
# 	for j in range(k):
# 		x,y = map(int,input().split())
# 		arr[x][y] = 1
# 	visited = [[0]*m for _ in range(n)]
# 	cnt= 0
# 	for i in range(n):
# 		for j in range(m):
# 			if not visited[i][j] and arr[i][j]:
# 				cnt += bfs(i,j,visited,arr)

# 	print(cnt)

# 토마토
# https://www.acmicpc.net/problem/7576

# from collections import deque

# m, n = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# queue = deque([])
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# res = 0

# for i in range(n):
# 	for j in range(m):
# 		if matrix[i][j] == 1:
# 			queue.append([i, j])

# def bfs():
# 	while queue:
# 		x, y = queue.popleft()
# 		for i in range(4):
# 			nx, ny = dx[i] + x, dy[i] + y
# 			if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
# 				matrix[nx][ny] = matrix[x][y] + 1
# 				queue.append([nx, ny])

# bfs()
# for i in matrix:
# 	for j in i:
# 		if j == 0:
# 			print(-1)
# 			exit(0)
# 	res = max(res, max(i))
# print(res - 1)


# 4012. [모의 SW 역량테스트] 요리사
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH


# t = int(input())

# def dfs(idx,first,second):
# 	if idx == n:
# 		if len(first) != n// 2:
# 			return -1
# 		if len(second) != n// 2:
# 			return -1

# 		t1 = 0
# 		t2 = 0
# 		for i in range(n//2):
# 			for j in range(n//2):
# 				if i == j:
# 					continue
# 				t1 += arr[first[i]][first[j]]
# 				t2 += arr[second[i]][second[j]]
# 		diff = abs(t1-t2)
# 		return diff

# 	ans = -1
# 	t1 = dfs(idx+1,first+[idx],second)
# 	if ans == -1 or (t1!= -1 and ans > t1):
# 		ans = t1
# 	t2 = dfs(idx+1,first,second+[idx])
# 	if ans == -1 or (t2 != -1 and ans > t2):
# 		ans = t2
# 	return ans
# t = int(input())
# for i in range(t):
# 	n = int(input())
# 	arr = [list(map(int,input().split())) for _ in range(n)]

# 	print('#',i+1,' ',dfs(0,[],[]))

# 연구소
# https://www.acmicpc.net/problem/14502

# import copy
# from collections import deque

# n,m = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(n)]

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y,arr):
# 	visited = [[0] * m for _ in range(n)]
# 	visited[x][y] = 1
# 	q = deque([(x,y)])

# 	while q:
# 		x,y = q.popleft()

# 		for i in range(4):
# 			nx = dx[i] + x
# 			ny = dy[i] + y

# 			if 0 <= nx< n and 0 <= ny < m:
# 				if not visited[nx][ny] and not arr[nx][ny]:
# 					q.append((nx,ny))
# 					visited[nx][ny] = 1
# 					arr[nx][ny] = 2

# def chk(change):
# 	tmpArr = copy.deepcopy(arr)
# 	for x,y in change:
# 		tmpArr[x][y] = 1
# 	for i in range(n):
# 		for j in range(m):
# 			if tmpArr[i][j] == 2:
# 				bfs(i,j,tmpArr)
# 	ans = 0
# 	for i in range(n):
# 		for j in range(m):
# 			if tmpArr[i][j] == 0:
# 				ans+=1
# 	return ans

# answer = -1
# from collections import deque
# q = deque([])

# for i in range(n):
# 	for j in range(m):
# 		if arr[i][j] == 0:
# 			q.append((i,j))
# 		if len(q) == 3:
# 			answer = max(answer,chk(q))
# 			q.pop()
# print(answer)



# import copy
# from collections import deque

# n,m = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(n)]

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(arr):
# 	q = deque([])
# 	for i in range(n):
# 		for j in range(m):
# 			if arr[i][j] == 2:
# 				q.append((i,j))

# 	while q:
# 		x,y = q.popleft()

# 		for i in range(4):
# 			nx = dx[i] + x
# 			ny = dy[i] + y

# 			if 0 <= nx< n and 0 <= ny < m:
# 					if not arr[nx][ny]:
# 						q.append((nx,ny))
# 						arr[nx][ny] = 2
# 	ans = 0
# 	for i in range(n):
# 		for j in range(m):
# 			if arr[i][j] == 0:
# 				ans +=1
# 	return ans

# answer = -1
# def make_wall(cnt,arr):
# 	global answer
# 	tmpArr = copy.deepcopy(arr)
# 	if cnt == 3:
# 		answer = max(answer,bfs(tmpArr))
# 		return
# 	for i in range(n):
# 		for j in range(m):
# 			if tmpArr[i][j] == 0:
# 				tmpArr[i][j] = 1
# 				make_wall(cnt+1,tmpArr)
# 				tmpArr[i][j] = 0


# make_wall(0,arr)
# print(answer)




# from collections import deque
# import copy
# import sys
# input = sys.stdin.readline

# d = [[-1,0],[1,0],[0,-1],[0,1]]

# def bfs():
# 	queue = deque()
# 	test_map = copy.deepcopy(lab_map)
# 	for i in range(n):
# 		for k in range(m):
# 			if test_map[i][k] == 2:
# 				queue.append((i,k))

# 	while queue:
# 		r,c = queue.popleft()

# 		for i in range(4):
# 			dr = r+d[i][0]
# 			dc = c+d[i][1]

# 			if (0<=dr<n) and (0<=dc<m):
# 				if test_map[dr][dc] == 0:
# 					test_map[dr][dc] =2
# 					queue.append((dr,dc))

# 	global result
# 	count = 0
# 	for i in range(n):
# 		for k in range(m):
# 			if test_map[i][k] == 0:
# 				count +=1

# 	result = max(result, count)


# def make_wall(count):
# 	if count == 3:
# 		bfs()
# 		return
# 	for i in range(n):
# 		for k in range(m):
# 			if lab_map[i][k] == 0:
# 				lab_map[i][k] = 1
# 				make_wall(count+1)
# 				lab_map[i][k] = 0


# n, m = map(int,input().split())
# lab_map = [list(map(int,input().split())) for _ in range(n)]

# result = 0
# make_wall(0)

# print(result)



# 안전 영역
# https://www.acmicpc.net/problem/2468

# from collections import deque
# import sys
# sys.setrecursionlimit(100000)

# n = int(input())

# arr = [list(map(int,input().split())) for _ in range(n)]
# chk = 0
# for i in range(n):

# 	chk = max(chk,max(arr[i]))

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y,visited):
# 	q = deque([(x,y)])
# 	visited[x][y] = 1

# 	while q:
# 		x,y = q.popleft()

# 		for i in range(4):
# 			nx = dx[i] + x
# 			ny = dy[i] + y

# 			if 0 <= nx < n and 0<= ny < n:
# 				if not visited[nx][ny]:
# 					q.append((nx,ny))
# 					visited[nx][ny] = 1


# def check(chk):
# 	visited = [[0]*n for _ in range(n)]

# 	for i in range(n):
# 		for j in range(n):
# 			if arr[i][j] <= chk:
# 				visited[i][j] = 1
# 	ans = 0
# 	for i in range(n):
# 		for j in range(n):
# 			if not visited[i][j]:
# 				bfs(i,j,visited)
# 				ans+=1

# 	return ans

# answer = -1
# for i in range(chk):
# 	answer = max(answer,check(i))

# if answer == -1:
# 	print(0)
# else:
# 	print(answer)


# 평범한 배낭
# https://www.acmicpc.net/problem/12865


# n,k = map(int,input().split())
# chk = [0]* (k+1)
# arr = []
# for i in range(n):
# 	w,v = map(int,input().split())
# 	arr.append([w,v])
# 	chk[w] = v
# arr.sort(key= lambda x : x[0])
# ans = 0
# for w,v in arr:
# 	ans = max((chk[k-w]+v),ans)
# print(ans)


# n,k = map(int,input().split())
# arr = [[0,0]] + [list(map(int,input().split())) for _ in range(n)]
# dp  = [[0 for _ in range(k+1)] for _ in range(n+1)]

# for i in range(1,n+1):
# 	for j in range(1,k+1):
# 		w,v = arr[i]
# 		if j < w:
# 			dp[i][j] = dp[i-1][j]
# 		else:
# 			dp[i][j] = max(dp[i-1][j-w] + v,dp[i-1][j])

# print(dp[n][k])



# n = int(input())
# arr = [0]*(n+1)+[[i for i in range(n+1)] for _ in range(n)]

# def chk(x):
# 	for i in range(x):
# 		if arr[x] == arr[i] or abs(arr[x] - arr[i]) == abs(x-i):
# 			return False
# 	return True

# def dfs(start):
# 	global cnt
# 	if start == n:
# 		cnt+=1
# 		# print(cnt)
# 	else:
# 		for i in range(n):
# 			row[start] = i
# 			if not chk(start):
# 				dfs(start+1)
# row = [0] * n
# cnt = 0
# dfs(0)
# print(cnt)


# def adjacent(x):
# 	for i in range(x):
# 		if row[x] == row[i] or abs(row[x] - row[i]) == x - i: # 열이 같거나 대각선이 같으면 false
# 			return False # 대각선이 같은경우는 두 좌표에서 행 - 행 = 열 - 열 이 같으면 두개는 같은 대각선상에 있다.
# 	return True

# #한줄씩 재귀하며 dfs 실행

# def dfs(x):
# 	global result
# 	if x == N:
# 		result += 1
# 	else:
# 		# 각 행에 퀸 놓기
# 		for i in range(N): # i 는 열번호 0부터 N 전까지 옮겨가면서 유망한곳 찾기
# 			row[x] = i
# 			if adjacent(x):
# 				dfs(x + 1)

# N = int(input())
# row = [0] * N
# result = 0
# dfs(0)
# print(result)

n = int(input())

def chk(x):
	for i in range(x):
		if arr[x] == arr[i] or abs(x-i) ==  abs(arr[x] - arr[i]):
			return False
	return True

def dfs(x):
	global result
	if x == n:
		result+=1
	else:
		for i in range(n):
			arr[x] = i
			if chk(x):
				dfs(x+1)


arr = [0] * n
result = 0
dfs(0)
print(result)
