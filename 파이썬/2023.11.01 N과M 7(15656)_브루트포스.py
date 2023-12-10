import sys
input = sys.stdin.readline

n,m = map(int,input().split(' '))
arr = list(map(int,input().split(' ')))
arr.sort()

def bt(idx,smalList):
	if idx == m:
		print(*smalList,sep=' ')
		return

	for i in arr:


		bt(idx+1,smalList+[i])

bt(0,[])
