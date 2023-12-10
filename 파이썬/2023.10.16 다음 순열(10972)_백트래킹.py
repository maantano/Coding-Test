# import sys
# from itertools import permutations,combinations
# input = sys.stdin.readline

# n = int(input())
# arr= list(map(int,input().split()))
# per = permutations(sorted(arr))

# flag = True
# answer = []
# for i in per:
# 	if not flag:
# 		answer = i
# 		break
# 	tmp = []
# 	for j in range(n):
# 		tmp.append(i[j])
# 	if tmp == arr:
# 		flag = False
# if answer:
# 	print(*answer)
# else:
# 	print('-1')

# from itertools import permutations
# import sys

# input = sys.stdin.readline

# n = int(input())
# perm = list(map(int,input().split()))

# permutation = list(permutations(range(1,n+1),n))
# # print(permutation)
# cnt = 0
# for idx,i in enumerate(permutation):
# 	if i == tuple(perm):
# 		cnt = idx+1
# if cnt == len(permutation):
# 	print(-1)
# else:
# 	print(*permutation[cnt])


# ================================================================================

# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = list(map(int,input().split()))


# def nextPermutation(answer):
# 	k = -1
# 	m = -1
# 	for i in range(len(answer)-1):
# 		if answer[i] < answer[i+1]:
# 			k = i
# 	if k == -1:
# 		return -1
# 	for i in range(k,len(answer)):
# 		if answer[k] < answer[i]:
# 			m = i
# 	answer[m],answer[k] = answer[k],answer[m]
# 	answer = answer[:k+1]+sorted(answer[k+1:])
# 	return answer
# while True:
# 	answer = nextPermutation(arr)
# 	if answer == arr:
# 		print(answer)
# 		break
# 	elif answer == -1:
# 		print(-1)
# 		break


n = int(input())
arr = list(map(int,input().split()))

for i in range(n-1,0,-1):
	if arr[i-1] < arr[i]:
		for j in range(n-1,0,-1):
			if arr[i-1] < arr[j]:
				arr[i-1],arr[j] = arr[j],arr[i-1]
				arr = arr[:i] + sorted(arr[i:])
				print(*arr)
				exit()
print(-1)


