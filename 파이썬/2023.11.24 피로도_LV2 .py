k = 80
dungeons = [[80,20],[50,40],[30,10]]
result = 3

answer = 0
N = 0
visited = []

def dfs(k,cnt,dungeons):
	global answer
	if cnt > answer:
		answer  = cnt

	for j in range(N):
		if k >= dungeons[j][0] and not visited[j]:
			visited[j] = 1
			dfs(k - dungeons[j][1],cnt+1,dungeons)
			visited[j] = 0

def solution(k,dungeons):
	global N,visited
	N = len(dungeons)
	visited = [0] * N
	dfs(k,0,dungeons)
	return answer

print(solution(k,dungeons))


solution = lambda k, d: max([solution(k - u, d[:i] + d[i+1:]) + 1 for i, (m, u) in enumerate(d) if k >= m] or [0])
