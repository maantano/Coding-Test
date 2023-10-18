import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

def bt(idx,smallList):

	for i in range(n):
		if idx == m:
			print(*smallList)
			return
		smallList.append(arr[i])
		bt(idx+1,smallList)
		smallList.pop()

bt(0,[])
