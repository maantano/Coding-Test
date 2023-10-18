import sys
input = sys.stdin.readline


n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

INF = int(1e9)
visited = [0] * 10001

def bt(idx,smallList):
	if idx == m:
		print(*smallList)
		return
	for i in range(n):
		if not visited[i]:
			if smallList:
				if smallList[-1] >= arr[i]:
					continue

			smallList.append(arr[i])
			visited[i] = 1
			bt(idx+1,smallList)
			smallList.pop()
			visited[i] = 0


bt(0,[])
