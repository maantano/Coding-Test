





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

# n = int(input())

# def chk(x):
# 	for i in range(x):
# 		if arr[x] == arr[i] or abs(x-i) ==  abs(arr[x] - arr[i]):
# 			return False
# 	return True

# def dfs(x):
# 	global result
# 	if x == n:
# 		result+=1
# 	else:
# 		for i in range(n):
# 			arr[x] = i
# 			if chk(x):
# 				dfs(x+1)


# arr = [0] * n
# result = 0
# dfs(0)
# print(result)



# n = int(input())
# def chk(x):
# 	for i in range(x):
# 		if arr[x] == arr[i] or abs(x-i) == abs(arr[x]-arr[i]):
# 			return False
# 	return True

# def dfs(x):
# 	global result
# 	if x == n:
# 		result += 1
# 	else:
# 		for i in range(n):
# 			arr[x] = i
# 			if chk(x):
# 				dfs(x+1)


# arr = [0] * n
# result = 0
# dfs(0)
# print(result)

# 스타트와 링크
# n = int(input())
# arr = [list(map(int,input().split())) for _ in range(n)]

# def dfs(d,first,second):
# 	if d == n:
# 		if len(first) != n // 2:
# 			return -1
# 		if len(second) != n // 2:
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

# 	result = -1
# 	t1 = dfs(d+1,first+[d],second)
# 	if result == -1 or (t1 != -1 and result > t1):
# 		result = t1

# 	t2 = dfs(d+1,first,second+[d])
# 	if result == -1 or (t2 != -1 and result > t2):
# 		result = t2

# 	return result

# print(dfs(0,[],[]))

# import sys
# input= sys.stdin.readline

# n,k =map(int,input().split())
# r,c = map(int,input().split())
# dr =[-1,-1,-1,0,0,1,1,1]
# dc =[-1,0,1,1,-1,-1,0,1]

# move_li = [(r,c)] + [(r+dr[i],c+dc[i])  for i in range(8) if 1<=r+dr[i] <= n and 1<= c+dc[i] <= n]
# s = set()

# for i in range(k):
# 	r_i,c_i = map(int,input().split())
# 	for mr,mc in move_li:
# 		if abs(r_i-mr) == abs(c_i-mc) or mr == r_i or mc == c_i:
# 			s.add((mr,mc))
# if (r,c) in s:
# 	if len(move_li) == len(s):
# 		print('CHECKMATE')
# 	else:
# 		print('CHECK')
# else:
# 	if len(s) == len(move_li) - 1:
# 		print('STALEMATE')
# 	else:
# 		print('NONE')



# n = int(input())

# arr = [0] * n

# result = 0


# def chk(x):
# 	for i in range(x):
# 		if arr[x] == arr[i] or abs(x-i) == abs(arr[x] - arr[i]):
# 			return False
# 	return True


# def dfs(x):
# 	global result
# 	if x == n:
# 		result+=1
# 	else:

# 		for i in range(n):
# 			arr[x] = i
# 			if chk(x):
# 				dfs(x+1)

# dfs(0)
# print(result)


# 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725


# import sys
# sys.setrecursionlimit(10**6)
# n = int(sys.stdin.readline())

# graph = [[] for i in range(n+1)]

# for i in range(n-1):
# 	a, b = map(int, sys.stdin.readline().split())
# 	graph[a].append(b)
# 	graph[b].append(a)

# visited = [0]*(n+1)

# arr = []

# def dfs(s):
# 	for i in graph[s]:
# 		if visited[i] == 0:
# 			visited[i] = s
# 			dfs(i)

# dfs(1)

# for x in range(2, n+1):
# 	print(visited[x])


# 영역 구하기
# https://www.acmicpc.net/problem/2583


# from collections import deque

# m, n ,k = map(int,input().split())
# visited = [[0] * (n) for _ in range(m)]


# for _ in range(k):
# 	x1,y1,x2,y2 = map(int,input().split())

# 	for i in range(y1,y2):
# 		for j in range(x1,x2):
# 			visited[i][j] = 1


# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# answer = []
# def bfs(x,y):
# 	q = deque([(x,y)])
# 	visited[x][y] = 1
# 	ans = 1
# 	while q:
# 		y,x = q.popleft()

# 		for i in range(4):
# 			nx = dx[i] + x
# 			ny = dy[i] + y

# 			if 0<=ny <m and 0<=nx <n:
# 				if not visited[ny][nx]:
# 					q.append((ny,nx))
# 					ans+=1
# 					visited[ny][nx] = visited[y][x] + 1
# 	answer.append(ans)

# for i in range(m):
# 	for j in range(n):
# 		if not visited[i][j]:
# 			bfs(i,j)
# answer.sort()
# print(len(answer))
# print(*answer)

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(1000000)
# n = int(input())
# arr = [int(input()) for _ in range(n)]

# def chk(start,end,chk1,chk2):
# 	for i in range(start+1,end):
# 		if arr[i]> chk1 or arr[i] > chk2:
# 			return False
# 	return True
# result = 0

# for i in range(n):
# 	for j in range(i+1,n):
# 		if chk(i,j,arr[i],arr[j]):
# 			result+=1
# print(result)


# 오아시스 재결합
# https://www.acmicpc.net/problem/3015
# n = int(input())
# arr = [int(input()) for _ in range(n)]


# 괄호
# https://www.acmicpc.net/problem/9012

# n = int(input())
# for _ in range(n):
# 	s = list(input().rstrip())
# 	if len(s) %2 != 0:
# 		print('NO')
# 		continue
# 	tmp = []
# 	if s[0] == ')':
# 		print('NO')
# 		continue
# 	for i in range(len(s)):
# 		if s[i] == '(':
# 			tmp.append('(')
# 		else:
# 			if len(s) <1:
# 				break
# 			tmp.pop()
# 	if len(tmp)>0:
# 		print('NO')
# 	else:
# 		print('YES')

# import sys
# input = sys.stdin.readline

# n = int(input())
# for _ in range(n):
# 	s = input().rstrip()
# 	tmp = 0
# 	for string in s:
# 		if string =='(':
# 			tmp+=1
# 		else:
# 			tmp-=1
# 		if tmp <0:
# 			print('NO')
# 			break
# 	if tmp >0:
# 		print('NO')
# 	elif tmp == 0:
# 		print('YES')

# 스택
# https://www.acmicpc.net/problem/10828
# import sys
# input = sys.stdin.readline
# n = int(input())
# ans = []
# for _ in range(n):
# 	p = input().split()

# 	if p[0] == 'push':
# 		ans.append(p[1])
# 	elif p[0] == 'top':
# 		if len(ans) > 0:
# 			print(ans[-1])
# 		else:
# 			print(-1)
# 	elif p[0] == 'size':
# 		print(len(ans))
# 	elif p[0] == 'empty':
# 		if len(ans) == 0:
# 			print(1)
# 		else:
# 			print(0)
# 	elif p[0] =='pop':
# 		if len(ans) > 0:
# 			print(ans.pop())
# 		else:
# 			print(-1)



# 스택 수열
# https://www.acmicpc.net/problem/1874

# n = int(input())

# count = 1
# answer = []
# stack = []
# tmp = True


# for i in range(n):
# 	num = int(input())

# 	while count <= num:
# 		stack.append(count)
# 		count+=1
# 		answer.append('+')

# 	if stack[-1] == num:
# 		stack.pop()
# 		answer.append('-')
# 	else:
# 		tmp = False
# 		break


# if not tmp:
# 	print('NO')
# else:
# 	for s in answer:
# 		print(s)


# 균형잡힌 세상
# https://www.acmicpc.net/problem/4949


# while True:
# 	str = input()
# 	check = []
# 	answer = 'yes'
# 	if str == '.':
# 		break
# 	for s in str:
# 		if s=='(' or s=='[':
# 			check.append(s)
# 		elif s == ')':
# 			if not len(check):
# 				answer = 'no'
# 				break
# 			else:
# 				if check.pop(-1) != '(':
# 					answer = 'no'
# 					break
# 		elif s == ']':
# 			if not len(check):
# 				answer = 'no'
# 				break
# 			else:
# 				if check.pop() != '[':
# 					answer = 'no'
# 					break
# 		else:
# 			continue
# 	if len(check):
# 		answer = 'no'
# 	print(answer)



# 쇠막대기
# https://www.acmicpc.net/problem/10799
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(1000000)

# s = input().rstrip()

# stack = []
# cnt = 0

# for i in range(len(s)):
# 	if s[i] == '(':
# 		stack.append('(')
# 	else:
# 		if s[i-1] == '(':
# 			stack.pop()
# 			cnt+=len(stack)
# 		else:
# 			stack.pop()
# 			cnt+=1
# print(cnt)


# 적록색약
# https://www.acmicpc.net/problem/10026


# from collections import deque
# import copy
# n = int(input())

# arr = [list(input().rstrip()) for _ in range(n)]
# visited = [[0] * n for _ in range(n)]


# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# cnt = 0

# answer = []
# def bfs(x,y,chk,arr):
# 	visited[x][y] = 1
# 	q = deque([(x,y)])
# 	while q:
# 		x,y = q.popleft()
# 		for i in range(4):
# 			nx = dx[i] + x
# 			ny = dy[i] + y

# 			if 0 <= nx < n and 0<= ny < n:
# 				if not visited[nx][ny] and arr[nx][ny] == chk:
# 					q.append((nx,ny))
# 					visited[nx][ny] = 1


# for i in range(n):
# 	for j in range(n):
# 		if not visited[i][j]:
# 			if arr[i][j] == 'R':
# 				bfs(i,j,'R',arr)
# 				cnt+=1
# 			if arr[i][j] == 'B':
# 				bfs(i,j,'B',arr)
# 				cnt+=1
# 			if arr[i][j] == 'G':
# 				bfs(i,j,'G',arr)
# 				cnt+=1
# answer.append(cnt)


# def bfs2(x,y,chk,arr):
# 	visited[x][y] = 1
# 	q = deque([(x,y)])
# 	while q:
# 		x,y = q.popleft()
# 		for i in range(4):
# 			nx = dx[i] + x
# 			ny = dy[i] + y

# 			if 0 <= nx < n and 0<= ny < n:
# 				if not visited[nx][ny] and arr[nx][ny] in chk:
# 					q.append((nx,ny))
# 					visited[nx][ny] = 1



# visited = [[0] * n for _ in range(n)]
# arr2 = copy.deepcopy(arr)
# cnt2 = 0
# for i in range(n):
# 	for j in range(n):
# 		if not visited[i][j]:
# 			if arr2[i][j] == 'G' or arr2[i][j] =='R':
# 				bfs2(i,j,['R','G'],arr2)
# 				cnt2+=1
# 			else:
# 				bfs2(i,j,['B'],arr2)
# 				cnt2+=1
# answer.append(cnt2)
# print(*answer)






# https://www.acmicpc.net/problem/1935
# import sys
# n = int(input())
# string = input().rstrip()
# digit = [int(input()) for _ in range(n)]

# stack = []
# for s in string:
# 	if s.isalpha():
# 		stack.append(digit[ord(s) - 65])
# 	else:
# 		a = stack.pop()
# 		b = stack.pop()
# 		if s == '*':
# 			stack.append(a*b)
# 		if s == '+':
# 			stack.append(a+b)
# 		if s == '-':
# 			stack.append(b-a)
# 		if s == '/':
# 			tmp = b/a
# 			stack.append(tmp)

# print('{:.2f}'.format(stack[0]))


# https://www.acmicpc.net/problem/5397


# 런타임에러
# import sys
# input = sys.stdin.readline

# n = int(input())
# for _ in range(n):
# 	idx = 0
# 	string = input().rstrip()
# 	stack = []
# 	for s in string:
# 		if s == '<':
# 			if idx >0:
# 				idx-=1
# 		elif s == '>':
# 			if idx < len(stack):
# 				idx+=1
# 		elif s =='-':
# 			stack.pop(idx-1)
# 		else:
# 			stack.insert(idx,s)
# 			idx+=1
# 	print(''.join(stack))

# 정답

# t = int(input())

# for _ in range(t):
# 	list1 = []
# 	list2 = []

# 	data = input()

# 	for i in data:
# 		if i == '-':
# 			if list1:
# 				list1.pop()
# 		elif i == '<':
# 			if list1:
# 				list2.append(list1.pop())
# 		elif i == '>':
# 			if list2:
# 				list1.append(list2.pop())
# 		else:
# 			list1.append(i)
# 	list1.extend(reversed(list2))
# 	print(''.join(list1))


# 다시 풀것.
# 오큰수
# https://www.acmicpc.net/problem/17298

# n = int(input())
# arr = list(map(int,input().split()))
# NGE  = [-1] * n
# stack = [0]
# for i in range(1,n):
# 	while stack and arr[stack[-1]] < arr[i]:
# 		NGE[stack.pop()] = arr[i]
# 	stack.append(i)
# print(*NGE)


# 단어 뒤집기 2
# https://www.acmicpc.net/problem/17413
# import sys
# input = sys.stdin.readline

# string = list(input().rstrip())

# s1 = []
# s2 = []
# ans = []
# chk = True
# for s in string:

# 	if s == '<':
# 		chk = False
# 		s2.append('<')
# 	elif s == '>':
# 		chk = True
# 		s2.append('>')
# 		ans.append(''.join(s2))
# 		s2 = []
# 	else:
# 		if not chk:
# 			s2.append(s)
# 		else:
# 			if s == ' ':
# 				ans.append(''.join(reversed(s1)))
# 				s1 = []
# 			else:
# 				s1.append(s)
# if s1:
# 	ans.append(''.join(reversed(s1)))
# if s2:
# 	ans.append(''.join(s2))

# print(*ans)


# 다시
# import sys
# input = sys.stdin.readline

# string = input().rstrip()
# word_stack = []
# tag = False
# res = ''


# for s in string:
# 	if s == ' ':
# 		while word_stack:
# 			res+= word_stack.pop()
# 		res += s

# 	elif s == '<':
# 		while word_stack:
# 			res+= word_stack.pop()
# 		tag = True
# 		res += s

# 	elif s == '>':
# 		tag = False
# 		res += s
# 	elif tag:
# 		res += s
# 	else:
# 		word_stack.append(s)

# while word_stack:
#     res += word_stack.pop()
# print(res)




# import sys
# input = sys.stdin.readline

# string = input().rstrip()

# stack = []
# tag = False
# res = ''


# for s in string:
# 	if s == '<':
# 		while stack:
# 			res+=stack.pop()
# 		tag = True
# 		res+=s
# 	elif s == '>':
# 		tag = False
# 		res+=s
# 	elif s ==' ':
# 		while stack:
# 			res+=stack.pop()
# 		res+=s
# 	elif tag:
# 		res+=s
# 	else:
# 		stack.append(s)

# while stack:
# 	res+=stack.pop()
# print(res)


# https://www.acmicpc.net/problem/17298

# n = int(input())
# arr = list(map(int,input().split()))

# answer = [-1] * n
# stack = [0]
# idx = 0

# for i in range(1,n):
# 	while stack and arr[stack[-1]] < arr[i]:
# 		chk = stack.pop()
# 		answer[chk] = arr[i]
# 	stack.append(i)

# print(*answer)

# 문자열 폭발
# https://www.acmicpc.net/problem/9935

# import sys
# input = sys.stdin.readline

# string = input().rstrip()
# chk=input().rstrip()
# l = len(chk)

# stack  = [string[i] for i in range(l)]
# chkArr = []

# for i in range(l,len(string)):
# 	while ''.join(stack[-l:]) == chk:
# 		for _ in range(l):
# 			stack.pop()
# 	stack.append(string[i])

# res = ''

# if ''.join(stack[-l:]) == chk:
# 	res = ''.join(stack[:-l])
# else:
# 	res = ''.join(stack)

# if res:
# 	print(res)
# else:
# 	print('FRULA')



# 괄호 끼워넣기
# https://www.acmicpc.net/problem/11899

# marks = input().rstrip()
# stack = [marks[0]]
# cnt = 0

# for m in range(1,len(marks)):
# 	if marks[m] == ')':
# 		if stack and stack[-1] == '(':
# 			stack.pop()
# 		else:
# 			cnt+=1
# 	else:
# 		stack.append(marks[m])
# print(cnt+len(stack))

# 다시
# 후위 표기식
# https://www.acmicpc.net/problem/1918

# string = input().rstrip()
# stack = []
# ans = ''


# for s in string:
# 	if s.isalpha():
# 		ans += s
# 	else:
# 		if s == '(':
# 			stack.append(s)
# 		elif s == '*' or s == '/':
# 			while stack and (stack[-1] == '*' or stack[-1] == '/'):
# 				ans+=stack.pop()
# 			stack.append(s)
# 		elif s == '+' or s == '-':
# 			while stack and stack[-1] != '(':
# 				ans += stack.pop()
# 			stack.append(s)
# 		elif s == ')':
# 			while stack and stack[-1] != '(':
# 				ans += stack.pop()
# 			stack.pop()
# while stack:
# 	ans += stack.pop()
# print(ans)










# print('('.isalpha())
# print('*'.isalpha())

# string = input().rstrip()

# stack = []
# tmp = True
# ans = []
# alpha = []
# mark = []
# idx = 0
# res = ''
# alpha2 = []
# mark2 = []
# while idx <= len(string):
# 	if string[idx] == '(':
# 		idx+=1
# 		while string[idx] != ')':
# 			if string[idx].isalpha():
# 				alpha.append(string[idx])
# 			else:
# 				mark.append(string[idx])
# 			idx+=1
# 		res +=''.join(alpha) + ''.join(mark)
# 		alpha = []
# 		mark = []
# 	else:
# 		if string[idx].isalpha():

# 			alpha2.append(string[idx])
# 		else:
# 			mark2.append(string[idx])
# 		idx+=1
		# res +=''.join(alpha) + ''.join(mark)
		# res+= string[idx]
		# ans.append(string[idx])





# for s in string:
# 	if s == '(':
# 		while s ==''
# 		if s.isalpha():
# 			stack2.append(s)
# 		else:
# 			stack3.append(s)


# string = input().rstrip()

# for i in range(len(string)):
