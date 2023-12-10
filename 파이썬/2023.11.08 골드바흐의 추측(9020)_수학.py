
### 시간 초과 ㅎㅎㅎ....
# import sys
# input = sys.stdin.readline

# def ari(n):
# 	answer = []
# 	chk = [1]*(n+1)

# 	for i in range(2,n+1):
# 		if chk[i]:
# 			answer.append(i)
# 			for j in range(i*2,n+1,i):
# 				if chk[j]:
# 					chk[j] = 0
# 	return answer

# t = int(input())

# for _ in range(t):
# 	n = int(input())
# 	arr = ari(n)
# 	minChk = int(1e9)
# 	answer = []
# 	for i in range(len(arr)):
# 		for j in range(len(arr)):
# 			if arr[i] + arr[j] > n:
# 				continue
# 			if arr[i] + arr[j] == n:
# 				if abs(arr[i]-arr[j]) < minChk:
# 					minChk = (abs(arr[i]-arr[j]))
# 					answer = [arr[i],arr[j]]

# 	print(*answer)



def is_prime(n):
	if n == 1:
		return False
	for j in range(2, int(n**0.5) + 1):
		if n % j == 0:
			return False
	return True


for _ in range(int(input())):
	num = int(input())

	a, b = num//2, num//2
	while a > 0:
		if is_prime(a) and is_prime(b):
			print(a, b)
			break
		else:
			a -= 1
			b += 1
