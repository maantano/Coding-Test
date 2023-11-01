# M = 10 이고 N = 12

# 3
# 10 12 3 9
# 10 12 7 2
# 13 11 5 6

import sys
input = sys.stdin.readline

n = int(input().rstrip())

def chk(m,n,x,y):
	while x <= m * n:
		if (x-y) % n == 0:
			return x
		x += m
	return -1

def chk2(m,n,x,y):
	k = x
	while year <= m * n:
		if (k-x) % m and (k-y) % n == 0:
			return k
		k += m
	return -1

for i in range(n):
	m,n,x,y = map(int,input().split())
	print(chk(m,n,x,y))

# def chk(m,n,x,y):
# 	year = 1
# 	while year <= m *n:
# 		if year % m == x and year % n == y:
# 			return year
# 		year+=1
# 	return -1

# for i in range(n):
# 	m,n,x,y = map(int,input().split())
# 	print(chk(m,n,x,y))

# for i in range(n):
# 	year = 1
# 	m,n,x,y = map(int,input().split())
# 	while True:
# 		if year % m == x and year % n == y:
# 			print(year)
# 			break
# 		year+=1



