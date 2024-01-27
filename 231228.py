
# #10430 // 나머지
# a,b,c = map(int,input().split(' '))

# print((a+b)%c)
# print(((a%c)+(b%c))%c)
# print((a*b)%c)
# print(((a%c)*(b%c))%c)


# 4375 //1
# while True:
# 	try:
# 		n = int(input())
# 	except:
# 		break
# 	num = 0
# 	i = 1
# 	while True:
# 		num = num * 10 + 1
# 		num %= n
# 		if num == 0:
# 			print(i)
# 			break
# 		i+=1


# 1037 약수
# n = int(input())
# arr = sorted(list(map(int,input().split())))
# print(arr[0]*arr[-1])


# 17427 약수의 합 2

# n = int(input())
# answer = 0
# for i in range(1,n+1):
# 	answer+=((n//i) * i)
# print(answer)

# 시간초과
# import sys
# input = sys.stdin.readline
# n = int(input())

# answer = 0
# dp=[]
# for i in range(1,n+1):
# 	for j in range(1,int(i**0.5)+1):
# 		if i % j == 0:
# 			answer+=j
# 			dp.append(j)
# 			if j**2 != i:
# 				answer+=(i//j)
# 				dp.append(i//j)
# print(answer)


# 17425 약수의 합

#  시간 초과
# def sumArr(x):
# 	answer = x
# 	for i in range(2,x+1):
# 		answer+=((x//i) * i)
# 	return answer
# import sys
# input = sys.stdin.readline
# t = int(input())
# for i in range(t):
# 	chk = int(input())
# 	print(sumArr(chk))

#  Pypy3 으로 성공
# 테스트 케이스가 있으므로 계속 약수의 합을 구할 필요 없이 미리 한번을 구하고 가져다 사용만 하면됨,
# s[i-1]이 이전 수의 약수의 합 + 현재의 수의 약수의 합 d[i]를 합쳐서 s[i]를 구함.
# import sys
# input = sys.stdin.readline

# MAX = 1000000;
# d = [1] * (MAX+1)
# s = [0] * (MAX+1)

# for i in range(2,MAX+1):
# 	j = 1
# 	while i*j <=MAX:
# 		d[i*j] += i
# 		j+=1

# for i in range(1,MAX+1):
# 	s[i] = s[i-1] + d[i]

# t = int(input())
# ans = []
# for _ in range(t):
# 	n = int(input())
# 	ans.append(s[n])
# print('\n'.join(map(str,ans))+'\n')

# 2609 최대공약수와 최소공배수

# arr = list(map(int,input().split()))

def gcd(a,b):
	while b>0:
		a,b = b,a%b
	return a

def lcm(a,b):
	return (a*b) // gcd(a,b)
print(gcd(min(arr),max(arr)))
print(lcm(min(arr),max(arr)))



# 1978 소수찾기

# def prime(x):
# 	if x ==1:
# 		return False
# 	for i in range(2,int(x**0.5)+1):
# 		if x % i ==0:
# 			return False
# 	return True

# n = int(input())
# arr = list(map(int,input().split()))

# answer = 0
# for i in arr:
# 	answer += prime(i)
# print(answer)

# 1929 소수구하기
# m,n = map(int,input().split())

# def prime(x):
# 	if x < 2:
# 		return False
# 	for i in range(2,int(x**0.5)+1):
# 		if x % i == 0:
# 			return False
# 	return True

# for i in range(m,n+1):
# 	if(prime(i)):print(i)


# 에라토스테네스의 체
# MAX = 1000000
# chk = [0] * (MAX+1)
# chk[0] = chk[1] = 1

# for i in range(2,MAX+1):
# 	if not chk[i]:
# 		j = i*2
# 		while j<=MAX:
# 			chk[j] = 1
# 			j+=i
# m,n = map(int,input().split())
# for i in range(m,n+1):
# 	if not chk[i]:
# 		print(i)

# 6588 골드바흐의 추측
MAX = 1000000
chk = [0] * (MAX+1)
chk[0] = chk[1] = 1
prime = []

for i in range(2,MAX+1):
	if not chk[i]:
		prime.append(i)
		j = i*2
		while j<=MAX:
			chk[j] = 1
			j+=i
prime = prime[1:]
while True:
	n = int(input())
	if n ==0:
		break
	for p in prime:
		if not chk[n-p]:
			print('{0} = {1} + {2}'.format(n,p,n-p))
			break
