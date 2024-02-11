# 1번.

# s = 'wonderful'
# ans  = []

# chk = ''
# for c in s:
# 	if len(ans) > 0 and ans[-1] == c:
# 		chk = c
# 		ans.append('*')
# 	else:
# 		if chk == c:
# 			continue
# 		ans.append(c)
# 		chk = c
# 	print(ans)
# print(''.join(ans))


# 2번.


# v = [
# 	[1, 1, 0, 1, 1],
# 	[0, 1, 1, 0, 0],
# 	[0, 0, 0, 0, 0],
# 	[1, 1, 0, 1, 1],
# 	[1, 0, 1, 1, 1],
# 	[1, 0, 1, 1, 1]
# ]

# from collections import deque

# n = len(v)
# m = len(v[0])
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# visited = [[0]*m for _ in range(n)]

# ans = 0
# def bfs(x,y,visited):
# 	q = deque([(x,y)])
# 	visited[x][y] = 1
# 	cnt = 1
# 	while q:
# 		x,y = q.popleft()

# 		for i in range(4):
# 			nx = dx[i] + x
# 			ny = dy[i] + y

# 			if 0<= nx < n and 0<= ny < m:
# 				if not visited[nx][ny] and v[nx][ny]:
# 					visited[nx][ny] = 1
# 					cnt+=1
# 					q.append((nx,ny))
# 	return cnt
# answer = []
# for i in range(n):
# 	for j in range(m):
# 		if v[i][j] and not visited[i][j]:
# 			answer.append(bfs(i,j,visited))

# print([len(answer),max(answer)])

# 사회적 거리 유지를 위해 공연 관람객들의 좌석을 배정하려 합니다. 공연장의 각 좌석은 1 x 1 크기의 정사각형 모양이며, 전체 좌석은 n x n 크기 정사각 격자 모양입니다.
# 관람객에게 좌석을 배정하는 규칙은 다음과 같습니다.
# 제일 처음 입장하는 관람객은 1행 1열 좌석을 배정받습니다.

# 두 번쨰 관람객부터는 먼저 좌석을 배정받은 다른 관람객 중 가장 가까운 관람객까지의 거리가 최대인 좌석을 배정합니다.

# 만약 그런 좌석이 여러개라면 열 번호가 가장 작은 좌석을 배정합니다.
# 만약 열 번호가 가장 작은 좌석이 여러 개라면 행 번호가 가장 작은 좌석을 배정합니다.
# 두 좌석 사이의 거리는 행 번호 차이 + 열번호 차이입니다.
# 예를 들어 [2행,3열] 과 [5행,1열] 사이의 거리는 |2-5| + |3 - 1| = 5 입니다. (||는 절대값 기호입니다.)


# 첫번째는 1.1
# 두번쨰는 1.1부터 거리 8로 5.5
# 그럼 1.1과 5.5에서부터 거리를 계산해서 5.1, 4.2, 3.3, 2.4, 1.5 지만 열 번호가 가장 작은 5.1이 세번쨰
# 그다음 1.1, 5.1, 5.5 부터 거리가 4로 3.3,2.4, 1.4 로 같지만 열번호가 가장 작은 3.3
# 그다음 1.1, 5.5, 5.1, 3.3 에서 거리가 가장 큰 1.5

# 이런식으로 가는거야

# 그럼 결과는 [[1,16,9,21,5].[14,7,19,11,24],[6,17,4,22,13,[15,8,20,12,25,[3,18.10,23,2]]
# 이 순서로 나와야 해




# 정답
# def calDist(seat, visited):
# 	row, col = seat
# 	min_dist = float('inf')
# 	for s in visited:
# 		allocated_row, allocated_col = s
# 		dist = abs(row - allocated_row) + abs(col - allocated_col)
# 		min_dist = min(min_dist, dist)
# 	return min_dist

# def backtrack(n, visited, row, col):
# 	if len(visited) == n * n:
# 		return visited

# 	min_dist = float('-inf')
# 	next_seat = None

# 	for i in range(row, n + 1):
# 		start_col = 1 if i == row else col
# 		for j in range(start_col, n + 1):
# 			seat = (i, j)
# 			if seat not in visited:
# 				cost = calDist(seat, visited)
# 				if cost > min_dist:
# 					min_dist = cost
# 					next_seat = seat

# 	if next_seat:
# 		visited.append(next_seat)
# 		result = backtrack(n, visited, row, col)
# 		if result:
# 			return result
# 		visited.pop()

# 	return None

# def find_kth_seat(n, k):
# 	visited = [(1, 1)]
# 	result = backtrack(n, visited, 1, 1)
# 	print(result)
# 	if result:
# 		return result[k - 1]
# 	else:
# 		return None

# n = 5
# k = 12
# print(find_kth_seat(n, k))


# n = 5
# k = 12

# def calDist(seat, visited):
# 	row, col = seat
# 	min_dist = int(1e9)
# 	for s in visited:
# 		allocated_row, allocated_col = s
# 		dist = abs(row - allocated_row) + abs(col - allocated_col)
# 		min_dist = min(min_dist, dist)
# 	return min_dist
# answer = []

# def chkSeats(n):
# 	global answer
# 	visited = [(1, 1)]

# 	for i in range(1, n*n):
# 		dist = -1
# 		next = [0,0]

# 		for i in range(1, n+1):
# 			for j in range(1, n+1):
# 				seat = (i, j)
# 				if seat not in visited:
# 					cost = calDist(seat, visited)
# 					if cost > dist:
# 						dist = cost
# 						next = seat
# 					elif cost == dist:
# 						if j < next[1]:
# 							next = seat
# 		answer.append(next)
# 		visited.append(next)

# 	return visited

# visited = chkSeats(n)
# print(visited[k-1])
# allocated_seats_matrix = [[0] * n for _ in range(n)]

# for i, seat in enumerate(allocated_seats):
# 	row, col = seat
# 	allocated_seats_matrix[row-1][col-1] = i + 1


# for row in allocated_seats_matrix:
# 	print(row)

# 정답.
# def calculate_distance(seat, allocated_seats):
# 	row, col = seat
# 	min_distance = float('inf')

# 	for allocated_seat in allocated_seats:
# 		allocated_row, allocated_col = allocated_seat
# 		distance = abs(row - allocated_row) + abs(col - allocated_col)
# 		min_distance = min(min_distance, distance)

# 	return min_distance
# answer = []
# def allocate_seats(n):
# 	global answer
# 	allocated_seats = [(1, 1)]  # 첫 번째 관람객은 항상 (1, 1) 좌석에 앉음

# 	for i in range(1, n*n):
# 		max_distance = -1
# 		next_seat = None

# 		for row in range(1, n+1):
# 			for col in range(1, n+1):
# 				seat = (row, col)
# 				if seat not in allocated_seats:
# 					distance = calculate_distance(seat, allocated_seats)
# 					if distance > max_distance:
# 						max_distance = distance
# 						next_seat = seat
# 					elif distance == max_distance:
# 						if col < next_seat[1]:
# 							next_seat = seat
# 		answer.append(next_seat)
# 		allocated_seats.append(next_seat)

# 	return allocated_seats

# # 예시 실행
# n = 5
# allocated_seats = allocate_seats(n)
# allocated_seats_matrix = [[0] * n for _ in range(n)]

# for i, seat in enumerate(allocated_seats):
# 	row, col = seat
# 	allocated_seats_matrix[row-1][col-1] = i + 1


# for row in allocated_seats_matrix:
# 	print(row)

# 3번

# 사회적 거리 유지를 위해 공연 관람객들의 좌석을 배정하려 합니다. 공연장의 각 좌석은 1 x 1 크기의 정사각형 모양이며, 전체 좌석은 n x n 크기 정사각 격자 모양입니다.
# 관람객에게 좌석을 배정하는 규칙은 다음과 같습니다.
# 제일 처음 입장하는 관람객은 1행 1열 좌석을 배정받습니다.

# 두 번쨰 관람객부터는 먼저 좌석을 배정받은 다른 관람객 중 가장 가까운 관람객까지의 거리가 최대인 좌석을 배정합니다.

# 만약 그런 좌석이 여러개라면 열 번호가 가장 작은 좌석을 배정합니다.
# 만약 열 번호가 가장 작은 좌석이 여러 개라면 행 번호가 가장 작은 좌석을 배정합니다.
# 두 좌석 사이의 거리는 행 번호 차이 + 열번호 차이입니다.
# 예를 들어 [2행,3열] 과 [5행,1열] 사이의 거리는 |2-5| + |3 - 1| = 5 입니다. (||는 절대값 기호입니다.)
# def find_seat(n, k):
# 	# 이미 선택된 좌석들을 저장할 집합
# 	selected_seats = set([(1, 1)])

# 	for _ in range(k - 1):
# 		max_distance = -1
# 		next_seat = None

# 		# 이미 선택된 좌석들을 순회하며 가장 먼 좌석을 선택
# 		for row in range(1, n + 1):
# 			for col in range(1, n + 1):
# 				if (row, col) not in selected_seats:
# 					min_distance_to_selected_seat = min(abs(row - r) + abs(col - c) for r, c in selected_seats)
# 					distance = abs(row - 1) + abs(col - 1)
# 					if distance >= max_distance and distance > min_distance_to_selected_seat:
# 						if distance == max_distance:
# 							if col < next_seat[1]:
# 								next_seat = (row, col)
# 						else:
# 							max_distance = distance
# 							next_seat = (row, col)

# 		# 다음 좌석 선택
# 		selected_seats.add(next_seat)

# 	return next_seat

# n = 5
# k = 12
# result = find_seat(n, k)
# print(result)  # 출력: (4, 4)



# import sys
# import heapq
# # sys.setrecursionlimit(10 ** 6)
# n = 5
# k = 12


# # for i in range(1,n+1):
# # 	for j in range(1,n+1):





# INF = int(1e9)
# g = [[] for _ in range(n+1)]
# distance = [INF] * (n+1)

# for i in range(1,n+1):
# 	for j in range(1,n+1):
# 		g[i].append((j,(abs(i-j)+abs(j-i))))

# def djikstra(start):
# 	q = []
# 	heapq.heappush(q,(0,start))
# 	distance[start] = 0

# 	while q:
# 		dist,now = heapq.heappop(q)
# 		if distance[now] < dist:
# 			continue
# 		for i in g[now]:
# 			cost = dist+i[1]
# 			if cost < distance[i[0]]:
# 				distance[i[0]] = cost
# 				heapq.heappush(q,(cost,i[0]))

# djikstra(1)
# print(distance)
# max_dist = max(distance[1:])
# print(max_dist)

# import heapq

# def calculate_distance(n, start):
# 	INF = int(1e9)
# 	distance = [INF] * (n+1)
# 	distance[start] = 0

# 	q = []
# 	heapq.heappush(q, (0, start))

# 	while q:
# 		dist, now = heapq.heappop(q)
# 		if distance[now] < dist:
# 			continue
# 		for i in g[now]:
# 			cost = dist + i[1]
# 			if cost < distance[i[0]]:
# 				distance[i[0]] = cost
# 				heapq.heappush(q, (cost, i[0]))

# 	return distance

# def allocate_seats(n):
# 	g = [[] for _ in range(n+1)]
# 	for i in range(1, n+1):
# 		for j in range(1, n+1):
# 			g[i].append((j, (abs(i-j) + abs(j-i))))

# 	allocated_seats = [(1, 1)]  # 첫 번째 관람객은 항상 (1, 1) 좌석에 앉음

# 	for _ in range(1, n*n):  # 첫 번째 좌석을 제외한 나머지 좌석에 대해 반복
# 		max_distance = -1
# 		next_seat = None

# 		# 출발 좌표(1, 1)에서의 거리를 다시 계산하여 가장 먼 좌석을 찾음
# 		distance = calculate_distance(n, 1)
# 		for i in range(1, n+1):
# 			for j in range(1, n+1):
# 				if (i, j) not in allocated_seats:
# 					if distance[j] > max_distance:
# 						max_distance = distance[j]
# 						next_seat = (i, j)
# 					elif distance[j] == max_distance:
# 						# 열 번호를 비교하여 작은 열번호를 먼저 선택
# 						if j < next_seat[1]:
# 							next_seat = (i, j)

# 		# 가장 먼 좌석을 배정 후, 이미 배정된 좌석에 추가
# 		allocated_seats.append(next_seat)

# 	return allocated_seats

# # 예시 실행
# n = 5
# allocated_seats = allocate_seats(n)
# print("Allocated Seats:")
# for seat in allocated_seats:
# 	print(seat)

# import heapq

# def calculate_distance(n):
# 	INF = int(1e9)
# 	distance = [[INF] * (n+1) for _ in range(n+1)]

# 	for i in range(1, n+1):
# 		for j in range(1, n+1):
# 			distance[i][j] = abs(1 - i) + abs(1 - j)

# 	return distance

# def allocate_seats(n):
# 	distance = calculate_distance(n)
# 	allocated_seats = [(1, 1)]  # 첫 번째 관람객은 항상 (1, 1) 좌석에 앉음
# 	occupied_seats = set([(1, 1)])  # 이미 배정된 좌석

# 	for _ in range(1, n*n):  # 첫 번째 좌석을 제외한 나머지 좌석에 대해 반복
# 		max_distance = -1
# 		next_seat = None

# 		# 이미 배정된 좌석들과의 거리를 고려하여 가장 먼 좌석을 찾음
# 		for i in range(1, n+1):
# 			for j in range(1, n+1):
# 				if (i, j) not in occupied_seats:
# 					dist = distance[i][j]
# 					if dist > max_distance:
# 						max_distance = dist
# 						next_seat = (i, j)
# 					elif dist == max_distance:
# 						# 열 번호를 비교하여 작은 열번호를 먼저 선택
# 						if j < next_seat[1]:
# 							next_seat = (i, j)

# 		# 가장 먼 좌석을 배정 후, 이미 배정된 좌석에 추가
# 		allocated_seats.append(next_seat)
# 		occupied_seats.add(next_seat)

# 	return allocated_seats

# # 예시 실행
# n = 5
# allocated_seats = allocate_seats(n)
# print("Allocated Seats:")
# for seat in allocated_seats:
# 	print(seat)




# result = [4,4]
# from collections import deque
# g =[[0]*(n+1) for _ in range(n+1)]
# visited= [[0]*(n+1) for _ in range(n+1)]
# answer =  [[1,1]]
# def bfs():
# 	q = deque([(1,1)])
# 	visited[1][1] = 1
# 	g[1][1] = 1

# 	last = 1
# 	x = 0
# 	y = 0
# 	tmpX = int(1e9)
# 	tmpY = int(1e9)
# 	chkValue = 0
# 	while q:
# 		x,y = q.popleft()
# 		for i in range(1,n+1):
# 			for j in range(1,n+1):
# 				if not visited[i][j]:
# 					if abs(x-i) + abs(y-j) > chkValue:
# 						if abs(x-i) + abs(y-j) == chkValue and tmpY > j:
# 							continue
# 						chkValue = abs(x-i) + abs(y-j)
# 						tmpX = i
# 						tmpY = j
# 		q.append((tmpX,tmpY))
# 		visited[tmpX][tmpY] = 1
# 		g[tmpX][tmpY] = last +1
# 		answer.append([tmpX,tmpY])
# 		print('tmpX,tmpY ====>',tmpX,tmpY)
# 		print('chkValue ===>',chkValue)
# bfs()
# print(answer)
# res = 0
# tmpX = 0
# tmpY = 0
# while
# for i in range(1,n+1):
# 	for j in range(1,n+1):
# 		if abs(x-i) + abs(y-j) > res:
# 			res = abs(x-i) + abs(y-j)
# 			tmpX = i
# 			tmpY = j

# visited[tmpX][tmpY] = 1
# g[tmpX][tmpY] = last+1










# import sys
# input=sys.stdin.readline

# T=int(input())

# for i in range(T):
# 	N,S=map(int,input().split())
# 	L=sorted(list(map(int,input().split()))) #정렬해야함.
# 	start=1 ; end=max(L)
# 	while start<=end:
# 		mid=(start+end)//2
# 		left=L[0] ; count=1
# 		for i in range(1,N):
# 			right=L[i]
# 			if abs(right-left)>=mid:
# 				count+=1
# 				left=L[i]
# 		if count>=S:
# 			start=mid+1
# 		else:
# 			end=mid-1
# 	print(end)




# 4번



# play_list = [2,3,1,4]
# listen_time = 3
# t = sum(play_list)

# # res = 3
# while True:
# ans = []
# def dfs(time,cnt):
# 	global ans
# 	if time >= listen_time:
# 		ans.append(cnt)
# 		return

# 	for i in range(len(play_list)):
# 		play_list[i]

# play_list = [0] +[2,3,1,4]
# listen_time = 3
# play_list = [0] +[1,2,3,4]
# listen_time = 20
# # t = sum(play_list)
# n= len(play_list)
# k = sum(play_list)
# arr = [0]+play_list
# print(arr)
# dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

# for i in range(1,n+1):
# 	for j in range(1,k+1):
# 		w  = arr[i]
# 		if listen_time <w:
# 			dp[i][j] = dp[i-1][j]
# 		else:
# 			dp[i][j] = max(arr[i]+dp[i-1][j-w], dp[i-1][j])
# print(dp)
# print(dp[n][k])
# def max_songs(play_list, listen_time):
#     n = len(play_list)
#     total_time = sum(play_list)

#     # 듣는 시간이 한 바퀴 돌 수 있는 경우
#     if listen_time >= total_time:
#         return n

#     # 다이나믹 프로그래밍을 위한 2차원 DP 배열 초기화
#     dp = [[0] * (listen_time + 1) for _ in range(n + 1)]

#     for i in range(1, n + 1):
#         for j in range(1, listen_time + 1):
#             if play_list[i - 1] <= j:
#                 dp[i][j] = max(dp[i - 1][j], 1 + dp[i][(j - play_list[i - 1]) % total_time])
#             else:
#                 dp[i][j] = dp[i - 1][j]

#     # 마지막 곡까지 반복해서 들은 횟수 중 최대값 반환
#     return max(dp[-1])

# Example usage:
# play_list = [2,3,1,4]
# listen_time = 3
# print(max_songs(play_list, listen_time))  # Output: 3

# play_list = [1,2,3,4]
# listen_time = 5
# print(max_songs(play_list, listen_time))  # Output: 4

# play_list = [1,2,3,4]
# listen_time = 20
# print(max_songs(play_list, listen_time))  # Output: 4

# def max_songs_to_listen(play_list, listen_time):
#     total_time = 0
#     song_count = 0
#     idx = 0
#     while total_time + play_list[idx] <= listen_time:
#         if total_time + play_list[idx] >= listen_time:
#             break
#         total_time += play_list[idx]
#         song_count += 1
#         idx = (idx + 1) % len(play_list)
#         if idx == 0:
#             break
#     return song_count + 1

# # 예시 케이스 테스트
# play_list1 = [2, 3, 1, 4]
# listen_time1 = 3
# print(max_songs_to_listen(play_list1, listen_time1))  # Output: 3

# play_list2 = [1, 2, 3, 4]
# listen_time2 = 5
# print(max_songs_to_listen(play_list2, listen_time2))  # Output: 4
# play_list3 = [1, 2, 3, 4]
# listen_time3 = 20
# print(max_songs_to_listen(play_list3, listen_time3))  # Output: 4

# 4
# 2 2 2
# 3 4
# 2 2 2
# 1 2
# 2 2 1
# 4 2
# 2 2 1
# 3 2

t = int(input())
for test in range(t):
	n,m,k = map(int,input().split())
	p = list(map(int,input().split()))
	p.sort()
	ok = True
	mint = min(p)
	cnt = mint // m * k

	if cnt < 1:
		ok = False
	cnt-=1
	nujuk = mint % m

	for i in range(1,n):
		cnt -=1
		if cnt < 0:
			ok = False
		tmp1 =  p[i] % m
		if tmp1 == 0:
			nujuk = 0
		else:
			nujuk += tmp1
		cnt += (abs(p[i]-p[i-1]) + nujuk) // m * k
	if ok:
		print('Possible')
	else:
		print('Impossible')


















	# # cnt = (p[0] // m) * k
	# if p[0] < m:
	# 	print('imposible')
	# 	break
	# cnt = (m * k) - 1
	# maxt = max(p)
	# nujuk = 0
	# for i in range(1,len(p)-1):
	# 	t1 = abs(p[i] - p[i-1])
	# 	t2 = abs(p[i+1]-p[i])

	# 	if t1 % m * k > 0:
	# 		cnt += t1 % m * k
	# 	else:
	# 		nujuk += t1

	# 	if cnt < 0:
	# 		print('imposible')
	# 		break
	# 	cnt-=1


	# 	cnt+=(t1+t2) // m * k


		# if cnt < 0:
		# 	print('imposible')
		# 	break
		# cnt -=1




	# for i in range(maxt+1):



	# for chk in p:


	# for i in p:
	# 	if not ((i // m) * k):
	# 		print('impossible')
	# 		break










# def max_songs(play_list, listen_time):
#     n = len(play_list)
#     total_time = sum(play_list)

#     # 듣는 시간이 한 바퀴 돌 수 있는 경우
#     if listen_time >= total_time:
#         return n

#     # 다이나믹 프로그래밍을 위한 1차원 DP 배열 초기화
#     dp = [0] * (listen_time + 1)

#     # 각 곡에 대해 DP 배열 업데이트
#     for song_time in play_list:
#         for t in range(listen_time, song_time - 1, -1):
#             dp[t] = max(dp[t], 1 + dp[t - song_time])

#     # 최대 곡의 수 반환
#     return max(dp)

# # Example usage:
# play_list = [1,2,3,4]
# listen_time = 5

# arr = [[[2,3,1,4],3],[[1,2,3,4],5],[[1,2,3,4],20]]
# for i in range(3):
#      a,b = arr[i]
#      print(max_songs(a, b))  # Output: 3

# def max_songs(play_list, listen_time):
#     n = len(play_list)
#     total_time = sum(play_list)

#     # 듣는 시간이 한 바퀴 돌 수 있는 경우
#     if listen_time >= total_time:
#         return n

#     # 다이나믹 프로그래밍을 위한 1차원 DP 배열 초기화
#     dp = [0] * (listen_time + 1)

#     # 각 곡에 대해 DP 배열 업데이트
#     for song_time in play_list:
#         for t in range(song_time, listen_time + 1):
#             dp[t] = max(dp[t], 1 + dp[t - song_time])

#     # 최대 곡의 수 반환
#     return max(dp)

# # Example usage:

# play_list = [1,2,3,4]
# listen_time = 5

# arr = [[[2,3,1,4],3],[[1,2,3,4],5],[[1,2,3,4],20]]
# for i in range(3):
#      a,b = arr[i]
#      print(max_songs(a, b))  # Output: 3



# 400점중 270점


# import sys
# input = sys.stdin.readline
# # arr = [0]+[2,3,1,4]
# # n = len(arr)-1
# arr = [0]+[1,2,3,4]
# n = len(arr)-1
# k = 20
# dp = [[0 for _ in range(k+1)] for _ in range(n+1)]


# for i in range(1,n+1):
# 	for j in range(1,k+1):
# 		v = arr[i]
# 		if j <= v:
# 			dp[i][j] = dp[i-1][j]
# 		else:
# 			dp[i][j] = max(v+dp[i-1][j-v], dp[i-1][j])
# print(arr)
# print(dp)
# print(dp[n][k])
# [0, 2, 3, 1, 4]
# [
# 	[0, 0, 0, 0, 0, 0],
# 	[0, 0, 2, 2, 2, 2],
# 	[0, 0, 2, 3, 3, 5],
# 	[0, 1, 2, 3, 4, 5]
# ]
# import sys
# input = sys.stdin.readline

# n,k = map(int,input().split())
# arr = [[0,0]] + [list(map(int,input().split())) for _ in range(n)]
# print(arr)
# dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
# print(dp)
# for i in range(1,n+1):
# 	for j in range(1,k+1):
# 		w , v = arr[i]
# 		if j <w:
# 			dp[i][j] = dp[i-1][j]
# 		else:
# 			dp[i][j] = max(v+dp[i-1][j-w], dp[i-1][j])

# print(dp[n][k])
