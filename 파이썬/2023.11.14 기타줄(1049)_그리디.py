
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arrP = []
arrS = []
for i in range(m):
	p,s = map(int,input().split())
	arrP.append(p)
	arrS.append(s)
arrP.sort()
arrS.sort()
answer = 0

while n > 0:
	if n >=6:
		n-=6
		if arrP[0] > arrS[0] * 6:
			answer+= arrS[0] * 6
		else:
			answer+=arrP[0]
	else:
		answer = min(answer+(arrS[0] * n),answer+arrP[0])
		n = 0
print(answer)
