# # N,M = map(int,input().split())

# # visited = [0] * (N+1)
# # answer = []

# # def backTrack(n,tmpList):
# # 	if n == M:
# # 		answer.append(tmpList)
# # 		return
# # 	for i in range(1,N+1):
# # 		if visited[i] == 0:
# # 			visited[i] = 1
# # 			backTrack(n+1,tmpList+[i])
# # 			visited[i] = 0
# # backTrack(0,[])

# # for i in answer:
# # 	print(*i)



# N,M = map(int,input().split())
# visited = [0] * (N+1)
# answer = []

# def bt(n,smallList):
# 	if n == M:
# 		answer.append(smallList)
# 		return
# 	for i in range(1,N+1):
# 		if not visited[i] and (len(smallList) == 0 or i > smallList[-1]):
# 			visited[i] = 1
# 			bt(n+1,smallList+[i])
# 			visited[i] = 0

# bt(0,[])

# for i in answer:
# 	print(*i)


from itertools import combinations

n,m = map(int,input().split())

arr = [i for i in range(1,n+1)]

for seq in combinations(arr,m):
	print(*seq)
