# 소수의 연속합
# https://www.acmicpc.net/problem/1644

# 하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다.
# 몇 가지 자연수의 예를 들어 보면 다음과 같다.

# 3 : 3 (한 가지)
# 41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세 가지)
# 53 : 5+7+11+13+17 = 53 (두 가지)
# 하지만 연속된 소수의 합으로 나타낼 수 없는 자연수들도 있는데, 20이 그 예이다.
# 7+13을 계산하면 20이 되기는 하나 7과 13이 연속이 아니기에 적합한 표현이 아니다.
# 또한 한 소수는 반드시 한 번만 덧셈에 사용될 수 있기 때문에, 3+5+5+7과 같은 표현도 적합하지 않다.
# 자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램을 작성하시오.

# 첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 4,000,000)
# N^2 불가


# import sys
# input = sys.stdin.readline

# # 에리스토테네스의 체
# n = int(input())
# a = [False,False]+[True]*(n-1)
# p = []
# for i in range(2,n+1):
# 	if a[i]:
# 		p.append(i)
# 		for j in range(2*i,n+1,i):
# 			a[j] = False
# answer = 0
# start = 0
# end = 0

# while end <= len(p):
# 	tmpSum = sum(p[start:end])
# 	if tmpSum == n:
# 		answer+=1
# 		end+=1
# 	elif tmpSum < n:
# 		end+=1
# 	elif tmpSum > n:
# 		start+=1
# print(answer)


# 합분해
# https://www.acmicpc.net/problem/2225

# 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성하시오.
# 덧셈의 순서가 바뀐 경우는 다른 경우로 센다(1+2와 2+1은 서로 다른 경우). 또한 한 개의 수를 여러 번 쓸 수도 있다.

# import sys
# input = sys.stdin.readline
# n,k = map(int,input().split())
# dp  = [[0] *(k+1) for _ in range(n+1)]
# dp[0][0] = 1

# for i in range(0,n+1):
# 	for j in range(1,k+1):
# 		dp[i][j] = dp[i-1][j] + dp[i][j-1]
# print(dp[n][k] % 1000000000)

# 곱셈
# https://www.acmicpc.net/problem/1629
# 단순히 제곱으로 풀면 시간초과가 난다.

# a,b,c = map(int,input().split())

# def power(a,b):
# 	if b == 1:
# 		return a % c
# 	else:
# 		tmp = power(a,b//2)
# 		if b % 2 == 0:
# 			return tmp * tmp % c
# 		else:
# 			return tmp * tmp * a % c
# print(power(a,b))





# 행렬 제곱
# https://www.acmicpc.net/problem/10830


# 크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오.
# 수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.


# import sys
# input = sys.stdin.readline

# n,b = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(n)]


# def mul_arr (arr1,arr2):
# 	res = [[0]*n for _ in range(n)]

# 	for i in range(n):
# 		for j in range(n):
# 			for z in range(n):
# 				res[i][j] += arr1[i][z] * arr2[z][j] % 1000
# 	return res

# def power(a,b):
# 	if b == 1:
# 		return a
# 	else:
# 		tmp = power(a,b//2)
# 		if b % 2 == 0:
# 			return mul_arr(tmp,tmp)
# 		else:
# 			return mul_arr(mul_arr(tmp,tmp),a)
# result  = power(arr,b)

# for row in result:
# 	for col in row:
# 		print(col % 1000 , end = ' ')
# 	print()


# 나머지 합
# https://www.acmicpc.net/problem/10986
# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# num = list(map(int,input().split()))
# sum = 0
# reminder = [0] * m
# result = reminder[0]

# for i in range(n):
# 	sum += num[i]
# 	reminder[sum%m] += 1
# for i in reminder:
# 	result += i * (i-1) // 2


# 문자열
# https://www.acmicpc.net/problem/1120

# a,b = map(str,input().split(' '))
# tmpL = len(b) - len(a)
# chk = 0
# answer = 0
# for i in range(0,tmpL):
# 	str1 = b[i]+a
# 	str2 = a+b[-i]
# 	for j in range(len(a)+i+1):
# 		print(b[j])
# 		if b[j] == str1[j]:
# 			chk+=1
# 		else:
# 			chk-=1
# 	if chk>=0:
# 		a = str1
# 	else:
# 		a = str2
# for i in range(len(a)):
# 	if a[i] != b[i]:
# 		answer+=1
# print(answer)

# a,b = input().split()

# answer = []
# for i in range(len(b)-len(a) +1):
# 	count = 0
# 	for j in range(len(a)):
# 		if a[j] != b[i+j]:
# 			count+=1
# 	answer.append(count)
# print(min(answer))


# 문서 검색
# https://www.acmicpc.net/problem/1543

# s = input().rstrip()
# chk = input().rstrip()

# start = 0
# end = len(s)
# answer = 0
# while start <= end:
# 	if s[start:len(chk)+start] == chk:
# 		answer+=1
# 		start +=len(chk)
# 	else:
# 		start+=1
# print(answer)


# Four Squares
# https://www.acmicpc.net/problem/17626

# import math
# n = int(input())
# answer = 1
# def divider(n):
# 	global answer
# 	print('n ===>',n)
# 	print('int(math.sqrt(n)) ===>',int(math.sqrt(n)))
# 	if n % int(math.sqrt(n)) == 0 :
# 		print(answer)
# 		return answer
# 	else:
# 		answer+=1
# 		divider(n-(int(math.sqrt(n))**2))

# divider(n)



import math

n = int(input())
dp = [0,1]
for i in range(2, n+1):
	minValue = 1e9
	for j in range(1, int(math.sqrt(i)) + 1):
		minValue = min(minValue, dp[i - j**2])
	dp.append(minValue + 1)

print(dp)
print(dp[n])

