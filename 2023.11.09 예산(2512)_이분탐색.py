# import sys
# input = sys.stdin.readline

# t = int(input())
# arr = sorted(list(map(int,input().split())))
# limit = int(input())
# s = 0
# e = t-1
# answer = sum(arr)//t

# if sum(arr) < limit:
# 	print(arr[-1])
# else:
# 	while s <= e:
# 		mid = (s+e) // 2
# 		if arr[s] == arr[e]:
# 			break
# 		elif arr[mid] < answer:
# 			s = mid +1
# 		elif arr[mid] > answer:
# 			e = mid
# 	y = 0
# 	for i in range(arr[s-1],arr[e]+1):
# 		tmp = 0
# 		for j in arr:
# 			if j < i:
# 				tmp += j
# 			else:
# 				tmp +=i
# 		if tmp < limit:
# 			y = i
# 	print(y)




import sys
input = sys.stdin.readline

n = int(input())

cities = list(map(int,input().split()))
budgets = int(input())

start, end= 0,max(cities)
if sum(cities) <= budgets:
	print(max(cities))
else:
	while start <= end:
		mid = (start+end) // 2
		total = 0
		for i in cities:
			total += min(i,mid)
		if total <= budgets:
			start = mid + 1
		else:
			end = mid - 1
	print(end)



