import sys
input = sys.stdin.readline

n,m = map(int,input().split())
chk = [0,0] + [1]*(n+1)
cnt = 0

for i in range(2,n+1):
	if chk[i]:
		for j in range(i,n+1,i):
			if chk[j]:
				chk[j] = 0
				cnt +=1
				if cnt == m:
					print(j)
					break
