# N,M = map(int,input().split())

# arr=list(map(int,input().split()))
# result = 0

# for i in range(N-2):
# 	for j in range(i+1,N-1):
# 		for k in range(j+1,N):
# 			if arr[i]+arr[j]+arr[k]>M:
# 				continue
# 			else:
# 				result = max(result,arr[i]+arr[j]+arr[k])
# print(result)



from itertools import combinations

n, m = map(int,input().split())

card = list(map(int, input().split()))
com = list(combinations(card, 3))
total = 0
for i in com:
	if sum(i) <= m:
		total = max(total, sum(i))
print(total)
