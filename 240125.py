# 설탕 배달
# https://www.acmicpc.net/problem/2839
# n키로를 배달해야하고, 3,5키로 설탕이 있다.
# n = int(input())
# bag = 0
# while n >=0:
# 	if n % 5 == 0:
# 		bag+=(n//5)
# 		print(bag)
# 		break
# 	n-=3
# 	bag+=1
# else:
# 	print(-1)
# https://www.acmicpc.net/problem/9095
# 1, 2, 3 더하기
# n = int(input())
# arr = [int(input()) for _ in range(n)]



# 수학 알고리즘
# - 나머지 연산,
# - 약수, 최대공약수
# - 소수


# 1. 나머지 연산
# (A + B) % M === ((A % M) + (B % M) % M )
# (A * B) % M === ( (A * M) + (B * M) % M )

# a = 4
# b = 7
# m = 3
# (4+7) % 3 == (4%3 + 7%3) % 3
# 덧셈, 곱셈, 뺼셈만 이용가능
# 나누기는 성맆하지 않는다.

# 나머지 연산은 문제에서 "정답을 ~~~로 나눈 나머지를 출력하라"는 말이 있는 이뉴는 정답이 int나 long과 같은 자료형 범위를 넘어가기 때문이다.

# n = int(input())
# N의 배수는 N을 나눈 나머지가 0인지를 확인하면 된다.
# ex.
# 1 % 7 = 1 ==> 1% 7
# 11 % 7 = 4 ===> (1% 7 == 1 * 10 + 1)  % 7
# 111 % 7 =  6 ===> ((11 % 7 == 4) * 10 +1)  % 7
# 나머지 연산은 그 수가 너무 큰 경우, 그 나머지가 가지고 있는 의미가 있다면 사용하는 것.



# while True:
# 	try:
# 		n = int(input())
# 	except:
# 		break
# 	num  = 0
# 	i = 1
# 	while True:
# 		num = num * 10 + 1
# 		num %= n
# 		if num == 0:
# 			print(i)
# 			break
# 		i+=1


# n = int(input())

# dp = [0] * 12
# dp[1] = 1
# dp[2] = 2
# dp[3] = 4
# for i in range(4,12):
# 	dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# for i in range(n):
# 	chk = int(input())
# 	print(dp[chk])





# import sys
# input = sys.stdin.readline
# n,m = int(input().split())
# arr = list(map(int,input().split()))
# answer = []
# for i in range(len(arr)):
# 	chk = arr[i]
# 	if chk % m == 0:
# 		answer.append([i])
# 	for j in range(i+1,len(arr)):
# 		chk+=arr[j]
# 		if chk % m == 0:
# 			answer.append([i,j])
# print(len(answer))




# import sys
# input = sys.stdin.readline

# N,M= map(int, input().split())
# num = list(map(int, input().split()))
# sum = 0
# numRemainder = [0] * M

# for i in range(N):
# 	sum+= num[i]
# 	numRemainder[sum % M] += 1

# print(numRemainder)
# result = numRemainder[0]

# for i in numRemainder:
# 	result += i * (i-1) // 2

# print(result)



