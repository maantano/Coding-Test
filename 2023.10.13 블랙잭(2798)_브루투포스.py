n,m = map(int,input().split())

arr=[list(map(int,input().split()))]
arr.sort()

# cnt = 0
# for i in arr:
tmparr = []
answer = 0
def dfs(cnt,start):
	if cnt == 3:
		if sum(tmparr) <= m:
			answer = max(tmparr,answer)
		return

	for i in range(start,len(arr)):
		tmparr.append(arr[i])
		dfs(cnt+1,i+1)
		tmparr.pop()
print(answer)





