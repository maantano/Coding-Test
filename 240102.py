# 9375 패션왕 신해빈

# t = int(input())
# for i in range(t):
# 	n = int(input())
# 	d = {}
# 	for i in range(n):
# 		a,b = map(str,input().split())
# 		if b not in d:
# 			d[b] = 1
# 		else:
# 			d[b] +=1
# 	answer = 1
# 	for k,v in d.items():
# 		answer *= (v+1)
# 	print(answer-1)

# from collections import Counter
# from functools import reduce
# t = int(input())
# for i in range(t):
# 	n = int(input())
# 	d = {}
# 	for i in range(n):
# 		a,b = map(str,input().split())
# 		if b not in d:
# 			d[b] = 1
# 		else:
# 			d[b] += 1
# 	answer = reduce(lambda x,y : x * (y+1), d.values(),1) -1
# 	print(answer)

# 프로그래머스 위장
# clothes=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# def solution(clothes):
# 	from collections import Counter
# 	from functools import reduce
# 	cnt = Counter([kind for name, kind in clothes])
# 	answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
# 	# reduce
# 	# function: (_T@reduce, _S@reduce) -> _T@reduce,
#     # sequence: Iterable[_S@reduce],
#     # initial: _T@reduce
# 	return answer

# solution(clothes)

# 25206 # 너의 평점은
# n = 20
# grade_dict = {'A+':4.5,
# 			'A0':4.0,
# 			'B+':3.5,
# 			'B0':3.0,
# 			'C+':2.5,
# 			'C0':2.0,
# 			'D+':1.5,
# 			'D0':1.0,
# 			'F':0}
# total = 0
# result = 0
# for _ in range(n):
# 	subject, credit, grade = input().split()
# 	credit = float(credit)
# 	if grade != 'P':
# 		total += credit
# 		result += credit * grade_dict[grade]
# print('{:.6f}'.format(result / total))


# 10610 30
#  메모리 초과
# from itertools import permutations
# import heapq
# n = str(input())
# arr = list(n)
# q = []
# if n == '30':
# 	print(n)
# else:
# 	answer = 0
# 	combi = list(permutations(arr,len(arr)))
# 	for i in combi:
# 		if i[0] == '0':
# 			continue
# 		heapq.heappush(q,(-int(''.join(i)),int(''.join(i))))

# 	for i in q:
# 		if i[1] % 30 ==0:
# 			answer = i[1]
# 			break
# 	if not answer:
# 		print(-1)
# 	else:
# 		print(answer)

#  시간 초과
# from itertools import permutations
# n = list(str(input()))
# permu = []
# for p in permutations(n):
# 	permu.append(int(''.join(p)))

# sortedPermu = sorted(permu,reverse=True)
# answer = 0
# for i in sortedPermu:
# 	if i % 30 == 0:
# 		answer = i
# 		break
# if not answer:
# 	print(-1)
# else:
# 	print(answer)

# n = input()
# n = sorted(n, reverse=True)
# sum = 0
# if '0' not in n:
# 	print(-1)
# else:
# 	for i in n:
# 		sum += int(i)
# 	if sum % 3 != 0 :
# 		print(-1)
# 	else :
# 		print(''.join(n))

# 14500 테트로미노
# 직접 회전 되는 경우의 수 다 만들어서 적용
# n,m = map(int,input().split())
# a = [list(map(int,input().split())) for _ in range(n)]
# ans = 0
# for i in range(n):
# 	for j in range(m):
# 		if j + 3< m:
# 			tmp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i][j+3]
# 			if ans < tmp : ans = tmp
# 		if i + 3  < n:
# 			tmp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+3][j]
# 			if ans < tmp : ans = tmp
# 		if i+1 < n and j+2 < m:
# 			tmp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+1][j+2]
# 			if ans < tmp : ans = tmp
# 		if i+2 < n and j+1 < m:
# 			tmp = a[i][j] + a[i][j+1] + a[i+1][j] + a[i+2][j]
# 			if ans < tmp : ans = tmp
# 		if i+1 < n and j+2 < m:
# 			tmp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+2]
# 			if ans < tmp : ans = tmp
# 		if i+2 < n and j-1 >= 0:
# 			tmp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+2][j-1]
# 			if ans < tmp : ans = tmp
# 		if i-1 >= 0 and j+2 < m:
# 			temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i-1][j+2]
# 			if ans < temp: ans = temp

# 		if i+2 < n and j+1 < m:
# 			temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+2][j+1]
# 			if ans < temp: ans = temp

# 		if i+1 < n and j+2 < m:
# 			temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j]
# 			if ans < temp: ans = temp

# 		if i+2 < n and j+1 < m:
# 			temp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+2][j+1]
# 			if ans < temp: ans = temp

# 		if i+1 < n and j+1 < m:
# 			temp = a[i][j] + a[i][j+1] + a[i+1][j] + a[i+1][j+1]
# 			if ans < temp: ans = temp

# 		if i-1 >= 0 and j+2 < m:
# 			temp = a[i][j] + a[i][j+1] + a[i-1][j+1] + a[i-1][j+2]
# 			if ans < temp: ans = temp

# 		if i+2 < n and j+1 < m:
# 			temp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+2][j+1]
# 			if ans < temp: ans = temp

# 		if i+1 < n and j+2 < m:
# 			temp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+1][j+2]
# 			if ans < temp: ans = temp

# 		if i+2 < n and j-1 >= 0:
# 			temp = a[i][j] + a[i+1][j] + a[i+1][j-1] + a[i+2][j-1]
# 			if ans < temp: ans = temp

# 		if j+2 < m:
# 			temp = a[i][j] + a[i][j+1] + a[i][j+2]
# 			if i-1 >= 0:
# 				temp2 = temp + a[i-1][j+1]
# 				if ans < temp2: ans = temp2

# 			if i+1 < n:
# 				temp2 = temp + a[i+1][j+1]
# 				if ans < temp2: ans = temp2


# 		if i+2 < n:
# 			temp = a[i][j] + a[i+1][j] + a[i+2][j]
# 			if j+1 < m:
# 				temp2 = temp + a[i+1][j+1]
# 				if ans < temp2: ans = temp2

# 			if j-1 >= 0:
# 				temp2 = temp + a[i+1][j-1]
# 				if ans < temp2: ans = temp2

# print(ans)

# blocks = (
# 	("1111"),
# 	("11",
#   	 "11"),
#   	("10",
#   	 "10",
#   	 "11"),
# 	("10",
#   	 "11",
#   	 "01"),
# 	("111",
# 	 "010",)
# )

# def mirror(b):
# 	ans = []
# 	for i in range(len(b)):
# 		ans.append(b[i][::-1])
# 	return ans

# def rotate(b):
# 	ans = ['']*len(b[0])
# 	for j in range(len(b[0])):
# 		for i in range(len(b)-1,-1,-1):
# 			ans[j] += b[i][j]
# 	return ans

# def calc(a,b,x,y):
# 	n = len(a)
# 	m = len(a[0])
# 	s = 0
# 	for i in range(len(b)):
# 		for j in range(len(b[0])):
# 			if b[i][j] == '0':
# 				continue
# 			nx,ny = x+i,y+j
# 			if 0 <= nx < n and 0<= ny <m:
# 				s+=a[nx][ny]
# 			else:
# 				return -1
# 	return s
# n,m = map(int,input().split())
# a = [list(map(int,input().split())) for _ in range(n)]
# ans = 0
# for i in range(n):
# 	for j in range(m):
# 		for block in blocks:
# 			b = block[::]
# 			for mir in range(2):
# 				for rot in range(4):
# 					cur = calc(a,b,i,j)
# 					if cur != -1 and ans < cur:
# 						ans = cur
# 					b = rotate(b)
# 				b = mirror(b)
# print(ans)


# blocks = (
# 	("1111"),
# 	("11",
#   	 "11"),
#   	("10",
#   	 "10",
#   	 "11"),
# 	("10",
#   	 "11",
#   	 "01"),
# 	("111",
# 	 "010",)
# )

# def mirror(b):
# 	ans = []
# 	for i in range(len(b)):
# 		ans.append(b[i][::-1])
# 	return ans

# def rotate(b):
# 	ans = ['']*len(b[0])
# 	for j in range(len(b[0])):
# 		for i in range(len(b)-1,-1,-1):
# 			ans[j] += b[i][j]
# 	return ans

# def calc(a,b,x,y):
# 	n = len(a)
# 	m = len(a[0])
# 	s = 0
# 	for i in range(len(b)):
# 		for j in range(len(b[0])):
# 			if b[i][j] =='0':
# 				continue
# 			nx,ny = x+i,y+j
# 			if 0<= nx < n and 0<= ny < m:
# 				s += a[nx][ny]
# 			else:
# 				return -1
# 	return -1

# n,m = map(int,input().split(' '))
# arr = [list(map(int,input().split())) for _ in range(n)]
# ans = 0

# for i in range(n):
# 	for j in range(m):
# 		for block in blocks:
# 			b = block[::]
# 			for mir in range(2):
# 				for rot in range(4):
# 					cur = calc(arr,b,i,j)
# 					if cur != -1 and ans < cur:
# 						ans = cur
# 					b = rotate(b)
# 				b = mirror(b)
# print(ans)



# 6064 카잉 달력
# pyp3
# t = int(input())
# for i in range(t):
# 	m,n,x,y = map(int,input().split())
# 	x -= 1
# 	y -= 1
# 	k = x
# 	while k < n*m:
# 		if k % n == y:
# 			print(k+1)
# 			break
# 		k+=m
# 	else:
# 		print(-1)


# 1748 수 이어 쓰기 1
# 실제로 그냥 수를 붙여서 가도 된다.
# N제한이 1억이지만, 하나씩 붙여 가면 되기 때문에 시간 복잡도는 N


# n = int(input())
# ans = 0
# length = 1
# start = 1
# while start <= n:
# 	end = start * 10 - 1
# 	if end > n:
# 		end = n
# 	ans += (end-start+1)*length
# 	start *= 10
# 	length+=1
# print(ans)


# 9095  1,2,3 더하기

# t = int(input())
# dp = [0] * (12)
# dp[1] = 1
# dp[2] = 2
# dp[3] = 4
# dp[4] = 7
# for i in range(4,12):
# 		dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
# for i in range(t):
# 	n = int(input())
# 	print(dp[n])


# import sys
# input = sys.stdin.readline

# def go(sum, goal):
# 	if sum > goal:
# 		return
# 	if sum == goal:
# 		global answer
# 		answer += 1
# 		return
# 	for i in range(1, 4):
# 		go(sum + i, goal)

# n = int(input())
# answer = 0
# for _ in range(n):
# 	goal = int(input())
# 	go(0, goal)
# 	print(answer)
# 	answer = 0




# 15649 N과 M 1
# def dfs(idx,list):
# 	if idx == m:
# 		print(*list)
# 		return
# 	for i in range(1,n+1):
# 		if not chk[i]:
# 			chk[i] = 1
# 			dfs(idx+1,list+[i])
# 			chk[i] = 0

# n,m = map(int,input().split())
# chk = [0] * (n+1)
# dfs(0,[])



# 15650 N과 M 2

# def dfs(idx,list,start):
# 	if idx == m:
# 		print(*list)
# 		return
# 	for i in range(start,n+1):

# 		dfs(idx+1,list+[i],i+1)

# n,m = map(int,input().split())
# chk = [0] * (n+1)
# dfs(0,[],1)

# import sys
# n,m = map(int,input().split())
# a = [0]*m
# def go(idx,selected,n,m):
# 	if selected == m:
# 		sys.stdout.write(' '.join(map(str,a))+'\n')
# 		return
# 	if idx >n:
# 		return
# 	a[selected] = idx
# 	go(idx+1,selected+1,n,m)
# 	a[selected] = 0
# 	go(idx+1,selected,n,m)

# go(1,0,n,m)

# 15651 N과 M 3
# def dfs(idx,list):
# 	if idx == m:
# 		print(*list)
# 		return
# 	for i in range(1,n+1):
# 		dfs(idx+1,list+[i])

# n,m = map(int,input().split())

# dfs(0,[])

#15652 N과 M (4)
# n,m = map(int,input().split())
# visited = [0] * (n+1)
# def dfs(idx,list,skip):
# 	if idx == m:
# 		print(*list)
# 		return
# 	for i in range(1,n+1):
# 		if i >= skip:
# 			dfs(idx+1,list+[i],i)
# dfs(0,[],0)

#15654 N과 M (5)
# n,m = map(int,input().split())
# arr = sorted(list(map(int,input().split(' '))))
# visited = [0] * (arr[-1]+1)
# s = set()
# def dfs(idx,list):
# 	if idx == m:
# 		print(*list)
# 		return
# 	for i in arr:
# 		if not visited[i]:
# 			visited[i]= 1
# 			dfs(idx+1,list+[i])
# 			visited[i]= 0
# dfs(0,[])


#15655 N과 M (6)

# n,m = map(int,input().split())
# arr = sorted(list(map(int,input().split())))
# visited = [0] * (arr[-1]+1)

# def dfs(idx,list,skip):
# 	if idx == m:
# 		print(*list)
# 		return
# 	for i in arr:
# 		if i > skip:
# 			if not visited[i]:
# 				visited[i] = 1
# 				dfs(idx+1,list+[i],i)
# 			visited[i] = 0
# dfs(0,[],0)


# 15656 N과 M (7)

# n,m = map(int,input().split())
# arr = sorted(list(map(int,input().split())))

# def dfs(idx,list):
# 	if idx == m:
# 		print(*list)
# 		return
# 	for i in arr:
# 		dfs(idx+1,list+[i])
# dfs(0,[])


# 15657 N과 M (8)

n,m = map(int,input().split())
arr = sorted(list(map(int,input().split())))

def dfs(idx,list):
	if idx == m:
		print(*list)
		return
	for i in arr:
		if len(list) > 0:
			if list[-1] <= i:
				dfs(idx+1,list+[i])
		else:
			dfs(idx+1,list+[i])
dfs(0,[])
