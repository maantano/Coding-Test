# import sys
# input = sys.stdin.readline


# while True:
# 	n = int(input())
# 	if n == 0:
# 		break
# 	chk = [0,0] + [1] * (n+1)
# 	answer = []
# 	for i in range(2,n+1):
# 		if chk[i]:
# 			answer.append(i)
# 			for j in range(i,n+1,i):
# 				if chk[j]:
# 					chk[j] = 0
# 	a,b = (len(answer)//2)-1 , len(answer) // 2
# 	while True:
# 		if n == answer[a] + answer[b]:
# 			print(n,' = ',answer[a],' + ',answer[b],sep='')
# 			break
# 		elif n < answer[a-1] + answer[b+1]:
# 			a-=1
# 		elif n > answer[a-1] + answer[b+1]:
# 			b-=1


import sys

number = [True] * 1000001

# 소수 list
for i in range(2, int(len(number) ** 0.5) + 1):
	if number[i]:
		for j in range(2 * i, 1000001, i):
			number[j] = False


while 1:
	n = int(sys.stdin.readline())

	if n == 0:
		break

	for i in range(n - 3, 2, -2):
		if (number[i] == True) and (number[n - i] == True):
			print(f"{n} = {n-i} + {i}")
			break
	else:
		print('"Goldbach\'s conjecture is wrong."')
