# 18290  NM과 K (1)


# def dfs(x,y,idx,total):
# 	global answer
# 	if idx == k:
# 		answer = max(answer,total)
# 		return
# 	for i in range(n):
# 		for j in range(m):
# 			if visited[i][j]: continue
# 			for d in range(4):
# 				nx = x+dx[d]
# 				ny = y+dy[d]
# 				if 0<=nx<n and 0<= ny < m:
# 					if i == nx or j == ny:
# 						continue
# 					visited[nx][ny] = 1
# 					visited[i][j] = 1
# 					dfs(i,j,idx+1,total+arr[i][j])
# 					visited[i][j] = 0
# 					visited[nx][ny] = 0

# dfs(0,0,0,0)
# print(answer)


# n, m, k = map(int,input().split())
# a = [list(map(int,input().split())) for _ in range(n)]
# c = [[False]*m for _ in range(n)]
# ans = -2147483647
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]

# def go(px, py, cnt, s):
# 	if cnt == k:
# 		global ans
# 		if ans < s:
# 			ans = s
# 		return
# 	for x in range(px, n):
# 		for y in range(py if x == px else 0, m):
# 			if c[x][y]:
# 				continue
# 			ok = True
# 			for i in range(4):
# 				nx, ny = x+dx[i], y+dy[i]
# 				if 0 <= nx < n and 0 <= ny < m:
# 					if c[nx][ny]:
# 						ok = False
# 			if ok:
# 				c[x][y] = True
# 				go(x, y, cnt+1, s+a[x][y])
# 				c[x][y] = False

# go(0, 0, 0, 0)
# print(ans)


# n = int(input())
# m = int(input())
# broken = [0] * 10
# if m > 0:
# 	btn = list(map(int,input().split()))
# else:
# 	btn = []

# for b in btn:
# 	broken[b] = 1

# def check(chk):
# 	if chk == 0:
# 		if broken[0]:
# 			return 0
# 		else:
# 			return 1
# 	time = 0
# 	while chk > 0:
# 		tmp = chk % 10
# 		if broken[tmp]:
# 			return 0
# 		else:
# 			time+=1
# 			chk //= 10
# 	return time

# ans = abs(100-n)
# for i in range(0,1000001):
# 	c = i
# 	t = check(i)
# 	if t > 0:
# 		press = abs(c-n)
# 		if ans > t + press:
# 			ans = t + press
# print(ans)



# 9095 1,2,3 더하기

# t = int(input())
# answer = 0
# def dfs(total,goal):
# 	if total > goal:
# 		return 0
# 	if total == goal:
# 		return 1
# 	now = 0
# 	for i in range(1,4):
# 		now += dfs(total+i,goal)
# 	return now

# for i in range(t):
# 	chk = int(input())
# 	print(dfs(0,chk))


# 1759 암호 만들기

# vowel = ['a','e','i','o','u']

# n,m = map(int,input().split(' '))
# arr = sorted(list(map(str,input().split(' '))))

# def chk(password):
# 	ja = 0
# 	mo = 0
# 	for x in password:
# 		if x in 'aeiou':
# 			mo +=1
# 		else:
# 			ja +=1
# 	return ja >= 2 and mo >= 1

# def dfs(n,alpha,password,i):
# 	if len(password) == n:
# 		if chk(password):
# 			print(password)
# 		return
# 	if i == len(alpha):
# 		return
# 	dfs(n, alpha, password+alpha[i], i+1)
# 	dfs(n, alpha, password, i+1)

# dfs(n,arr,'',0)


# 14501 퇴사

inf = -10**9
n = int(input())
t = [0]*(n+1)
p = [0]*(n+1)
for i in range(1, n+1):
	t[i],p[i] = map(int,input().split())
ans = 0
def dfs(day,total):
	global ans
	if day == n+1:
		ans = max(ans,total)
		return
	if day > n+1:
		return
	dfs(day+1,total)
	dfs(day+t[day],total+p[day])
	# for i in arr:

dfs(1,0)
print(ans)


# for i in range(n):
