# import sys
# input = sys.stdin.readline


# p,k = map(int,input().split())

# def isPrime(x):
# 	if x == 1:
# 		return False
# 	else:
# 		for i in range(2,int(x**0.5)+1):
# 			if x % i ==0:
# 				return False
# 		return True

# sosu = []
# for i in range(2,p+1):
# 	if isPrime(i):
# 		sosu.append(i)
# answer = []
# flag = True
# for i in range(len(sosu)+1):
# 	for j in range(i+1,len(sosu)+1):
# 		if i * j == p:
# 			if i < k:
# 				print(f'BAD {i}')
# 				flag = False
# 				break
# 			elif j < k:
# 				print(f'BAD {j}')
# 				flag = False
# 				break

# if flag:
# 	print('GOOD')



# 입력
P, K = map(int, input().split())

# K까지 나눠지는 수가 있는지 확인
for i in range(2, K):
	if P % i == 0:
		print("BAD", i)
		break
else:
	print("GOOD")
