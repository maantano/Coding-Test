





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

def dfs(idx,first,second):
	if idx == n:
		if len(first) != n// 2:
			return -1
		if len(second) != n// 2:
			return -1

		t1 = 0
		t2 = 0
		for i in range(n//2):
			for j in range(n//2):
				if i == j:
					continue
				t1 += arr[first[i]][first[j]]
				t2 += arr[second[i]][second[j]]
		diff = abs(t1-t2)
		return diff

	ans = -1
	t1 = dfs(idx+1,first+[idx],second)
	if ans == -1 or (t1!= -1 and ans > t1):
		ans = t1
	t2 = dfs(idx+1,first,second+[idx])
	if ans == -1 or (t2 != -1 and ans > t2):
		ans = t2
	return ans
t = int(input())
for i in range(t):
	n = int(input())
	arr = [list(map(int,input().split())) for _ in range(n)]

	print('#',i+1,' ',dfs(0,[],[]))
