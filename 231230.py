


# 4948 베르트랑 공준

# 1
# 10
# 13
# 100
# 1000
# 10000
# 100000
# 0

# MAX = 123456 * 2 + 1
# p =[1] * MAX

# for i in range(1,MAX+1):
# 	if i ==1:
# 		continue
# 	for j in range(2,int(i**0.5)+1):
# 		if i % j == 0:
# 			p[i] = 0
# 			break
# while True:
# 	n = int(input())
# 	if n == 0:
# 		break
# 	prime = 0
# 	for i in range(n+1,(n*2)+1):
# 		prime += p[i]
# 	print(prime)


# 2108 통계학
# from collections import Counter
# n = int(input())
# arr = sorted([int(input()) for _ in range(n)])

# c = Counter(arr)
# c = sorted(c.items(),key=lambda x : (x[1],x[0]))

# print(round(sum(arr) / len(arr)))
# print(arr[len(arr)//2])
# if c[0][1] == c[1][1]:
# 	print(c[1][0])
# else:
# 	print(c[0][0])
# print(max(arr)-min(arr))


# 1676 팩토리얼 0의 개수
# n = int(input())
# cnt = 0
# while n >0:
# 	cnt+= n//5
# 	n //=5
# print(cnt)
# n = int(input())
# print(n//5 + n //25 + n //125)



# 9020 # 골드바흐의 추측

def isPrime(x):
	for i in range(2,int(x**0.5)+1):
		if x % i == 0:
			return False
	return True

MAX = 10000

n = int(input())
for i in range(n):
	chk = int(input())
	a,b = chk//2,chk//2
	while a > 0:
		if isPrime(a) and isPrime(b):
			print(a,b)
			break
		else:
			a-=1
			b+=1


# MAX = 10000
# p = [0] * (MAX+1)
# p[0] = p[1] = 1
# prime = {}
# for i in range(2,MAX+1):
# 	if not p[i]:
# 		prime[i] = 1
# 		j = i*2
# 		while j < MAX:
# 			p[j] =1
# 			j+=i
# n = int(input())
# for i in range(n):
# 	chk = int(input())
# 	a,b = chk // 2, chk // 2
# 	while a > 2:
# 		if prime[a] and prime[b]:
# 			print(a,b)
# 		else:
# 			a-=1
# 			b+=1


