import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**5)
v = int(input())
arr = [[] for _ in range(v+1)]
for i in range(v):
	m = list(map(int,input().split()))
	l = len(m[1:-1])
	for j in range(1,l,2):
		arr[m[0]].append((m[j],m[j+1]))


# answer = 0
def dfs(start,answer,visited):
	for node,dist in arr[start]:
		if not visited[node]:
			visited[node] = 1
			answer+=dist
			# print('answer =====>',answer)
			dfs(node,answer,visited)
	# print('answer ====>',answer)
	return answer




visited = [0] * (v+1)
total = 0
for i in range(1,v+1):
	total= max(dfs(i,0,visited),total)
	# print('-------–––––––––––––––––')
print(total)
