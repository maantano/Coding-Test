# from itertools import combinations_with_replacement
# from itertools import combinations

# n,m = map(int,input().split())

# arr = [i for i in range(1,n+1)]
# print(arr)

# for combi in combinations(arr,m):
# 	print(*combi)



N,M = map(int,input().split())
answer = []
visited = [0] * (N+1)

def bt(n,smallList):
	if n == M:
		answer.append(smallList)
		return
	for i in range(1,N+1):
		if not visited[i]:
			bt(n+1,smallList+[i])
bt(0,[])

for i in answer:
	print(*i)

