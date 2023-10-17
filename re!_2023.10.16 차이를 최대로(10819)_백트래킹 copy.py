# n = int(input())
# arr = list(map(int,input().split()))
# tmp = []
# for i in range(n // 2):
# 	tmp.append(sorted(arr,reverse=True)[i])
# 	tmp.append(sorted(arr)[i])

# from itertools import permutations
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int,input().split()))

# per = permutations(arr)
# ans = 0

# # # 순열마다 차이를 더해(s), ans 보다 크면 ans를 update
# for i in per:
# 	s = 0
# 	for j in range(len(i)-1):
# 		s += abs(i[j]-i[j+1])
# 	ans = max(s,ans)

# print(ans)



import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

arr.sort()
ans = 0
s = 0
for j in range(len(arr)-1):
	s += abs(arr[j]-arr[j+1])
	s= max(ans,s)

answer = arr


def nextPermutation(answer):
	k = -1
	m = -1


	for i in range(len(answer)-1):
		if answer[i] < answer[i+1]:
			k = i

	if k == -1:
		return [-1]

	for i in range(k,len(answer)):
		if answer[k] < answer[i]:
			m = i
	answer[m],answer[k] = answer[k],answer[m]
	answer = answer[:k+1] + sorted(answer[k+1:])
	return answer


while True:
	answer = nextPermutation(answer)
	if answer == [-1]:
		break
	s = 0

	for j in range(len(answer)-1):
		s+=abs(answer[j]-answer[j+1])

	if s > ans:
		ans = s

print(ans)
