import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()
answer = []

visitied = [0] * n

def bt(idx,n,m):
	if idx == m:
		print(*answer)
		return

	overlap = 0
	for i in range(n):
		if not visitied[i] and overlap != arr[i]:
			if len(answer) > 0:
				if answer[-1] <= arr[i]:
					visitied[i] = 1
					overlap = arr[i]
					answer.append(arr[i])
					bt(idx+1,n,m)
					visitied[i] = 0
					answer.pop()
			else:
				visitied[i] = 1
				overlap = arr[i]
				answer.append(arr[i])
				bt(idx+1,n,m)
				visitied[i] = 0
				answer.pop()

bt(0,n,m)




