
# import sys
# input = sys.stdin.readline
# k,p,n = map(int,input().split())
# print(k * pow(p ,(n*10) ,1000000007)% 1000000007)


import sys


def f(p, n):
	if n == 1:
		print(1)
		return p

	elif n % 2 == 0:
		a = f(p, n / 2)
		return a * a % 1000000007

	else:
		b = f(p, (n - 1) / 2)
		return b * b * p % 1000000007

k, p, n = list(map(int, sys.stdin.readline().split()))
n = 10 * n
result = f(p, n)
result *= k
print(result % 1000000007)
