# import sys
# input = sys.stdin.readline
# from collections import deque

# t = int(input())

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y,m,d,s):
# 	visited = [[0]*9 for _ in range(9)]
# 	visited[x][y] = 1
# 	q = deque([(x,y)])
# 	tmp = 0
# 	while d > 0:
# 		x,y = q.popleft()
# 		for i in range(4):
# 			nx = dx[i] + x
# 			ny = dy[i] + y
# 			if 0<= nx < 9 and 0<= ny < 9:
# 				if not visited[nx][ny] and g[nx][ny] != -1:
# 					tmp+=g[nx][ny]
# 					q.append((nx,ny))
# 					visited[nx][ny] = 1
# 		d-=1
# 	if tmp <= m:
# 		g[x][y] = s
# 		return 1
# 	else:
# 		return 0


# for test in range(t):
# 	g = [list(map(int,input().split())) for _ in range(9)]
# 	n = int(input())
# 	p = []
# 	pq= deque(())
# 	for i in range(n):
# 		m,d,s = map(int,input().split())
# 		pq.append((m,d,s))
# 	ans = 0
# 	while pq:
# 		m,d,s = pq.popleft()
# 		flag = True
# 		for i in range(1,9):
# 			if flag:
# 				if i % 2 == 1:
# 					for j in range(1,9):
# 						if g[i][j] == 0:
# 							if bfs(i,j,m,d,s):
# 								ans+=1
# 								flag = False
# 				else:
# 					for j in range(8,-1,-1):
# 						if g[i][j] == 0:
# 							if bfs(i,j,m,d,s):
# 								ans+=1
# 								flag = False
# 			else:
# 				break
# 	if ans == 0:
# 		ans = -1
# 	print(f'#{test+1}',ans)
# #


# import sys
# input = sys.stdin.readline

# t = int(input())

# def dfs(row,y,cnt,total,visited):

# 	if cnt == 3:
# 		return total
# 	for j in range(9):
# 		visited[row][j] = 1
# 		dfs(row,j,cnt+1,total+g[row][j],visited)
# 		visited[row][j] = 0
# 		dfs(row,j,cnt,total-g[row][j],visited)




# for test in range(t):
# 	g = [list(map(int,input().split())) for _ in range(3)]
# 	visited = [[0]*9 for _ in range(9)]
# 	answer = 0
# 	for i in range(3):
# 		for j in range(9):
# 			dfs(i,j,1,g[i][j],visited)

# 촌수계산
# https://www.acmicpc.net/problem/2644

# import sys
# input = sys.stdin.readline

# n = int(input())
# tx,ty = map(int,input().split())
# m = int(input())
# g = [[] for _ in range(n+1)]

# for i in range(m):
# 	x,y = map(int,input().split())
# 	g[x].append(y)
# 	g[y].append(x)
# visited = [0]*(n+1)
# res = []

# def dfs(v,num):
# 	num+=1
# 	visited[v] = 1
# 	if v == ty:
# 		res.append(num)

# 	for i in g[v]:
# 		if not visited[i]:
# 			dfs(i,num)
# dfs(tx,0)

# if not len(res):
# 	print(-1)
# else:
# 	print(res[0]-1)


# 효율적인 해킹
# https://www.acmicpc.net/problem/1325

# n,m = map(int,input().split())

# g = [[] for _ in range(n+1)]
# res = []
# for i in range(m):
# 	x,y = map(int,input().split())
# 	g[y].append(x)


# def dfs(chk):
# 	global cnt
# 	for i in g[chk]:
# 		if not visited[i]:
# 			cnt+=1
# 			dfs(i)


# max_cnt = 0
# for i in range(1,n+1):
# 	visited = [0]*(n+1)
# 	cnt = 1
# 	dfs(i)
# 	if cnt > max_cnt:
# 		max_cnt = cnt
# 		res = [i]
# 	elif cnt == max_cnt:
# 		res.append(i)
# print(res)

# import sys
# input = sys.stdin.readline
# n, m = map(int,input().split())
# g = [[] for _ in range(n+1)]


# for i in range(m):
# 	x,y = map(int,input().split())
# 	g[y].append(x)


# def dfs(i):
# 	global cnt
# 	for chk in g[i]:
# 		if not visited[chk]:
# 			visited[chk] = 1
# 			cnt+=1
# 			dfs(chk)

# maxCnt = 0
# res = []
# for i in range(1,n+1):
# 	visited = [0] * (n+1)
# 	cnt = 1
# 	dfs(i)
# 	if cnt > maxCnt:
# 		maxCnt = cnt
# 		res = [i]
# 	elif cnt == maxCnt:
# 		res.append(i)

# print(res)

# 그림
# https://www.acmicpc.net/problem/1926

# import sys
# input = sys.stdin.readline

# from collections import deque

# n,m = map(int,input().split())

# g = [ list(map(int,input().split())) for _ in range(n)]
# visited = [[0] * m for _ in range(n)]

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y):
# 	q = deque([(x,y)])
# 	visited[x][y] = 1
# 	cnt = 1
# 	while q:
# 		x,y = q.popleft()

# 		for i in range(4):
# 			nx = dx[i] + x
# 			ny = dy[i] + y
# 			if 0<= nx <n and 0<= ny < m:
# 				if not g[nx][ny]:
# 					continue
# 				if not visited[nx][ny]:
# 					visited[nx][ny] = 1
# 					q.append((nx,ny))
# 					cnt+=1
# 	return cnt
# res = []
# for i in range(n):
# 	for j in range(m):
# 		if g[i][j] == 1 and not visited[i][j]:
# 			res.append(bfs(i,j))

# print(len(res))
# if not len(res):
# 	print(0)
# else:
# 	print(max(res))

# 숫자고르기
# https://www.acmicpc.net/problem/2668


# n = int(input())
# g = [i for i in range(1,n+1)]
# visited = [0] * (n+1)


# def dfs(arr):
# 	for v in range(1,n+1):
# 		if not visited[v] and arr not in g[v]:
# 			dfs(arr+g[v])

# 음식물 피하기
# https://www.acmicpc.net/problem/1743

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# n,m,k = map(int,input().split())

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]


# g= [[0]*(m) for _ in range(n)]
# for i in range(k):
# 	x,y = map(int,input().split())
# 	g[x-1][y-1] = 1

# cnt = 0
# def dfs(x,y):
# 	global cnt

# 	cnt += 1
# 	g[x][y] = 0

# 	for i in range(4):
# 		nx = dx[i] + x
# 		ny = dy[i] + y

# 		if 0<= nx < n and 0<=ny < m:
# 			if g[nx][ny]:
# 				dfs(nx,ny)
# ans = []
# for i in range(n):
# 	for j in range(m):
# 		if g[i][j]:
# 			dfs(i,j)
# 			ans.append(cnt)
# 			cnt = 0
# print(max(ans))


# 양
# https://www.acmicpc.net/problem/3184
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# r,c = map(int,input().split())
# g = [list(map(str,input().rstrip())) for _ in range(r)]
# visited = [[0]*c for _ in range(r)]
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# sheep = 0
# wolf = 0


# def dfs(x,y):
# 	global sheep,wolf

# 	for i in range(4):
# 		nx = dx[i] + x
# 		ny = dy[i] + y

# 		if 0<=nx<r and 0<= ny < c:
# 			if not visited[nx][ny] and g[nx][ny] != '#':
# 				visited[nx][ny] = 1
# 				if g[nx][ny] == 'v':
# 					wolf+=1
# 				elif g[nx][ny] == 'o':
# 					sheep+=1
# 				dfs(nx,ny)

# resSheep = 0
# resWolf = 0
# for i in range(r):
# 	for j in range(c):
# 		if not visited[i][j]:
# 			dfs(i,j)
# 			if sheep > wolf:
# 				resSheep += sheep
# 			else:
# 				resWolf+= wolf
# 			sheep,wolf =0,0

# print(resSheep,resWolf,sep=' ')

# 숫자고르기
# https://www.acmicpc.net/problem/2668

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# n = int(input())
# visited = [0] * (n+1)
# # g = [0]
# g = [[] for _ in range(n+1)]
# for i in range(1,n+1):
# 	g[i].append(int(input()))

# def dfs(num):
# 	if not visited[num]:
# 		visited[num] = 1
# 		for a in g[num]:
# 			tmp_up.add(num)
# 			tmp_down.add(a)
# 			if tmp_up == tmp_down:
# 				ans.extend(list(tmp_down))
# 				return
# 			dfs(a)
# 	visited[num] = False

# ans = []
# for i in range(1,n+1):
# 	visited = [0] * (n+1)
# 	tmp_up = set()
# 	tmp_down = set()
# 	dfs(i)
# ans = sorted(list(set(ans)))
# print(len(ans))
# print(ans,end='\n')

# 전쟁 - 전투
# https://www.acmicpc.net/problem/1303

# import sys
# input = sys.stdin.readline
# from collections import deque

# n,m = map(int,input().split())

# visited = [[0] * m for _ in range(n)]
# g = [list(map(str,input().rstrip())) for _ in range(n)]

# w = []
# b = []

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y,chk):
# 	cnt = 1
# 	q = deque([(x,y)])
# 	visited[x][y] = 1
# 	while q:
# 		x,y = q.popleft()
# 		for i in range(4):
# 			nx = dx[i] + x
# 			ny = dy[i] + y
# 			if nx < 0 or nx >= m or ny < 0 or ny >= n:
# 					continue
# 			# if 0<= nx < n and 0<= ny < m:
# 			if not visited[nx][ny] and g[nx][ny] == chk:
# 				q.append((nx,ny))
# 				cnt+=1
# 				visited[nx][ny] = 1

# 	return cnt ** 2
# black = 0
# white = 0
# for i in range(n):
# 	for j in range(m):
# 		if not visited[i][j]:
# 			if g[i][j] == 'B':
# 				black+= bfs(i,j,'B')
# 			else:
# 				# c = bfs(i,j,'W')
# 				white+=bfs(i,j,'W')
# 				# w.append(c**2)
# print(white , black,sep=' ')



# n = int(input())

# # 자연수 num이 주어질 때 num 보다 크거나 같은 자연수 중 다음 조건을 만족하는 가장 작은 수를 구해라
# # 1. 구하는 숫자의 자리수는 짝수여야 한다.
# # 2. 숫자가 2 * n 자리수 일때, 앞 n자리 수의 각 자릿수 곱과 뒤 n자리의 자릿수의 각 자릿수의 곱이 같아야한다.

# # 자연수 num을 매개변수로 줄때 num보다 크거나 같은 수중 조건을 만족하는 수를 구하는 함수를 만들어라


# def chk(n):
# 		s = str(n)
# 		l = len(s)
# 		if l % 2 != 0:
# 			return False
# 		h = l // 2
# 		front = 1
# 		back = 1
# 		for i in range(h):
# 			front *= int(s[i])
# 			back *= int(s[i + h])
# 		return front == back

# def solution(num):
# 	while True:
# 		if chk(num):
# 			return num
# 		num += 1

# print(solution(n))

# def add_strings(num1, num2):
# 	result = int(num1) + int(num2)
# 	return str(result)



# l = len(n)
# ans = ''
# up = 0
# for i in range(l-1,-1,-1):
# 	tmp = int(n[i]) + int(m[i]) + up
# 	if tmp > 10:
# 		up+=1
# 	else:
# 		up = 0
# 	ans+=str(int(tmp) % 10)

# print(up)
# print(ans)

# def solution():
# 	n = input().rstrip()
# 	d = {}
# 	for i in n:
# 		if i in d:
# 			d[i] += 1
# 		else:
# 			d[i] = 1
# 	d = dict(sorted(d.items(),key=lambda x: x[1], reverse=True))

# 	if 'C' in d and d['C'] >= len(n) //2:
# 		return 'C'
# 	else:
# 		if 'C' in d:
# 			d.pop('C')
# 		maxV = max(d.values())
# 		ans = ''
# 		for chk in d:
# 			if d[chk] == maxV:
# 				ans+=chk
# 			else:
# 				break
# 		return ''.join(sorted(ans))
# print(solution())


# N명의 학생이 시험을 보았습니다. 각 학생에는 1부터 N까지의 번호가 붙어있습니다. N명의 학생의 시험 점수를 바탕으로 등수를 부여하려고 합니다. 각 학생의 등수는 자신보다 높은 점수를 받은 학생의 수에 1을 더한 수입니다.예를 들어 세 학생이 있고 1,2,3번 학생의 서억이 각각 2,2,1이라면 1,2번 학생은 가장 점수가 높고 동점이기 때문에 1등이고 3번 학생은 1,2,번 학생보다 점수가 낮기 때문에 3등입니다. 1번부터 N번 학생 까지의 등수를 구하는 함수를 만들어줘

# // function solution(grade) {
# //     const n = grade.length;
# //     const ranks = new Array(n).fill(1);

# //     for (let i = 0; i < n; i++) {
# //         for (let j = 0; j < i; j++) {
# //             if (grade[i] > grade[j]) {
# //                 ranks[j]++;
# //             } else if (grade[i] < grade[j]) {
# //                 ranks[i]++;
# //             }
# //         }
# //     }
# //     return ranks;
# // }


# def calculate_ranks(scores):
# 	n = len(scores)
# 	ranks = [1] * n

# 	for i in range(n):
# 		for j in range(n):
# 			if scores[j] > scores[i]:
# 				ranks[i] += 1

# 	return ranks

# # 예시 입력
# scores = [3, 2, 1,2]
# ranks = calculate_ranks(scores)
# print(ranks)  # 출력: [1, 1, 3]


# 12시간 단위로 표시되는 시계가 있습니다.
# 오전일 경우 AM, 오후일 경우 PM으로 표시되며, 시간은 "시:분:초"로 표시됩니다.
# 예를 들어, 오전 11시 27분 35초일 경우 "AM 11:27:35"로 표시됩니다.
# 오후 8시 20분 4초일 경우 "PM 08:20:04"로 표시가 됩니다.
# 이제부터, 우리는 시계에 표시된 시간에서 N초후의 시간을 구하려고 합니다.
# 단, N초 후의 시간 표시를 12시간 단위에서 24시간 단위 표시로 변경하려고 합니다.
# 24시간 단위로 표시되므로 오전과 오후를 나타내는 "AM","PM"과 같은 문자열은 표시되지 않으며 "시:분:초"만 표시됩니다.

# 예를들어
# 1. 12시간 단위 시계로 표시된 "PM 01:00:00"에서 10초 후의 시간을 24시간 단위 표시로 변경하면 "13:00:10"으로 표시하게 됩니다.
# 2. 12시간 단위 시계로 표시된 "PM 11:59:59"에서 1초후의 시간을 24시간 단위로 변경하면 "00:00:00"으로 표시됩니다.

# 12시간 단위로 표시되는 현재 시각 P와 N이 배개변수로 주어질때, N초 후의 시간 표시를 24시간 단위 표시로 변경하는 함수를 만들어줘


def convertTimeTo24HoursFormat(p, n):
	period, time_str = p.split(' ')
	time_components = list(map(int, time_str.split(':')))
	hours, minutes, seconds = time_components

	if period == 'PM' and hours != 12:
		hours += 12
	elif period == 'AM' and hours == 12:
		hours = 0

	seconds += n
	minutes += seconds // 60
	hours += minutes // 60

	seconds %= 60
	minutes %= 60
	hours %= 24

	hours = str(hours).zfill(2)
	minutes = str(minutes).zfill(2)
	seconds = str(seconds).zfill(2)

	return f"{hours}:{minutes}:{seconds}"

print(convertTimeTo24HoursFormat("PM 11:59:59", 1))
print(convertTimeTo24HoursFormat("PM 01:00:00", 10))



# function solution(p, n) {

#     const period = p.split(' ')[0];
#     const timeComponents = p.split(' ')[1].split(':');
#     let hours = parseInt(timeComponents[0]);
#     let minutes = parseInt(timeComponents[1]);
#     let seconds = parseInt(timeComponents[2]);


#     if (period === 'PM' && hours !== 12) {
#         hours += 12;
#     } else if (period === 'AM' && hours === 12) {
#         hours = 0;
#     }

#     seconds += n;
#     minutes += Math.floor(seconds / 60);
#     hours += Math.floor(minutes / 60);

#     seconds %= 60;
#     minutes %= 60;
#     hours %= 24;

#     hours = hours < 10 ? '0' + hours : hours;
#     minutes = minutes < 10 ? '0' + minutes : minutes;
#     seconds = seconds < 10 ? '0' + seconds : seconds;

#     return hours + ':' + minutes + ':' + seconds;
# }
