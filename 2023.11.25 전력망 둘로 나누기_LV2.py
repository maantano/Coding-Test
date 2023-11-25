n = 9
# n = 4
# n= 7

wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
# wires = [[1,2],[2,3],[3,4]]
# wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]


from collections import deque

def bfs(start,g,visited,chk_link):
	q = deque([start])
	visited[start] = True
	cnt = 1
	while q:
		s = q.popleft()
		for adj_v in g[s]:
			if visited[adj_v] == False and chk_link[start][adj_v]:
				q.append(adj_v)
				visited[adj_v] = True
				cnt+=1
	return cnt

def solution(n, wires):
	answer = n
	chk_link = [[True]*(n+1) for _ in range(n+1)]
	g = [[] for i in range(n+1)]

	for i in wires:
		a,b= i
		g[a].append(b)
		g[b].append(a)

	for a,b in wires:
		visited = [0] * (n+1)
		chk_link[a][b] = False
		cnt_a = bfs(a,g,visited,chk_link)
		cnt_b = bfs(b,g,visited,chk_link)
		chk_link[a][b] = True
		answer  = min(answer,abs(cnt_a - cnt_b))
	return answer

solution(n, wires)

def dfs(start,g,visited,chk_link):
	cnt = 1
	visited[start] = 1
	for i in g[start]:
		if not visited[i] and chk_link[start][i]:
			cnt += dfs(i,g,visited,chk_link)
	return cnt

def solution(n,wires):
	answer  = int(1e9)

	chk_link = [[True]*(n+1) for _ in range(n+1)]
	g = [[] for _ in range(n+1)]

	for a,b in wires:
		g[a].append(b)
		g[b].append(a)

	for a,b in wires:
		visited = [0] * (n+1)
		chk_link[a][b] = 0
		cnt_a = dfs(a,g,visited,chk_link)
		cnt_b = dfs(b,g,visited,chk_link)
		chk_link[a][b] = 1
		answer = min(answer,abs(cnt_a - cnt_b))

	return answer

