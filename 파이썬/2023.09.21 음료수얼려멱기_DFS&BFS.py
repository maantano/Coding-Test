# n = 4
# m = 5
n = 3
m = 3

# g = [
# 	[0,0,1,1,0],
# 	[0,0,0,1,1],
# 	[1,1,1,1,1],
# 	[0,0,0,0,0],
# ]

g = []
for i in range(n):
	g.append(list(map(int,input())))
# print(g)
# v = [[False]* 5 for _ in range(4)]




count = 0

def dfs(x,y):
	if x < 0 or x >= n or y < 0 or y >= m:
	# if x <= -1 or x >= n or y <= -1 or y >= m:
		return False
	if g[x][y] == 0:
		g[x][y] = 1
		dfs(x-1,y)
		dfs(x+1,y)
		dfs(x,y-1)
		dfs(x,y+1)
		return True
	return False
result = 0
for i in range(n):
	for j in range(m):
		if dfs(i,j) == True:
			result +=1
print(result)

