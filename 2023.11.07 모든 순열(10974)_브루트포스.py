import sys

from itertools import permutations
input = sys.stdin.readline
n = int(input())
arr = [i+1 for i in range(n)]
l2 = list(permutations(arr,n))

for i in range(len(l2)):
	print(*l2[i],sep=' ')


import sys
input = sys.stdin.readline
n = int(input())
arr = [i+1 for i in range(n)]
visited= [0] * (n+1)
def chk(idx,l):
	if idx == n:
		print(*l,sep=' ')
		return
	for i in range(1,n+1):
		if not visited[i]:
			visited[i] = 1
			chk(idx+1,l+str(i))
			visited[i] = 0
chk(0,'')
