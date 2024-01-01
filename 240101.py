# 1629 곱셈
# 시간 초과
# a,b,c = map(int,input().split(' '))
# print(a**b % c)

# print(a%c)
# print(b%c)
# print(a//c)
# print(b//c)
# print((a%c) ** (b%c))

# print(a* (c*0.01) ** (b* (c*0.01)))
# print(b* (c*0.01))

# a,b,c =map(int,input().split(' '))
# def multi(a,n):
# 	if n == 1:
# 		return a % c
# 	else:
# 		tmp = multi(a,n//2)
# 		if n % 2 ==0:
# 			return (tmp * tmp) % c
# 		else:
# 			return (tmp * tmp * a) % c
# print(multi(a,b))


# 6603 로또

# from itertools import combinations
# while True:
# 	arr = list(map(int,input().split(' ')))
# 	if arr[0] == 0:
# 		break
# 	n = arr[0]
# 	arr = arr[1:]
# 	answer = list(combinations(arr,6))
# 	for i in answer:
# 		print(*i)
# 	print()

# 1094 막대기

# 틀림,,
# from collections import deque
# x = int(input())
# cnt = 1
# stick = deque([64])
# while True:
# 	if sum(stick) == x or x == 64:
# 		break
# 	else:
# 		tmp = stick.popleft() // 2
# 		a = b = tmp
# 		if b + sum(stick) >= x:
# 			stick.append(b)
# 			cnt+=1
# 		else:
# 			stick.append(a)
# 			stick.append(b)
# print(cnt)

# x = int(input())
# count = 0
# n = 64

# while x > 0:
# 	if n > x:
# 		n = n // 2
# 	else:
# 		count += 1
# 		x -= n
# print(count)

# 11051 이항 계수 2
# import sys
# input = sys.stdin.readline
# n,k = map(int,input().split())

# def facto(n):
# 	ans = 1
# 	for i in range(2,n+1):
# 		ans *= i
# 	return ans

# def bino_coef_facto(n,r):
# 	return facto(n) // facto(r) // facto(n-r)

# print(bino_coef_facto(n,k) %10007)

# 1699 제곱수의 합
# 번례를 찾고싶음,,
# print(int(7**0.5))
# n = int(input())
# cnt = 0
# chk = int(n**0.5)

# while n > 0 and chk >0:
# 	if n - chk**2 >= 0:
# 		cnt+=1
# 		n-=chk**2
# 	else:
# 		chk-=1
# print(cnt)


# import sys
# input = sys.stdin.readline

# n = int(input())
# dp = [k for k in range(n+1)]

# for i in range(1, n + 1):
# 	for j in range(1, i):
# 		if j*j > i:
# 			break
# 		if dp[i] > dp[i-j*j]+1:
# 			dp[i] = dp[i-j*j] + 1
# print(dp[n])

# SW Expert Academy 파리퇴치3
dxPlus = [-1,1,0,0]
dyPlus = [0,0,-1,1]
dxMulti = [-1,-1,1,1]
dyMulti = [-1,1,-1,1]

def plus(x,y):
	answer = arr[x][y]
	for i in range(4):
		for j in range(1,m):
			nx = dxPlus[i]*j + x
			ny = dyPlus[i]*j + y
			if 0<= nx < n and 0<= ny < n:
				answer+=arr[nx][ny]
	return answer



def multi(x,y):
	answer = arr[x][y]
	for i in range(4):
		for j in range(1,m):
			nx = dxMulti[i]*j + x
			ny = dyMulti[i]*j + y
			if 0<= nx < n and 0<= ny < n:
				answer+=arr[nx][ny]
	return answer



t = int(input())
for i in range(t):
	n,m = map(int,input().split(' '))
	arr = [list(map(int,input().split(' '))) for _ in range(n)]
	answer = 0
	for i in range(n):
		for j in range(n):
			answer = max(answer, plus(i,j),multi(i,j))
	print('answer ====>',answer)


