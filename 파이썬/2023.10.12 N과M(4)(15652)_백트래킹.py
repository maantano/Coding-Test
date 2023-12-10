n , m = map(int,input().split())
visited = [0] * (n+1)
answer = []


def bt(x,smallList):
	if x == m:
		answer.append(smallList)
		return
	for i in range(1,n+1):
		if not visited[i] and (len(smallList) == 0 or i >= smallList[-1]):
			bt(x+1,smallList+[i])
bt(0,[])

for i in answer:
	print(*i)
