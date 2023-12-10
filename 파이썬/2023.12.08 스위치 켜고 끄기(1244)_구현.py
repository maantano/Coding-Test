# import sys
# input = sys.stdin.readline


# n = int(input())
# arr = [0]+list(map(int,input().split()))

# t = int(input())

# for i in range(t):
# 	sex,num = map(int,input().split())
# 	if sex == 1:
# 		for j in range(num,n+1,num):
# 			if arr[j]:
# 				arr[j] = 0
# 			else:
# 				arr[j] = 1
# 	else:
# 		if arr[num] == 1:
# 			arr[num] = 0
# 		else:
# 			arr[num] = 1

# 		for j in range((n)//2):
# 			if num-j < 1 or  num+j > n: break

# 			if arr[num-j] != arr[num+j]:
# 				break
# 			else:
# 				if arr[num-j]:
# 					arr[num-j] = arr[num+j] = 0
# 				else:
# 					arr[num-j] = arr[num+j] = 1
# 	print(arr)

# print(arr[1:])




def change(num):
	if switch[num] == 0:
		switch[num] = 1
	else:
		switch[num] = 0
	return


N = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())
for _ in range(students):
	sex, num = map(int, input().split())
	if sex == 1:
		for i in range(num, N+1, num):
			change(i)
	else:
		change(num)
		for k in range(N//2):
			if num + k > N or num - k < 1 : break
			if switch[num + k] == switch[num - k]:
				change(num + k)
				change(num - k)
			else:
				break

for i in range(1, N+1):
	print(switch[i], end = " ")
	if i % 20 == 0 :
		print()

