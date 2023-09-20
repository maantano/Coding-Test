# # 25 ,5

# 내 풀이
n ,m = map(int,input().split())
cnt =0
while True:
	if (n % m) == 0:
		n = n // m
		cnt +=1
	else:
		n -= 1
		cnt +=1
	if n == 1:
		break
print(cnt)

# 책 풀이
n ,k = map(int,input().split())
result = 0

while n >= k:
	while n % k != 0:
		n-=1
		result +=1
	n //= k
	result +=1
print(result)
print(n)

while n >1:
	n -= 1
	result +=1

