
# BFS
# import sys
# input = sys.stdin.readline

# n = int(input())
# visited = [0]*(n+1)
# from collections import deque

# q = deque([n])

# while q:
# 	tmp = q.popleft()
# 	if tmp == 1:
# 		break
# 	if tmp % 3 == 0 and not visited[tmp//3]:
# 		q.append(tmp//3)
# 		visited[tmp // 3] = visited[tmp]+1
# 	if tmp % 2 == 0 and not visited[tmp//2]:
# 		q.append(tmp//2)
# 		visited[tmp // 2] = visited[tmp]+1
# 	if not visited[tmp-1]:
# 		q.append(tmp-1)
# 		visited[tmp - 1] = visited[tmp]+1
# print(visited[1])


# DP - BottomUp

n = int(input())

visited = [0] * (n+1)

for i in range(2,n+1):
	visited[i] = visited[i-1]+1
	if i % 2 == 0:
		visited[i] = min(visited[i],visited[i//2]+1)
	if i % 3 == 0:
		visited[i] = min(visited[i],visited[i//3]+1)
	print(visited)
print(visited[n])
