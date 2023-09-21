# n = 4
# m = 4
# k = 2
# x = 1

n,m,k,x = map(int,input().split())
g = [[] * n for _ in range(n+2)]
for i in range(n+1):
	x,y = map(int,input().split())
	g[x].append(y)



# g = [
# 	[],
# 	[],
# 	[2,3],
# 	[3,4],
# 	[],
# 	[]
# 	]



from collections import deque
distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])

while q:
	departure = q.popleft()
	for arrival in g[departure+1]:
		if distance[arrival] == -1:
			distance[arrival] = distance[departure]+1
			q.append(arrival)
		# break

chk = False
for i in range(1,n+1):
	if distance[i] == k:
		print(i)
		chk = True
if chk == False:
	print(-1)











