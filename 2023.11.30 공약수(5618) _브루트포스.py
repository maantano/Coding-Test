import sys
input = sys.stdin.readline



from collections import deque
def gcd(x,y):
	while y >0:
		x,y = y,x%y
	return x

def divisor(n):
	answer = []
	for i in range(1,int(n**0.5)+1):
		if n % i == 0:
			answer.append(i)
			if i**2 != n:
				answer.append(n//i)
	return sorted(answer)

n = int(input())
arr = deque(list(map(int,input().split())))

while len(arr) > 1:
	x = arr.popleft()
	y = arr.popleft()
	arr.append(gcd(x,y))

gcdNum = arr.popleft()

answer = divisor(gcdNum)

for i in answer:
	print(i)





