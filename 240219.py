# 숫자 카드
# https://www.acmicpc.net/problem/10815
# n = int(input())
# sang = sorted(map(int,input().split()))
# m = int(input())
# chk = map(int,input().split())

# for c in chk:
# 	start = 0
# 	end = n-1
# 	ok = False
# 	while start <= end:
# 		mid = (start+end) // 2
# 		if c == sang[mid]:
# 			ok = True
# 			break
# 		if c > sang[mid]:
# 			start = mid+ 1
# 		elif c < sang[mid]:
# 			end = mid -1
# 	print(1 if ok else 0,end = ' ')



# 수 찾기
# https://www.acmicpc.net/problem/1920

# n = int(input())
# arr = sorted(list(map(int,input().split())))
# m = int(input())
# chks = list(map(int,input().split()))

# for chk in chks:
# 	ok = False
# 	start,end = 0,n-1
# 	while start <= end:
# 		mid = (start+end) // 2

# 		if arr[mid] == chk:
# 			ok = True
# 			break
# 		if arr[mid] > chk:
# 			end = mid -1
# 		elif arr[mid] < chk:
# 			start = mid + 1

# 	print(1 if ok else 0)

# 숫자 카드 2
# https://www.acmicpc.net/problem/10816

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# n = int(input())
# arr = list(map(int,input().split()))
# m = int(input())
# chks = list(map(int,input().split()))
# # [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
# # print(arr)

# d = {}
# for i in arr:
# 	if i in d:
# 		d[i] += 1
# 	else:
# 		d[i] = 1
# print(' '.join(str(d[chk]) if chk in d else '0' for chk in chks))



# n = int(input())
# arr = sorted(list(map(int,input().split())))
# m = int(input())
# chks = list(map(int,input().split()))


# def bin(chk,arr,start,end):
# 	if start > end:
# 		return 0

# 	mid = (start+end) // 2
# 	if chk == arr[mid]:
# 		return arr[start:end+1].count(chk)
# 	if chk < arr[mid]:
# 		return bin(chk,arr,start,mid-1)
# 	elif chk > arr[mid]:
# 		return bin(chk,arr,mid+1,end)

# d = {}

# for i in chks:
# 	if i not in d:
# 		d[i] = bin(i,arr,0,n-1)

# print(' '.join(str(d[chk]) if chk in d else 0 for chk in chks ))



# 나무 자르기
# https://www.acmicpc.net/problem/2805

# n,m = map(int,input().split())
# tree = sorted(list(map(int,input().split())))
# start,end = 1,max(tree)
# while start <= end:
# 	mid = (start+end) // 2
# 	total = 0
# 	for i in tree:
# 		if i >= mid:
# 			total += i-mid
# 	if total >= m:
# 		start = mid+1
# 	else:
# 		end = mid - 1
# print(end)



# 랜선 자르기
# https://www.acmicpc.net/problem/1654

# k,n = map(int,input().split())
# line = [int(input()) for _ in range(k)]

# start,end = 1,max(line)

# while start<=end:
# 	mid = (start+end) // 2
# 	l = 0
# 	for i in line:
# 		l += i //mid
# 	if l >= n:
# 		start = mid+1
# 	else:
# 		end = mid-1
# print(end)


# 예산
# https://www.acmicpc.net/problem/2512

# n = int(input())
# arr = sorted(list(map(int,input().split())))
# total = int(input())

# start,end = 0,max(arr)

# while start<=end:
# 	mid = (start+end) // 2
# 	limit = 0
# 	for i in arr:
# 		if i < mid:
# 			limit+=i
# 		else:
# 			limit += mid

# 	if limit <= total:
# 		start = mid + 1
# 	else:
# 		end = mid - 1

# print(end)


# 게임
# https://www.acmicpc.net/problem/1072


# x,y = map(int,input().split())
# z = (100*y) // x

# left = 0
# right = x
# res = x

# if z >= 99:
# 	print(-1)

# else:
# 	while left <= right:
# 		mid = (left+right) // 2
# 		if (100*(y+mid)) // (x+mid) > z:
# 			res = mid
# 			right = mid-1
# 		else:
# 			left = mid + 1
# 	print(res)

# 기타 레슨
# https://www.acmicpc.net/problem/2343

# n,m = map(int,input().split())
# arr = list(map(int,input().split()))
# start = max(arr)
# end = sum(arr)
# while start <= end:
# 	mid = (start+end) // 2
# 	total = 0
# 	count = 1
# 	for t in arr:
# 		if total + t > mid:
# 			count += 1
# 			total = 0
# 		total += t
# 	if count <= m:
# 		ans = mid
# 		end = mid - 1
# 	else:
# 		start = mid +1
# print(ans)

# 용액
# https://www.acmicpc.net/problem/2467


# n = int(input())
# arr = list(map(int,input().split()))

# start = 0
# end = n-1
# s = abs(arr[start]+arr[end])
# ansS = 0
# ansE = n-1

# while start < end:
# 	mid = arr[start]+arr[end]

# 	if abs(mid) <= s:
# 		s = abs(mid)
# 		ansS = start
# 		ansE = end
# 		if s == 0:
# 			break
# 	if mid < 0:
# 		start += 1
# 	else:
# 		end -= 1
# print(arr[ansS],arr[ansE])



# n = int(input())
# arr = list(map(int,input().split()))

# ans = float("INF")
# ansS = 0
# ansE = 0

# for i in range(n-1):
# 	cur = arr[i]
# 	start = i+1
# 	end = n-1

# 	while start <= end:
# 		mid = (start+end) // 2
# 		tmp = cur + arr[mid]

# 		if abs(tmp) < ans:
# 			ans = abs(tmp)
# 			ansS = i
# 			ansE = mid

# 			if tmp == 0:
# 				break
# 		if tmp < 0:
# 			start = mid +1
# 		else:
# 			end = mid -1

# print(arr[ansS],arr[ansE])


# 이해 안됨
# 개똥벌레
# https://www.acmicpc.net/problem/3020

# n,h = map(int,input().split())

# down = [0] * (h+1)
# up = [0] * (h+1)

# min_cnt = n
# range_cnt = 0

# for i in range(n):
# 	if i % 2 == 0:
# 		down[int(input())] += 1
# 	else:
# 		up[int(input())] += 1

# for i in range(h-1,0,-1):
# 	down[i] += down[i+1]
# 	up[i] += up[i+1]

# for i in range(1,h+1):
# 	if min_cnt > (down[i] + up[h-i+1]):
# 		min_cnt = (down[i] +  up[h-i+1])
# 		range_cnt = 1
# 	elif min_cnt == (down[i] + up[h - i + 1]):
# 		range_cnt += 1
# print(min_cnt,range_cnt)

# 좋다
# https://www.acmicpc.net/problem/1253

# n = int(input())
# arr = sorted(list(map(int,input().split())))
# cnt = 0

# start = 0
# end = n-1
# ans = []

# for i in range(n):
# 	cur = arr[i]
# 	start = 0
# 	end = n-1

# 	while start < end:
# 		tmp = arr[start] + arr[end]
# 		if tmp == cur:
# 			if start == i:
# 				start+=1
# 			elif end == i:
# 				end -=1
# 			else:
# 				cnt+=1
# 				break
# 		elif tmp > cur:
# 			end -=1
# 		else:
# 			start += 1
# print(cnt)

# 시간 초과
# import sys
# input = sys.stdin.readline
# def chk(n):
# 	for i in range(2,int(n**0.5)+1):
# 		if n % i == 0:
# 			return False
# 	return True

# def chk2(n):
# 	idx = len(str(n)) // 2
# 	if len(str(n)) % 2 ==0:
# 		if str(n)[:idx] == str(n)[idx:][::-1]:
# 			return True
# 		else:
# 			return False
# 	else:
# 		if str(n)[:idx] == str(n)[idx+1:][::-1]:
# 			return True
# 		else:
# 			return False

# def chk3(n):
# 	if str(n)  == str(n)[::-1]:
# 		return True
# 	else:
# 		return False

# n = int(input())
# ans = 0
# while True:
# 	if n == 1:
# 		continue
# 	if chk(n) and chk3(n):
# 		ans = n
# 		break
# 	n+=1

# print(ans)


# # 통과
# import math

# def isPrime(x):
# 	for i in range(2, int(math.sqrt(x)+1)):
# 		if x % i == 0:
# 			return False
# 	return True

# N = int(input())
# result = 0

# for i in range(N, 1000001):
# 	if i == 1:
# 		continue
# 	if str(i) == str(i)[::-1]:
# 		if isPrime(i) == True:
# 			result = i
# 			break

# if result == 0:
# 	result = 1003001

# print(result)



# 숫자판 점프
# https://www.acmicpc.net/problem/2210

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# g = [list(map(str,input().split())) for _ in range(5)]
# ans = []
# def dfs(x,y,num):
# 	if len(num) == 6:
# 		if num not in ans:
# 			ans.append(num)
# 		return

# 	for i in range(4):
# 		nx = x + dx[i]
# 		ny = y + dy[i]
# 		if 0<=nx<5 and 0<= ny <5:
# 			dfs(nx,ny,num+g[nx][ny])

# for i in range(5):
# 	for j in range(5):
# 		dfs(i,j,g[i][j])

# print(len(ans))

# 색종이 붙이기
# https://www.acmicpc.net/problem/17136

# from collections import deque

# dx = [0,1,1]
# dy = [1,0,1]



# g = [list(map(int,input().split())) for _ in range(10)]
# visited = [[0] * 10 for _ in range(10)]


# def dfs(x,y):
# 	q = deque([(x,y)])
# 	visited[x][y] = 1

# 	while q:
# 		x,y = q.popleft()
# 		for i in range(3):
# 			nx = x + dx[i]
# 			ny = y + dy[i]

# 			if 0 <= nx < 10 and 0<= ny <10:
# 				if not visited[nx][ny] and g[nx][ny]:


# for i in range(10):
# 	for j in range(10):
# 		if not visited[i][j]:
# 			visited[i][j] = 1
# 			if g[i][j]:
# 				dfs(i,j)


# 회전 초밥
# https://www.acmicpc.net/problem/2531

# n,d,k,c =map(int,input().split())
# arr = [int(input()) for _ in range(n)]
# nArr = arr * 2


# for i in nArr:


# visited = [for i in range(1,d+1)]

# 1
# 4
# 2 4 7 10


# def chk(n):
# 	s = str(n)
# 	for i in range(0,len(s)-1):
# 		if s[i] > s[i+1]:
# 			return False
# 	return True




# t = int(input())
# for case in range(t):
# 	n = int(input())
# 	arr = sorted(list(map(int,input().split())))
# 	chkArr = []
# 	for i in range(n):
# 		for j in range(i+1,n):
# 			if chk(arr[i]*arr[j]):
# 				chkArr.append(arr[i]*arr[j])

# 	print(f"#{case+1} {chkArr[-1]}")



# def chk(n):
# 	s = str(n)
# 	for i in range(0,len(s)-1):
# 		if s[i] > s[i+1]:
# 			return False
# 	return True


# T = int(input())

# for case in range(1,T+1):
# 	n = int(input())
# 	arr = list(map(int,input().split()))
# 	arr.sort(reverse=True)
# 	maxV = -1
# 	for i in range(n-1):
# 		for j in range(i+1,n):
# 			v = arr[i]*arr[j]
# 			if maxV > v:
# 				break
# 			if chk(v):
# 				maxV = v
# 	print(f'#{case} {maxV}')



# def chk(n):
# 	s = str(n)
# 	for i in range(0,len(s)-1):
# 		if s[i] > s[i+1]:
# 			return False
# 	return True


# t = int(input())

# for case in range(t):
# 	n = int(input())
# 	arr = list(map(int,input().split()))
# 	arr.sort(reverse=True)
# 	maxV = -1
# 	for i in range(n-1):
# 		for j in range(i+1,n):
# 			v = arr[i]*arr[j]
# 			if maxV > v:
# 				break
# 			if chk(v):
# 				maxV = v
# 	print(f"#{case+1} {maxV}")

# 회전 초밥
# https://www.acmicpc.net/problem/2531


# import sys
# input = sys.stdin.readline
# n,d,k,c = map(int,input().split())
# arr = [int(input()) for _ in range(n)]

# lp,rp = 0,0
# answer = 0

# while lp != n:
# 	rp = lp+k
# 	case = set()
# 	addable = True

# 	for i in range(lp,rp):
# 		i %= n
# 		case.add(arr[i])
# 		if arr[i] == c: addable = False
# 	cnt = len(case)

# 	if addable: cnt += 1
# 	answer = max(answer,cnt)
# 	lp += 1
# print(answer)


# import sys
# input = sys.stdin.readline

# n,d,k,c = map(int,input().split())
# arr  = [int(input()) for _ in range(n)]

# start,end = 0,0
# answer = 0

# while start != n:
# 	end = start+k
# 	case = set()
# 	add = True

# 	for i in range(start,end):
# 		i %= n
# 		case.add(arr[i])
# 		if arr[i] == c: add = False

# 	cnt = len(case)

# 	if add: cnt+=1
# 	answer = max(answer,cnt)
# 	start += 1
# print(answer)



# 다음 소수
# https://www.acmicpc.net/problem/4134


# def prime(n):
# 	for i in range(2,int(n**0.5)+1):
# 		if n % i == 0:
# 			return False
# 	return True

# n = int(input())
# arr = [int(input()) for _ in range(n)]

# for chk in arr:
# 	if chk < 2:
# 		print(2)
# 		continue
# 	while True:
# 		if prime(chk):
# 			print(chk)
# 			break
# 		chk+=1



# 킹
# https://www.acmicpc.net/problem/1063

# R : 한 칸 오른쪽으로
# L : 한 칸 왼쪽으로
# B : 한 칸 아래로
# T : 한 칸 위로
# RT : 오른쪽 위 대각선으로
# LT : 왼쪽 위 대각선으로
# RB : 오른쪽 아래 대각선으로
# LB : 왼쪽 아래 대각선으로


# A1 A2 5
# B
# L
# LB
# RB
# LT
# def convert(s):
# 	return (ord(s[0]) - ord('H') + 8,int(s[1]))

# def chkMove(newMoveX,newMoveY):
# 	if 0<=newMoveX < 8 and 0<=newMoveY < 8:
# 		return True
# 	return False

# def stoneMove(sx,sy,move):

# 	if arr[sx][sy] == 2:
# 		if move == 'B':





# king,stone,n = map(str,input().split())

# kingX,kingY = convert(king)
# stoneX,stoneY = convert(stone)

# arr = [[0]*9 for _ in range(9)]

# arr[kingX][kingY] = 1
# arr[stoneX][stoneY] = 2

# for _ in range(n):
# 	path = input()

# 	if path == 'R':
# 		arr[kingX][kingY] = 0
# 		arr[kingX][kingY+1] = 1


# king,rock, t = input().split()
# t = int(t)
# move = [input() for _ in range(t)]


# king_x = int(ord(king[0])) - int(ord('A')) + 1
# king_y = int(king[1])

# rock_x = int(ord(rock[0])) - int(ord('A')) + 1
# rock_y = int(rock[1])


# alp = ['A','B','C','D','E','F','G','H']


# move_type = ['R','L' ,'B' ,'T' ,'RT' ,'LT' ,'RB' ,'LB']
# dx = [+1,-1, 0, 0, +1, -1, +1, -1]
# dy = [0, 0, -1, +1, +1, +1, -1, -1]



# for i in range(t): # t번 반복
# 	# move[i]가 move_type에서 몇번째 인덱스인지 찾기
# 	index = move_type.index(move[i])

# 	# 킹이 t번 움직인다. (예외 검사)
# 	if king_x + dx[index] >= 1 and king_x + dx[index] <= 8 and king_y + dy[index] >= 1 and king_y + dy[index] <= 8: # 킹 예외
# 		if king_x + dx[index] == rock_x and king_y + dy[index] == rock_y: #돌에 얹힘
# 			if rock_x + dx[index] >= 1 and rock_x + dx[index] <= 8 and rock_y + dy[index] >= 1 and rock_y + dy[index] <= 8: # 돌예외
# 				king_x += dx[index]
# 				king_y += dy[index]
# 				rock_x += dx[index]
# 				rock_y += dy[index]
# 			else:
# 				continue

# 		else :
# 			king_x += dx[index]
# 			king_y += dy[index]


# 	else:
# 		continue


# print(alp[king_x-1]+str(king_y))
# print(alp[rock_x-1]+str(rock_y))





# 도로와 신호등
# https://www.acmicpc.net/problem/2980

# import sys
# input = sys.stdin.readline

# N, L = map(int, input().split())
# pos = 0
# answer = 0

# for _ in range(N):
# 	d, r, g = map(int, input().split())

# 	answer += (d - pos)
# 	pos = d
# 	if answer % (r+g) <= r:
# 		answer += (r - (answer%(r+g)))

# answer += (L-pos)
# print(answer)

# 롤 케이크
# https://www.acmicpc.net/problem/3985

l = int(input())
n = int(input())
a = -1
ans1 = 0
b = -1
ans2 = 0
visited = [0] * (l+1)
for person in range(1,n+1):
	start,end = map(int,input().split())

	distance = end - start
	if a < distance:
		a = distance
		ans1 = person

	tmpCnt = 0
	for i in range(start,end+1):
		if not visited[i]:
			visited[i] = person
			tmpCnt+=1

	if b < tmpCnt:
		b = tmpCnt
		ans2 = person

print(ans1,ans2,sep='\n')


# 색종이
# https://www.acmicpc.net/problem/10163

import sys
input = sys.stdin.readline

N = int(input())
matrix = [[0]*1001 for _ in range(1001)]
for k in range(1,N+1):
	x,y,w,h = map(int, input().split())
	for i in range(x,x+w):
		for j in range(y,y+h):
			matrix[i][j] = k

cnt_color = [0] * (N+1)
for i in range(1001):
	for j in range(1001):
		if matrix[i][j]:
			cnt_color[matrix[i][j]] += 1

for i in range(1,N+1):
	print(cnt_color[i])
