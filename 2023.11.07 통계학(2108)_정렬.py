# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = sorted([int(input().rstrip()) for _ in range(n)])
# print(sum(arr) // len(arr))
# print(arr[len(arr)//2])


# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

import sys
input = sys.stdin.readline
n = int(input())
arr = sorted([int(input().rstrip()) for _ in range(n)])
print(round(sum(arr) / len(arr)))
print(arr[len(arr)//2])

d = {}
for i in arr:
	if i in d:
		d[i] +=1
	else:
		d[i] = 1

mx = max(d.values())
mx_d = []

for i in d:
	if mx == d[i]:
		mx_d.append(i)

if len(mx_d) > 1:
	print(mx_d[1])
else:
	print(mx_d[0])


print(max(arr)-min(arr))
