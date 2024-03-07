import sys
input = sys.stdin.readline

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




# string = input()
# stack  = []

# res = ''

# for s in string:
# 	if s.isalpha():
# 		res+=s
# 	else:
# 		if s =='(':
# 			stack.append(s)
# 		elif s =='*' or s =='/':
# 			while stack and (stack[-1] == '*' or stack[-1] == '/'):
# 				res+= stack.pop()
# 			stack.append(s)
# 		elif s =='+' or s =='-':
# 			while stack and stack[-1] != '(':
# 				res+= stack.pop()
# 			stack.append(s)
# 		elif s == ')':
# 			while stack and stack[-1] != '(':
# 				res += stack.pop()
# 			stack.pop()
# while stack:
# 	res += stack.pop()
# print(res)



# 창고 다각형
# https://www.acmicpc.net/problem/2304

# n = int(input())

# arr = [list(map(int,input().split())) for _ in range(n)]
# arr.sort(key= lambda x : x[0])

# ans = 0
# stack = [arr[0]]

# for chk in arr[1:]:
# 	if stack[-1][1] < chk[1]:
# 		x,y = stack.pop()
# 		ans += (chk[0] - x) * y
# 		stack.append([chk[0],chk[1]])

# if stack[0][1] > arr[-1][1]:
# 	ans += stack[0][1] + (arr[-1][0] - stack[0][0]) * arr[-1][1]
# else:
# 	ans += (arr[-1][0] - stack[0][0]) * stack[0][1] + arr[0][1]
# print(ans)

# [[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]

# n = int(input())

# lst = []
# result = 0
# for i in range(n) :
# 	a,b = map(int,input().split())
# 	lst.append([a,b])

# lst.sort()

# i = 0
# for l in lst :
# 	if l[1] >result :
# 		result = l[1]
# 		idx = i
# 	i += 1
# height = lst[0][1]

# for i in range(idx) :
# 	if height < lst[i+1][1] :
# 		result += height * (lst[i+1][0]-lst[i][0])
# 		height = lst[i+1][1]
# 	else :
# 		result += height * (lst[i+1][0] - lst[i][0])
# height = lst[-1][1]

# for i in range(n-1, idx, -1) :
# 	if height < lst[i-1][1] :
# 		result += height * (lst[i][0]-lst[i-1][0])
# 		height = lst[i-1][1]
# 	else :
# 		result += height * (lst[i][0] - lst[i-1][0])

# print(result)

# 다시
# 도키도키 간식드리미
# https://www.acmicpc.net/problem/12789

# n = int(input())
# arr = list(map(int,input().split()))

# stack = []
# chk = 1

# for i in arr:
# 	stack.append(i)
# 	while stack and stack[-1] == chk:
# 		stack.pop()
# 		chk+=1
# 	if len(stack) > 1 and stack[-1] > stack[-2]:
# 		print('Sad')
# 		exit()
# if stack:
# 	print('Sad')
# else:
# 	print('Nice')




# 외계인의 기타 연주
# https://www.acmicpc.net/problem/2841


# n = int(input())
# arr = [int(input()) for _ in range(n)]
# ans = [0] * n
# stack = []
# chk = 0

# for i in range(n):
# 	cnt = 0
# 	chk = i+1
# 	while chk != n and arr[i] > arr[chk]:
# 		cnt+=1
# 		chk+=1
# 	ans[i] = cnt
# print(sum(ans))


# n = int(input())
# arr = [int(input()) for _ in range(n)]
# stack = []
# cnt = 0
# for i in range(n):
# 	while stack and stack[-1] <= arr[i]:
# 		stack.pop()
# 	stack.append(arr[i])
# 	cnt+=len(stack)-1
# print(cnt)


# n = int(input())
# arr = [int(input()) for _ in range(n)]
# stack = []
# cnt = 0
# for i in range(n):
# 	while stack and stack[-1] <= arr[i]:
# 		stack.pop()
# 	stack.append(arr[i])
# 	cnt += len(stack) - 1
# print(cnt)


# n = int(input())
# arr = list(map(int,input().split()))
# stack = []
# chk = 1
# for i in range(n):
# 	stack.append(arr[i])
# 	while stack and stack[-1] == chk:
# 		stack.pop()
# 		chk+=1


# if stack:
# 	print('Sad')
# else:
# 	print('Nice')


# ============================================================
# 다시
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(1000000)

# string = input().rstrip()
# stack = []
# ans = 1
# answer =0
# chk = ''
# for i in range(len(string)):
# 	if string[i] == '(':
# 		stack.append(string[i])
# 		ans *= 2
# 	elif string[i] == '[':
# 		stack.append(string[i])
# 		ans *= 3
# 	elif string[i] == ')':
# 		if not stack or stack[-1] == '[':
# 			answer = 0
# 			break
# 		if string[i-1] == '(':
# 			answer += ans
# 		stack.pop()
# 		ans //= 2
# 	else:
# 		if not stack or stack[-1] == "(":
# 			answer = 0
# 			break
# 		if string[i-1] == "[":
# 			answer += ans
# 		stack.pop()
# 		ans //= 3

# if stack:
# 	print(0)
# else:
# 	print(answer)

# 상근이의 여행
# https://www.acmicpc.net/problem/9372
# def dfs(idx,cnt):
# 	chk[idx] = 1
# 	for n in g[idx]:
# 		if not chk[n]:
# 			cnt = dfs(n,cnt+1)
# 	return cnt

# t = int(input())
# for _ in range(t):
# 	n,m = map(int,input().split())
# 	g = [[] for _ in range(n+1)]
# 	for i in range(m):
# 		a,b = map(int,input().split())
# 		g[a].append(b)
# 		g[b].append(a)
# 	chk = [0] * (n+1)
# 	cnt = dfs(1,0)
# 	print(cnt)

# 트리 순회
# https://www.acmicpc.net/problem/1991

# n = int(input())
# g = [[] for _ in range(n)]
# g2 = [[] for _ in range(n)]
# g3 = [[] for _ in range(n)]

# for _ in range(n):
# 	a,b,c= map(str,input().split())
# 	if b != '.':
# 		g[ord(a)-65].append(ord(b)-65)
# 	if c != '.':
# 		g[ord(a)-65].append(ord(c)-65)

# print(g)


# visited = [0] * n
# visited2 = [0] * n
# visited3 = [0] * n
# ans = []
# ans2 = []
# ans3 = []
# def dfs(idx):
# 	visited[idx] = 1
# 	for chk in g[idx]:
# 		if not visited[chk]:
# 			ans.append(chk)
# 			dfs(chk)

# def dfs2(idx):
# 	visited2[idx] = 1
# 	for chk in g[idx][::-1]:
# 		if not visited2[chk]:
# 			ans2.append(chk)
# 			dfs2(chk)

# def dfs3(idx):
# 	visited[idx] = 1
# 	for chk in g[idx]:
# 		if not visited[chk]:
# 			ans.append(chk)
# 			dfs(chk)

# dfs(0)
# dfs2(0)
# print(ans)
# print(ans2)


# 정답
# n = int(input())
# d = {}
# for i in range(n):
# 	root,left,right = map(str,input().split())
# 	d[root] = [left,right]

# def a(root):
# 	if root != '.':
# 		print(root,end='')
# 		a(d[root][0])
# 		a(d[root][1])

# def b(root):
# 	if root !='.':
# 		b(d[root][0])
# 		print(root,end='')
# 		b(d[root][1])

# def c(root):
# 	if root !='.':
# 		c(d[root][0])
# 		c(d[root][1])
# 		print(root,end='')

# a('A')
# print()
# b('A')
# print()
# c('A')


# 완전 이진 트리
# https://www.acmicpc.net/problem/9934

# n = int(input())
# g = list(map(int,input().split()))

# tree = [[] for _ in range(n)]


# def MarkeTree(arr,x):
# 	mid = len(arr) // 2
# 	tree[x].append(arr[mid])
# 	if len(arr) == 1:
# 		return
# 	MarkeTree(arr[:mid],x+1)
# 	MarkeTree(arr[mid+1:],x+1)

# MarkeTree(g,0)
# for i in range(n):
# 	print(*tree[i])

# 나무 탈출
# https://www.acmicpc.net/problem/15900
# from collections import deque

# n = int(input())
# g = [[] for _ in range(n+1)]
# visited = [False for _ in range(n+1)]


# for i in range(n):
# 	a,b = map(int,input().split())
# 	g[a].append(b)
# 	g[b].append(a)

# dq = deque([(0,1)])
# visited[1] = 1
# d = 0

# while dq:
# 	now_d,now_node = dq.popleft()

# 	isLeaf = True
# 	for next_node in g[now_node]:
# 		if not visited[next_node]:
# 			isLeaf  = False
# 			visited[next_node] = 1
# 			dq.append((now_d+1,next_node))
# 	if isLeaf:
# 		d+=now_d
# if d % 2 == 1:
# 	print('Yes')
# else:
# 	print('No')

# import sys
# sys.setrecursionlimit(1000000)

# def solution(node):
# 	global need_move

# 	is_leaf = True
# 	for next in linked[node]:
# 		if not distance[next]:
# 			distance[next] = distance[node]+1
# 			solution(next)
# 			is_leaf = False

# 	if is_leaf:
# 		need_move += distance[node] - 1

# N = int(sys.stdin.readline())
# linked = [[] for _ in range(N+1)]
# distance = [0] * (N+1)
# need_move = 0

# for _ in range(N-1):
# 	a, b = map(int, sys.stdin.readline().split())
# 	linked[a].append(b)
# 	linked[b].append(a)

# distance[1] = 1
# solution(1)

# if need_move % 2:
# 	print('Yes')
# else:
# 	print('No')




# # ====================================================================================

# import sys
# from collections import deque

# N = int(sys.stdin.readline().rstrip())

# graph = [[] for _ in range(N+1)]
# visited = [False for _ in range(N+1)]

# for _ in range(N-1):
# 	f, s = map(int, sys.stdin.readline().split())
# 	graph[f].append(s)
# 	graph[s].append(f)

# dq = deque()
# dq.append((0, 1))
# visited[1] = True
# depth_cnt = 0

# # BFS로 탐색
# while dq:
# 	now_depth, now_node = dq.popleft()
# 	isLeaf = True
# 	for next_node in graph[now_node]:
# 		if not visited[next_node]:
# 			isLeaf = False
# 			visited[next_node] = True
# 			dq.append((now_depth+1, next_node))
# 	if isLeaf:
# 		depth_cnt += now_depth

# if depth_cnt % 2 == 1:
# 	print("Yes")
# else:
# 	print("No")

# 단절점과 단절선
# https://www.acmicpc.net/problem/14675
# import sys
# input = sys.stdin.readline
# n = int(input())
# g = [[]  for i in range(n+1)]

# for i in range(n-1):
# 	a,b = map(int,input().split())
# 	g[a].append(b)
# 	g[b].append(a)


# q = int(input())

# for i in range(q):
# 	a,b = map(int,input().split())

# 	if a == 2:
# 		print('yes')
# 	else:
# 		if len(g[b]) < 2:
# 			print('no')
# 		else:
# 			print('yes')




# 부동산 다툼
# https://www.acmicpc.net/problem/20364

# import sys

# n,q= map(int,input().split())
# visited = [0] * (n+1)

# for i in range(q):
# 	tan = int(input())
# 	target = tan
# 	flag = 0
# 	while target != 1:
# 		if visited[target] > 0:
# 			flag = target
# 		target //= 2
# 	if flag:
# 		print(flag)
# 	else:
# 		visited[tan] = 1
# 		print(0)



# N-Queen
# https://www.acmicpc.net/problem/9663

# n = int(input())

# def chk(x):
# 	for i in range(x):
# 		if arr[i] == arr[x] or abs(x-i) == abs(arr[i]-arr[x]):
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

# 먹을 것인가 먹힐 것인가
# https://www.acmicpc.net/problem/7795


# 1 1 3 7 8
# 1 3 6

# def chk(a,arrB):
# 	start = 0
# 	end = len(arrB)-1
# 	while start <= end:
# 		mid = (start+end) // 2
# 		if arrB[mid] < a:
# 			start+=1
# 		else:
# 			end-=1
# 	if mid == len(arrB) -1 : mid+=1
# 	return mid

# t = int(input())
# for _ in range(t):
# 	a,b = map(int,input().split())
# 	arrA = sorted(list(map(int,input().split())))
# 	arrB = sorted(list(map(int,input().split())))
# 	ans = 0
# 	for i in arrA:
# 		ans+=chk(i,arrB)
# 	print(ans)


# t = int(input())
# for _ in range(t):
# 	a,b = map(int,input().split())

# 	arrA = sorted(list(map(int,input().split())))
# 	arrB = sorted(list(map(int,input().split())))

# 	ans = 0
# 	start = 0
# 	for i in range(a):
# 		while True:
# 			if start == b or arrA[i]<=arrB[start]:
# 				ans+=start
# 				break
# 			else:
# 				start+=1
# 	print(ans)

# 암기왕
# https://www.acmicpc.net/problem/2776



# def chk(arr,c):
# 	start,end = 0,len(arr)-1
# 	while start <= end:
# 		mid = (start+end) // 2
# 		if arr[mid] == c:
# 			return 1
# 		elif arr[mid] < c:
# 			start = mid+1
# 		else:
# 			end = mid-1
# 	return 0

# t = int(input())
# for _ in range(t):
# 	n = int(input())
# 	a = sorted(list(map(int,input().split())))
# 	m = int(input())
# 	b = list(map(int,input().split()))

# 	for c in b:
# 		print(chk(a,c))

# 용돈 관리
# https://www.acmicpc.net/problem/6236


# n,m = map(int,input().split())
# arr = [int(input()) for _ in range(n)]

# start = min(arr)
# end = sum(arr)

# while start <= end:
# 	mid = (start+end) // 2
# 	tmp = mid
# 	num = 1
# 	for i in range(n):
# 		if tmp < arr[i]:
# 			tmp = mid
# 			num+=1
# 		tmp-=arr[i]

# 	if num > m or mid <max(arr):
# 		start = mid +1
# 	else:
# 		end = mid -1
# 		k = mid
# print(k)

# 과자 나눠주기
# https://www.acmicpc.net/problem/16401

# m,n = map(int,input().split())
# arr = list(map(int,input().split()))
# start = 0
# end = max(arr)
# answer = 0

# while start <= end:
# 	mid = (start+end) // 2
# 	tmp = 0
# 	if mid == 0:
# 		tmp = 0
# 		break

# 	for i in range(n):
# 		if arr[i] >= mid:
# 			tmp += (arr[i]//mid)
# 	if tmp >= m:
# 		start = mid +1
# 		answer = mid
# 	else:
# 		end = mid - 1

# print(answer)



# m,n = map(int,input().split())
# arr = list(map(int,input().split()))

# start = 1
# end = max(arr)
# answer = 0

# while start <= end:
# 	mid = (start+end) // 2
# 	tmp = 0


# 	for i in range(n):
# 		if arr[i] >= mid:
# 			tmp += (arr[i] // mid)
# 	if tmp >= m:
# 		start = mid+ 1
# 		answer = mid
# 	else:
# 		end = mid - 1
# print(answer)


# 보석 상자
# https://www.acmicpc.net/problem/2792

# n,m = map(int,input().split())
# arr = [int(input()) for i in range(m)]


# start = 1
# end = max(arr)

# while start <= end:
# 	mid = (start+end) // 2
# 	total = 0

# 	for color in arr:
# 		if color % mid == 0:
# 			total += color // mid
# 		else:
# 			total += (color//mid) + 1


# 	if total > n:
# 		start = mid +1
# 	else:
# 		end = mid -1
# print(start)

# 파닭파닭
# https://www.acmicpc.net/problem/14627

# s,c = map(int,input().split())
# arr = [int(input()) for _ in range(s)]


# start = 1
# end = max(arr)

# while start <= end:
# 	mid = (start+end)  // 2
# 	tmp = 0
# 	for chk in arr:
# 		tmp += chk // mid
# 	if tmp >= c:
# 		start=mid +1
# 	else:
# 		end = mid - 1

# print(sum(arr)-(c*end))

# 풍선 공장
# https://www.acmicpc.net/problem/15810


# n,m = map(int,input().split())
# arr = list(map(int,input().split()))

# start = 0
# end = max(arr) * m
# res = 0
# while start <= end:
# 	mid = (start+end) // 2
# 	if sum([mid//n for n in arr]) >= m:
# 		res = mid
# 		end = mid - 1
# 	else:
# 		start = mid + 1
# print(res)




# 히오스 프로게이머
# https://www.acmicpc.net/problem/16564

# n,k = map(int,input().split())
# arr = [int(input()) for _ in range(n)]


# start = min(arr)
# end = start+k

# ans = 0
# while start <= end:
# 	mid = (start+end) // 2
# 	tmp = 0

# 	for chk in arr:
# 		if mid > chk:
# 			tmp+= (mid-chk)

# 		if mid-chk <= k:
# 			end = mid-1
# 			ans = min(mid+chk,ans)
# 		else:
# 			start = mid +1
# print(ans)

# IF문 좀 대신 써줘
# https://www.acmicpc.net/problem/19637


# n,m = map(int,input().split())
# chks = [list(map(str,input().split())) for _ in range(n)]

# arr = [int(input()) for _ in range(m)]

# for chk in arr:
# 	start = 0
# 	end = len(chks)
# 	res = 0
# 	while start<=end:
# 		mid = (start+end) // 2
# 		if int(chks[mid][1]) >= chk:
# 			end = mid - 1
# 			res = mid
# 		else:
# 			start = mid +1
# 	print(chks[res][0])

# from bisect import bisect_left
# n,m = map(int,input().split())
# title = []
# power = []

# for _ in range(n):
# 	a,b = input().split()
# 	title.append(a)
# 	power.append(int(b))

# for _ in range(m):
# 	print(title[bisect_left(power,int(input()))])

# 이상한 술집
# https://www.acmicpc.net/problem/13702
# n,m = map(int,input().split())

# arr = [int(input()) for _ in range(n)]

# start = 1
# end = max(arr)
# res = 0
# while start <= end:
# 	mid = (start+end) // 2
# 	cnt = sum(i//mid for i in arr)
# 	if cnt >= m:
# 		res = mid
# 		start = mid + 1
# 	else:
# 		end = mid - 1
# print(res)

# 그르다 김가놈
# https://www.acmicpc.net/problem/18113

# import sys

# input = sys.stdin.readline

# n, k, m = map(int, input().split())
# gimbaps = [int(input()) for _ in range(n)]

# left = 1
# right = max(gimbaps)
# res = 0
# rcnt = 0

# def cutting (gimbap, p):
# 	if gimbap <= k:
# 		return 0
# 	elif gimbap < 2*k:
# 		gimbap -= k
# 	else:
# 		gimbap -= k*2

# 	return gimbap//p

# while left <= right:
# 	mid = (left + right) // 2
# 	cnt = 0
# 	for gimbap in gimbaps:
# 		cnt += cutting(gimbap,mid)

# 	if cnt >= m:
# 		left = mid + 1
# 		res = mid
# 		rcnt = cnt
# 	else:
# 		right = mid - 1

# if rcnt >= m:
# 	print(res)
# else:
# 	print(-1)


# 넷이 놀기
# https://www.acmicpc.net/problem/2121

# import sys

# n = int(sys.stdin.readline())
# a, b = map(int, sys.stdin.readline().split())
# data = set()
# for _ in range(n):
# 	data.add(tuple(map(int, sys.stdin.readline().split())))

# cnt = 0
# for i in data:
# 	if (i[0]+a, i[1]) in data and (i[0], i[1]+b) in data and (i[0]+a, i[1]+b) in data:
# 		cnt += 1
# print(cnt)

# 제곱근
# https://www.acmicpc.net/problem/13706

# n = int(input())

# start = 0
# end = n

# res = 0
# while start<= end:
# 	mid = (start+end) // 2

# 	if n >= mid ** 2:
# 		res = mid
# 		start = mid +1
# 	else:
# 		end = mid -1
# print(res)


# 어두운 굴다리
# https://www.acmicpc.net/problem/17266


# n = int(input())
# m = int(input())
# arr = list(map(int,input().split()))

# start = 0
# end = max(arr)


# def bs(li,m):
# 	if li[1]-li[0] > m:
# 		return 0
# 	if li[-1] - li[-2] > m:
# 		return 0


# while start<=end:
# 	mid = (start+end) // 2

# from bisect import bisect_left
# from bisect import bisect_right

# n,m = map(int,input().split())
# arr = list(map(int,input().split()))

# a,b= bisect_left(arr,m),bisect_right(arr,m)
# print(b-a if b-a else-1)



# n,m = map(int,input().split())
# arr = sorted([int(input()) for _ in range(n)])

# s = 0
# e = arr[-1] - arr[0]

# ans = 0
# while s <=e:
# 	mid = (s+e) // 2
# 	cur = arr[0]
# 	tmp = 1

# 	for i in range(1,n):
# 		if arr[i] >= cur + mid:
# 			tmp+=1
# 			cur = arr[i]
# 	if tmp >=m:
# 		s= mid+1
# 		ans = mid
# 	else:
# 		e = mid - 1
# print(ans)

# 캠프가는 영식
# https://www.acmicpc.net/problem/1590


n,t = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

res = []
for i in range(n):
	a,b,c = arr[i]
	li = [a+(b*i) for i in range(c)]
	if li[-1] < t:
		continue
	start = 0
	end = c-1
	ans = 0
	while start <= end:
		mid = (start+end) // 2
		if li[mid] >= t:
			end = mid - 1
			ans = mid
		else:
			start = mid + 1

	res.append(li[ans]-t)

print(min(res) if res else -1)





