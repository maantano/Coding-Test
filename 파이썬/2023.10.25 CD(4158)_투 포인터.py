# 실패 틀림,
# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# arr1 = [int(input()) for _ in range(n)]
# arr2 = [int(input()) for _ in range(m)]

# arr1.sort()
# arr2.sort()
# cnt = 0
# l,r = 0,0
# while l != n and r != m:
# 	if l == n:
# 		r+=1
# 	elif r == m:
# 		l+=1
# 	else:
# 		if arr1[l] > arr2[r]:
# 			r+=1
# 		elif arr1[l] < arr2[r]:
# 			l+=1
# 		else:
# 			cnt+=1
# 			r+=1
# x,y = map(int,input().split())
# print(cnt)

# 딕셔너리
# import sys
# input = sys.stdin.readline


# while True:
# 	n,m = map(int,input().split())
# 	if n == 0 and m == 0:
# 		break
# 	arr1 = [int(input()) for _ in range(n)]
# 	arr2 = [int(input()) for _ in range(m)]
# 	d = {}
# 	cnt = 0

# 	for i in arr1:
# 		if i not in d:
# 			d[i] = 1
# 		else:
# 			d[i] += 1
# 	for j in arr2:
# 		if j in d:
# 			cnt+=1
# 	print(cnt)

# 인터섹션
# import sys

# while True:
# 	n, m = map(int, sys.stdin.readline().rstrip().split(" "))

# 	if n == m == 0:
# 		break

# 	sg = set(int(sys.stdin.readline().rstrip()) for _ in range(n))
# 	sy = set(int(sys.stdin.readline().rstrip()) for _ in range(m))

# 	res = len(sg.intersection(sy))
# 	print(res)

import sys
input=sys.stdin.readline


while True:
	N,M=map(int,input().split())

	if N==0 and M==0:
		exit(0)

	N_list=[] ; M_list=[]

	for i in range(N):
		N_list.append(int(input()))

	for i in range(M):
		M_list.append(int(input()))

	index_N=0 ; index_M=0 ; total=0

	while index_N<N and index_M<M:

		if N_list[index_N]==M_list[index_M]:
			total+=1
			index_N+=1 ; index_M+=1

		elif N_list[index_N]>M_list[index_M]:
			index_M+=1
		else:
			index_N+=1

	print(total)
