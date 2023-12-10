import sys
input = sys.stdin.readline

n,m = map(int,input().split(' '))

def dp(idx, smallList):
	if idx == m:
		print(*smallList,sep=' ')
		return
	else:
		for i in range(1,n+1):
			if i in smallList:
				continue
			dp(idx+1,smallList+[i])
dp(0,[])
