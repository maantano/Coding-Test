import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
answer= []

def bt(idx,n,m):
	if idx == m:
		print(*answer)
		return
	overlap = 0
	for i in range(n):
		if overlap != arr[i]:
			if len(answer)>0:
				if answer[-1] <= arr[i]:
					overlap = arr[i]
					answer.append(arr[i])
					bt(idx+1,n,m)
					answer.pop()
			else:
				overlap = arr[i]
				answer.append(arr[i])
				bt(idx+1,n,m)
				answer.pop()

bt(0,n,m)
