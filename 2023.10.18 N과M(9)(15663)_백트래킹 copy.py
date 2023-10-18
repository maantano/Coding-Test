import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

def bt(idx,smallList):
	for i in range(n):
		if idx == m:
			print('smallList ===>',smallList)
			return
		# if smallList:
		# 	if smallList[-1] == arr[i]:

		smallList[0].append(arr[i])
		smallList[1].append(i)
		bt(idx+1,smallList)
		smallList[0].pop()
		smallList[1].pop()

bt(0,[[],[]])
