# from itertools import permutations
# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = list(map(int,input().split()))


# per = permutations(arr)
# ans = 0

# for i in per:
# 	s = 0
# 	for j in range(len(i) - 1):
# 		s += abs(i[j]-i[j+1])
# 	if s > ans:
# 		ans = s
# print(ans)


import sys
input = sys.stdin.readline
def next_permutation(list_a):
	k = -1
	m = -1
	# 증가하는 마지막 부분을 가리키는 index k 찾기
	for i in range(len(list_a) -1):
		if list_a[i] < list_a[i+1]:
			k = i

	if k == -1:
		return [-1]
	#  index k 이후 부분 중 값이 k보다 크면서 가장 멀리 있는 index m 찾기
	for i in range(k,len(list_a)):
		if list_a[k] < list_a[i]:
			m = i


	list_a[k],list_a[m] = list_a[m],list_a[k]
	list_a = list_a[:k+1] + sorted(list_a[k+1:])

	return list_a

n = int(input())
a = list(map(int,input().split()))

a.sort()

ans = 0
s = 0
for j in range(len(a)-1):
	s += abs(a[j] - a[j+1])
if s > ans:
	ans = s
arr = a

while True:
	arr = next_permutation(arr)
	if arr == [-1]:
		break
	s = 0

	for j in range(len(arr)-1):
		s+=abs(arr[j]-arr[j+1])
	if s > ans:
		ans = s
print(ans)


